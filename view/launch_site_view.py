import tkinter as tk
from tkinter import messagebox

class LaunchSiteView:
    def __init__(self, site_service):
        self.site_service = site_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("Launch Site Management")
        self.window.geometry("400x250")
        self.window.resizable(False, False)


        tk.Label(self.window, text="Launch Site Information", font=("Arial", 13, "bold")).grid(
            row=0, column=0, columnspan=2, pady=15
        )


        tk.Label(self.window, text="Site Name:").grid(row=1, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Location:").grid(row=2, column=0, padx=20, pady=8, sticky="e")

        self.name_entry = tk.Entry(self.window, width=35)
        self.location_entry = tk.Entry(self.window, width=35)

        self.name_entry.grid(row=1, column=1, pady=8)
        self.location_entry.grid(row=2, column=1, pady=8)

        btn_frame = tk.Frame(self.window)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=35)

        tk.Button(btn_frame, text="Add Site", width=14, command=self.add_site).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Delete Site", width=14, command=self.add_site).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Update Site", width=14, command=self.add_site).pack(side="left", padx=12)





        self.window.mainloop()

    def add_site(self):
        name = self.name_entry.get()
        location = self.location_entry.get()

        if not name or not location:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        self.site_service.add_site(name, location)
        messagebox.showinfo("Success", "Launch site added successfully!")
        self.name_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)

