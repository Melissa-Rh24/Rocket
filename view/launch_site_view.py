import tkinter as tk
from tkinter import messagebox

class LaunchSiteView:
    def __init__(self, site_service):
        self.service = site_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("launch site management")

        tk.Label(self.window, text="name").grid(row=0, column=0)
        tk.Label(self.window, text="location").grid(row=1, column=0)

        self.name_entry = tk.Entry(self.window)
        self.location_entry = tk.Entry(self.window)

        self.name_entry.grid(row=0, column=1)
        self.location_entry.grid(row=1, column=1)

        tk.Button(self.window, text="add site", command=self.add_site).grid(row=2, column=0, columnspan=2)
        tk.Button(self.window, text="list sites", command=self.list_sites).grid(row=3, column=0, columnspan=2)

        self.text_area = tk.Text(self.window, width=50, height=10)
        self.text_area.grid(row=4, column=0, columnspan=2)

        self.window.mainloop()

    def add_site(self):
        try:
            name = self.name_entry.get()
            location = self.location_entry.get()
            site = self.service.create_site(name, location)
            messagebox.showinfo("success", f"site added with id {site.site_id}")
        except Exception as e:
            messagebox.showerror("error", str(e))

    def list_sites(self):
        sites = self.service.get_all_sites()
        self.text_area.delete('1.0', tk.END)
        for s in sites:
            self.text_area.insert(tk.END, f"id: {s.site_id}, name: {s.name}, location: {s.location}\n")
