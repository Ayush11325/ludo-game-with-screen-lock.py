import tkinter as tk
from tkinter import messagebox

class LockScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lock Screen")
        self.root.geometry("300x200")
        self.password = "ayush123"  # change kar skte h

        self.label = tk.Label(root, text="Enter Password:")
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.button = tk.Button(root, text="Unlock", command=self.unlock)
        self.button.pack()

    def unlock(self):
        entered_password = self.password_entry.get()
        if entered_password == self.password:
            messagebox.showinfo("Success", "Lock Screen Unlocked!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Password")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = LockScreenApp(root)
    root.mainloop()
