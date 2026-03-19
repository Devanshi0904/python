import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector as sql

def insert():
    con =sql.connect(
        host="127.0.0.1",
        user = "root",
        password = "root",
        port =3306,
        database="meditrack"
    )

# ---------- Database Setup ----------
conn = sql.connect("meditrack.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    disease TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS bills(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    amount REAL
)
""")

conn.commit()

# ---------- Patient Class ----------
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def save(self):
        cur.execute("INSERT INTO patients(name, age, disease) VALUES (?, ?, ?)",
                    (self.name, self.age, self.disease))
        conn.commit()

# ---------- GUI ----------
app = tk.Tk()
app.title("MediTrack System")
app.geometry("300x350")

# ---------- Widgets ----------
tk.Label(app, text="Patient Name").pack()
name_entry = tk.Entry(app)
name_entry.pack()

tk.Label(app, text="Age").pack()
age_entry = tk.Entry(app)
age_entry.pack()

tk.Label(app, text="Disease").pack()
disease_entry = tk.Entry(app)
disease_entry.pack()

def save_patient():
    try:
        p = Patient(name_entry.get(), int(age_entry.get()), disease_entry.get())
        p.save()
        messagebox.showinfo("Saved", "Patient added successfully!")
    except Exception:
        messagebox.showerror("Error", "Invalid data entered!")

tk.Button(app, text="Save Patient", command=save_patient).pack(pady=5)

# ---------- Billing ----------
tk.Label(app, text="Enter Patient ID for Billing").pack()
bill_id = tk.Entry(app)
bill_id.pack()

tk.Label(app, text="Amount").pack()
bill_amount = tk.Entry(app)
bill_amount.pack()

def save_bill():
    try:
        cur.execute("INSERT INTO bills(patient_id, amount) VALUES(?, ?)",
                    (int(bill_id.get()), float(bill_amount.get())))
        conn.commit()
        messagebox.showinfo("Saved", "Bill recorded!")
    except:
        messagebox.showerror("Error", "Invalid billing input!")

tk.Button(app, text="Save Bill", command=save_bill).pack(pady=5)

# ---------- Regex Search ----------
tk.Label(app, text="Search Disease Pattern").pack()
search_entry = tk.Entry(app)
search_entry.pack()

def search():
    pattern = search_entry.get()
    cur.execute("SELECT name, disease FROM patients")
    patients = cur.fetchall()

    result = [p[0] for p in patients if re.search(pattern, p[1], re.IGNORECASE)]

    messagebox.showinfo("Results", "\n".join(result) if result else "No match found.")

tk.Button(app, text="Search", command=search).pack(pady=10)

app.mainloop()
