import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re
import csv
from datetime import datetime


# Custom Exceptions
class InvalidInputException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

# OOP Classes
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

class Device:
    def __init__(self, model, serial):
        self.model = model
        self.serial = serial
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)

class Repair:
    def __init__(self, issue, technician, status='Pending', service_cost=0.0, parts_cost=0.0, tax_rate=0.1):
        self.issue = issue
        self.technician = technician
        self.status = status
        self.service_cost = service_cost
        self.parts_cost = parts_cost
        if tax_rate == 0:
            raise ZeroDivisionError("Tax rate cannot be zero to avoid potential division issues in advanced calculations.")
        self.tax = (service_cost + parts_cost) * tax_rate
        self.total = service_cost + parts_cost + self.tax
        self.date = datetime.now().strftime('%Y-%m-%d')

    # Overloading example (though Python uses duck typing, simulate with __str__)
    def __str__(self):
        return f"Repair: {self.issue}, Status: {self.status}, Total: {self.total}"

# Inheritance with overriding and super()
class SpecialRepair(Repair):
    def __init__(self, issue, technician, extra_fee=0.0, **kwargs):
        super().__init__(issue, technician, **kwargs)
        self.extra_fee = extra_fee
        self.total += extra_fee

    # Overriding
    def __str__(self):
        return super().__str__() + f", Extra Fee: {self.extra_fee}"

# Database Initialization
def init_db():
    conn = sqlite3.connect('repairmate.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (id INTEGER PRIMARY KEY, customer_id INTEGER, model TEXT, serial TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS repairs
                 (id INTEGER PRIMARY KEY, device_id INTEGER, issue TEXT, technician TEXT, status TEXT,
                  service_cost REAL, parts_cost REAL, tax REAL, total REAL, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
    # Default users (plain text for simplicity)
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin', 'Admin')")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (2, 'tech', 'tech', 'Technician')")
    conn.commit()
    return conn

# Main Application
class RepairMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RepairMate")
        self.conn = init_db()
        self.current_user = None
        self.show_login()

    def show_login(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            c = self.conn.cursor()
            c.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
            result = c.fetchone()
            if result:
                self.current_user = User(username, result[0])
                self.login_frame.destroy()
                self.show_main_menu()
            else:
                raise InvalidInputException("Invalid credentials")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_main_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()
        try:
            if self.current_user.role == 'Admin':
                tk.Button(self.menu_frame, text="Add Customer", command=self.add_customer).pack()
                tk.Button(self.menu_frame, text="Add Device", command=self.add_device).pack()
                tk.Button(self.menu_frame, text="Add Repair", command=self.add_repair).pack()
                tk.Button(self.menu_frame, text="Generate Invoice", command=self.generate_invoice).pack()
                tk.Button(self.menu_frame, text="Search Repairs", command=self.search_repairs).pack()
            elif self.current_user.role == 'Technician':
                tk.Button(self.menu_frame, text="Add Repair", command=self.add_repair).pack()
                tk.Button(self.menu_frame, text="Search Repairs", command=self.search_repairs).pack()
            else:
                raise AccessDeniedException("Unknown role")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_customer(self):
        try:
            if self.current_user.role != 'Admin':
                raise AccessDeniedException("Access denied")
            self.cust_window = tk.Toplevel(self.root)
            tk.Label(self.cust_window, text="Name").grid(row=0, column=0)
            name_entry = tk.Entry(self.cust_window)
            name_entry.grid(row=0, column=1)
            tk.Label(self.cust_window, text="Email").grid(row=1, column=0)
            email_entry = tk.Entry(self.cust_window)
            email_entry.grid(row=1, column=1)
            tk.Label(self.cust_window, text="Phone").grid(row=2, column=0)
            phone_entry = tk.Entry(self.cust_window)
            phone_entry.grid(row=2, column=1)

            def save():
                try:
                    name = name_entry.get()
                    if not name:
                        raise InvalidInputException("Name is required")
                    c = self.conn.cursor()
                    c.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                              (name, email_entry.get(), phone_entry.get()))
                    self.conn.commit()
                    customer = Customer(name, email_entry.get(), phone_entry.get())
                    messagebox.showinfo("Success", "Customer added")
                    self.cust_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                finally:
                    pass  # Could close resources if needed

            tk.Button(self.cust_window, text="Save", command=save).grid(row=3, columnspan=2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_device(self):
        try:
            if self.current_user.role != 'Admin':
                raise AccessDeniedException("Access denied")
            self.dev_window = tk.Toplevel(self.root)
            tk.Label(self.dev_window, text="Customer ID").grid(row=0, column=0)
            cust_id_entry = tk.Entry(self.dev_window)
            cust_id_entry.grid(row=0, column=1)
            tk.Label(self.dev_window, text="Model").grid(row=1, column=0)
            model_entry = tk.Entry(self.dev_window)
            model_entry.grid(row=1, column=1)
            tk.Label(self.dev_window, text="Serial").grid(row=2, column=0)
            serial_entry = tk.Entry(self.dev_window)
            serial_entry.grid(row=2, column=1)

            def save():
                try:
                    cust_id = int(cust_id_entry.get())
                    c = self.conn.cursor()
                    c.execute("SELECT id FROM customers WHERE id=?", (cust_id,))
                    if not c.fetchone():
                        raise InvalidInputException("Customer not found")
                    c.execute("INSERT INTO devices (customer_id, model, serial) VALUES (?, ?, ?)",
                              (cust_id, model_entry.get(), serial_entry.get()))
                    self.conn.commit()
                    device = Device(model_entry.get(), serial_entry.get())
                    messagebox.showinfo("Success", "Device added")
                    self.dev_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid Customer ID")
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            tk.Button(self.dev_window, text="Save", command=save).grid(row=3, columnspan=2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_repair(self):
        try:
            if self.current_user.role not in ['Admin', 'Technician']:
                raise AccessDeniedException("Access denied")
            self.rep_window = tk.Toplevel(self.root)
            tk.Label(self.rep_window, text="Device ID").grid(row=0, column=0)
            dev_id_entry = tk.Entry(self.rep_window)
            dev_id_entry.grid(row=0, column=1)
            tk.Label(self.rep_window, text="Issue").grid(row=1, column=0)
            issue_entry = tk.Entry(self.rep_window)
            issue_entry.grid(row=1, column=1)
            tk.Label(self.rep_window, text="Technician").grid(row=2, column=0)
            tech_entry = tk.Entry(self.rep_window)
            tech_entry.grid(row=2, column=1)
            tk.Label(self.rep_window, text="Status").grid(row=3, column=0)
            status_entry = tk.Entry(self.rep_window)
            status_entry.grid(row=3, column=1)
            tk.Label(self.rep_window, text="Service Cost").grid(row=4, column=0)
            service_entry = tk.Entry(self.rep_window)
            service_entry.grid(row=4, column=1)
            tk.Label(self.rep_window, text="Parts Cost").grid(row=5, column=0)
            parts_entry = tk.Entry(self.rep_window)
            parts_entry.grid(row=5, column=1)
            tk.Label(self.rep_window, text="Tax Rate (e.g., 0.1)").grid(row=6, column=0)
            tax_entry = tk.Entry(self.rep_window)
            tax_entry.insert(0, "0.1")
            tax_entry.grid(row=6, column=1)
            tk.Label(self.rep_window, text="Special Repair? (yes/no)").grid(row=7, column=0)
            special_entry = tk.Entry(self.rep_window)
            special_entry.grid(row=7, column=1)
            tk.Label(self.rep_window, text="Extra Fee (if special)").grid(row=8, column=0)
            extra_entry = tk.Entry(self.rep_window)
            extra_entry.grid(row=8, column=1)

            def save():
                try:
                    dev_id = int(dev_id_entry.get())
                    service = float(service_entry.get() or 0)
                    parts = float(parts_entry.get() or 0)
                    tax_rate = float(tax_entry.get() or 0.1)
                    extra = float(extra_entry.get() or 0)
                    is_special = special_entry.get().lower() == 'yes'
                    c = self.conn.cursor()
                    c.execute("SELECT id FROM devices WHERE id=?", (dev_id,))
                    if not c.fetchone():
                        raise InvalidInputException("Device not found")
                    if is_special:
                        repair = SpecialRepair(issue_entry.get(), tech_entry.get(), extra_fee=extra,
                                               status=status_entry.get() or 'Pending',
                                               service_cost=service, parts_cost=parts, tax_rate=tax_rate)
                    else:
                        repair = Repair(issue_entry.get(), tech_entry.get(), status=status_entry.get() or 'Pending',
                                        service_cost=service, parts_cost=parts, tax_rate=tax_rate)
                    c.execute("""INSERT INTO repairs (device_id, issue, technician, status, service_cost, parts_cost, tax, total, date)
                                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                              (dev_id, repair.issue, repair.technician, repair.status,
                               repair.service_cost, repair.parts_cost, repair.tax, repair.total, repair.date))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Repair added")
                    self.rep_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid numeric input")
                except ZeroDivisionError as e:
                    messagebox.showerror("Error", str(e))
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            tk.Button(self.rep_window, text="Save", command=save).grid(row=9, columnspan=2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_invoice(self):
        try:
            if self.current_user.role != 'Admin':
                raise AccessDeniedException("Access denied")
            self.inv_window = tk.Toplevel(self.root)
            tk.Label(self.inv_window, text="Repair ID").grid(row=0, column=0)
            rep_id_entry = tk.Entry(self.inv_window)
            rep_id_entry.grid(row=0, column=1)

            def gen():
                try:
                    rep_id = int(rep_id_entry.get())
                    c = self.conn.cursor()
                    c.execute("""SELECT customers.name, devices.model, repairs.issue, repairs.technician, repairs.status, 
                                        repairs.service_cost, repairs.parts_cost, repairs.tax, repairs.total, repairs.date
                                 FROM repairs 
                                 JOIN devices ON repairs.device_id = devices.id
                                 JOIN customers ON devices.customer_id = customers.id
                                 WHERE repairs.id = ?""", (rep_id,))
                    row = c.fetchone()
                    if not row:
                        raise InvalidInputException("Repair not found")
                    # Save to CSV
                    filename = f'invoice_{rep_id}.csv'
                    with open(filename, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(['Customer', 'Model', 'Issue', 'Technician', 'Status', 'Service Cost', 'Parts Cost', 'Tax', 'Total', 'Date'])
                        writer.writerow(row)
                    # Also save to text for alternative
                    with open(f'invoice_{rep_id}.txt', 'w') as f:
                        f.write("\n".join([f"{header}: {value}" for header, value in zip(['Customer', 'Model', 'Issue', 'Technician', 'Status', 'Service Cost', 'Parts Cost', 'Tax', 'Total', 'Date'], row)]))
                    messagebox.showinfo("Success", f"Invoice saved to {filename} and .txt")
                    self.inv_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            tk.Button(self.inv_window, text="Generate", command=gen).grid(row=1, columnspan=2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def search_repairs(self):
        try:
            self.search_window = tk.Toplevel(self.root)
            tk.Label(self.search_window, text="Search Pattern (regex, e.g., Pending)").grid(row=0, column=0)
            pattern_entry = tk.Entry(self.search_window)
            pattern_entry.grid(row=0, column=1)
            tk.Label(self.search_window, text="Field (model or status)").grid(row=1, column=0)
            field_entry = tk.Entry(self.search_window)
            field_entry.grid(row=1, column=1)
            tree = ttk.Treeview(self.search_window, columns=('Repair ID', 'Model', 'Status', 'Issue'), show='headings')
            tree.heading('Repair ID', text='Repair ID')
            tree.heading('Model', text='Model')
            tree.heading('Status', text='Status')
            tree.heading('Issue', text='Issue')
            tree.grid(row=3, columnspan=2)

            def search():
                pattern_str = pattern_entry.get()
                field = field_entry.get().lower()
                if field not in ['model', 'status']:
                    raise InvalidInputException("Invalid field: must be 'model' or 'status'")
                try:
                    regex = re.compile(pattern_str, re.IGNORECASE)  # Using modifier for case-insensitivity
                except re.error:
                    messagebox.showerror("Error", "Invalid regex pattern")
                    return
                c = self.conn.cursor()
                if field == 'model':
                    c.execute("""SELECT repairs.id, devices.model, repairs.status, repairs.issue 
                                 FROM repairs JOIN devices ON repairs.device_id = devices.id""")
                else:
                    c.execute("""SELECT id, '', status, issue FROM repairs""")
                rows = c.fetchall()
                matching = [row for row in rows if regex.search(row[1] if field == 'model' else row[2])]
                for i in tree.get_children():
                    tree.delete(i)
                for row in matching:
                    tree.insert('', 'end', values=row)

            tk.Button(self.search_window, text="Search", command=search).grid(row=2, columnspan=2)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = RepairMateApp(root)
    root.mainloop()