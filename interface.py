#basic gui for project
import tkinter as tk
from tkinter import messagebox

def add_to_whitelist():
    messagebox.showinfo("Whitelist", "Device added to whitelist!")

def scan_in_sandbox():
    messagebox.showwarning("Sandbox", "Scanning in sandbox...")

def show_logs():
    messagebox.showinfo("Logs", "Opening event logs...")

# Root window
root = tk.Tk()
root.title("Secure USB Access Controller")
root.geometry("400x300")

# Status Label
status_label = tk.Label(root, text="USB Status: 🔒 Blocked", fg="red", font=("Arial", 12, "bold"))
status_label.pack(pady=10)

# Device Info
info_frame = tk.Frame(root)
info_frame.pack()

tk.Label(info_frame, text="VID:").grid(row=0, column=0)
tk.Label(info_frame, text="1234").grid(row=0, column=1)

tk.Label(info_frame, text="PID:").grid(row=1, column=0)
tk.Label(info_frame, text="5678").grid(row=1, column=1)

tk.Label(info_frame, text="Type:").grid(row=2, column=0)
tk.Label(info_frame, text="Mass Storage").grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add to Whitelist", command=add_to_whitelist).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Scan in Sandbox", command=scan_in_sandbox).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="View Logs", command=show_logs).grid(row=0, column=2, padx=5)

# Run GUI
root.mainloop()
