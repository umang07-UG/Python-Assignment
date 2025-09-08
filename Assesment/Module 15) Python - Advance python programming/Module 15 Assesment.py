import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re
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
            raise ZeroDivisionError("Tax rate cannot be zero")
        self.tax = (service_cost + parts_cost) * tax_rate
        self.total = service_cost + parts_cost + self.tax
        self.date = datetime.now().strftime('%Y-%m-%d')

    def __str__(self):  
        return f"Repair: {self.issue}, Status: {self.status}, Total: {self.total}"


class SpecialRepair(Repair):
    def __init__(self, issue, technician, extra_fee=0.0, **kwargs):
        super().__init__(issue, technician, **kwargs)
        self.extra_fee = extra_fee
        self.total += extra_fee

    def __str__(self):  # overriding
        return super().__str__() + f", Extra Fee: {self.extra_fee}"

# DB
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
    # default users
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin', 'Admin')")
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (2, 'tech', 'tech', 'Technician')")
    conn.commit()
    return conn

# Main
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
            messagebox.showerror("Error", "Unknown role")

    def add_customer(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Name").grid(row=0, column=0)
        name_entry = tk.Entry(win); name_entry.grid(row=0, column=1)
        tk.Label(win, text="Email").grid(row=1, column=0)
        email_entry = tk.Entry(win); email_entry.grid(row=1, column=1)
        tk.Label(win, text="Phone").grid(row=2, column=0)
        phone_entry = tk.Entry(win); phone_entry.grid(row=2, column=1)

        def save():
            try:
                if not name_entry.get():
                    raise InvalidInputException("Name required")
                c = self.conn.cursor()
                c.execute("INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
                          (name_entry.get(), email_entry.get(), phone_entry.get()))
                self.conn.commit()
                messagebox.showinfo("Done", "Customer saved")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save).grid(row=3, columnspan=2)

    def add_device(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Customer ID").grid(row=0, column=0)
        cust_id_entry = tk.Entry(win); cust_id_entry.grid(row=0, column=1)
        tk.Label(win, text="Model").grid(row=1, column=0)
        model_entry = tk.Entry(win); model_entry.grid(row=1, column=1)
        tk.Label(win, text="Serial").grid(row=2, column=0)
        serial_entry = tk.Entry(win); serial_entry.grid(row=2, column=1)

        def save():
            try:
                cid = int(cust_id_entry.get())
                c = self.conn.cursor()
                c.execute("SELECT id FROM customers WHERE id=?", (cid,))
                if not c.fetchone():
                    raise InvalidInputException("Customer not found")
                c.execute("INSERT INTO devices (customer_id, model, serial) VALUES (?, ?, ?)",
                          (cid, model_entry.get(), serial_entry.get()))
                self.conn.commit()
                messagebox.showinfo("Done", "Device saved")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save).grid(row=3, columnspan=2)

    def add_repair(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Device ID").grid(row=0, column=0)
        dev_entry = tk.Entry(win); dev_entry.grid(row=0, column=1)
        tk.Label(win, text="Issue").grid(row=1, column=0)
        issue_entry = tk.Entry(win); issue_entry.grid(row=1, column=1)
        tk.Label(win, text="Technician").grid(row=2, column=0)
        tech_entry = tk.Entry(win); tech_entry.grid(row=2, column=1)
        tk.Label(win, text="Service Cost").grid(row=3, column=0)
        service_entry = tk.Entry(win); service_entry.grid(row=3, column=1)
        tk.Label(win, text="Parts Cost").grid(row=4, column=0)
        parts_entry = tk.Entry(win); parts_entry.grid(row=4, column=1)

        def save():
            try:
                did = int(dev_entry.get())
                c = self.conn.cursor()
                c.execute("SELECT id FROM devices WHERE id=?", (did,))
                if not c.fetchone():
                    raise InvalidInputException("Device not found")
                repair = Repair(issue_entry.get(), tech_entry.get(),
                                service_cost=float(service_entry.get() or 0),
                                parts_cost=float(parts_entry.get() or 0))
                c.execute("INSERT INTO repairs (device_id, issue, technician, status, service_cost, parts_cost, tax, total, date) VALUES (?,?,?,?,?,?,?,?,?)",
                          (did, repair.issue, repair.technician, repair.status,
                           repair.service_cost, repair.parts_cost, repair.tax, repair.total, repair.date))
                self.conn.commit()
                messagebox.showinfo("Done", "Repair saved")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save).grid(row=5, columnspan=2)

    def generate_invoice(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Repair ID").grid(row=0, column=0)
        rep_entry = tk.Entry(win); rep_entry.grid(row=0, column=1)

        def gen():
            try:
                rid = int(rep_entry.get())
                c = self.conn.cursor()
                c.execute("""SELECT customers.name, devices.model, repairs.issue, repairs.technician, repairs.status,
                             repairs.service_cost, repairs.parts_cost, repairs.tax, repairs.total, repairs.date
                             FROM repairs 
                             JOIN devices ON repairs.device_id = devices.id
                             JOIN customers ON devices.customer_id = customers.id
                             WHERE repairs.id=?""", (rid,))
                row = c.fetchone()
                if not row:
                    raise InvalidInputException("Repair not found")

                # text 
                headers = ['Customer','Model','Issue','Technician','Status','Service Cost','Parts Cost','Tax','Total','Date']
                with open(f"invoice_{rid}.txt","w") as f:
                    for h,v in zip(headers,row):
                        f.write(f"{h}: {v}\n")

                messagebox.showinfo("Done", f"Invoice saved as invoice_{rid}.txt")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Generate", command=gen).grid(row=1, columnspan=2)

    def search_repairs(self):
        win = tk.Toplevel(self.root)
        tk.Label(win, text="Pattern (regex)").grid(row=0, column=0)
        pat_entry = tk.Entry(win); pat_entry.grid(row=0, column=1)
        tk.Label(win, text="Field (model/status)").grid(row=1, column=0)
        field_entry = tk.Entry(win); field_entry.grid(row=1, column=1)
        tree = ttk.Treeview(win, columns=("ID","Model","Status","Issue"), show="headings")
        for col in ("ID","Model","Status","Issue"):
            tree.heading(col, text=col)
        tree.grid(row=3, columnspan=2)

        def do_search():
            try:
                pat = pat_entry.get()
                field = field_entry.get().lower()
                reg = re.compile(pat, re.IGNORECASE)
                c = self.conn.cursor()
                if field=="model":
                    c.execute("SELECT repairs.id, devices.model, repairs.status, repairs.issue FROM repairs JOIN devices ON repairs.device_id=devices.id")
                else:
                    c.execute("SELECT id,'',status,issue FROM repairs")
                rows = c.fetchall()
                tree.delete(*tree.get_children())
                for r in rows:
                    if reg.search(r[1] if field=="model" else r[2]):
                        tree.insert("", "end", values=r)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Search", command=do_search).grid(row=2, columnspan=2)

if __name__=="__main__":
    root = tk.Tk()
    app = RepairMateApp(root)
    root.mainloop()

