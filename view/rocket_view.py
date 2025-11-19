import tkinter as tk
from tkinter import messagebox

class RocketView:
    def __init__(self, rocket_service):
        self.service = rocket_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("rocket management")

        tk.Label(self.window, text="name").grid(row=0, column=0)
        tk.Label(self.window, text="mass").grid(row=1, column=0)
        tk.Label(self.window, text="fuel capacity").grid(row=2, column=0)
        tk.Label(self.window, text="max speed").grid(row=3, column=0)

        self.name_entry = tk.Entry(self.window)
        self.mass_entry = tk.Entry(self.window)
        self.fuel_entry = tk.Entry(self.window)
        self.speed_entry = tk.Entry(self.window)

        self.name_entry.grid(row=0, column=1)
        self.mass_entry.grid(row=1, column=1)
        self.fuel_entry.grid(row=2, column=1)
        self.speed_entry.grid(row=3, column=1)

        tk.Button(self.window, text="add rocket", command=self.add_rocket).grid(row=4, column=0, columnspan=2)
        tk.Button(self.window, text="list rockets", command=self.list_rockets).grid(row=5, column=0, columnspan=2)

        self.text_area = tk.Text(self.window, width=50, height=10)
        self.text_area.grid(row=6, column=0, columnspan=2)

        self.window.mainloop()

    def add_rocket(self):
        try:
            name = self.name_entry.get()
            mass = float(self.mass_entry.get())
            fuel = float(self.fuel_entry.get())
            speed = float(self.speed_entry.get())
            rocket = self.service.create_rocket(name, mass, fuel, speed)
            messagebox.showinfo("success", f"rocket added with id {rocket.rocket_id}")
        except Exception as e:
            messagebox.showerror("error", str(e))

    def list_rockets(self):
        rockets = self.service.get_all_rockets()
        self.text_area.delete('1.0', tk.END)
        for r in rockets:
            self.text_area.insert(tk.END, f"id: {r.rocket_id}, name: {r.name}, mass: {r.mass}, fuel: {r.fuel_capacity}, speed: {r.max_speed}\n")
