import tkinter as tk
from tkinter import messagebox

class RocketView:
    def __init__(self, rocket_service):
        self.rocket_service = rocket_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("Rocket Management")
        self.window.geometry("450x320")
        self.window.resizable(False, False)


        title = tk.Label(self.window, text="Rocket Information", font=("Arial", 13, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=15)


        tk.Label(self.window, text="Rocket Name:").grid(row=1, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Mass (kg):").grid(row=2, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Fuel Capacity (L):").grid(row=3, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Max Speed (m/s):").grid(row=4, column=0, padx=20, pady=8, sticky="e")


        self.name_entry = tk.Entry(self.window, width=35)
        self.mass_entry = tk.Entry(self.window, width=35)
        self.fuel_entry = tk.Entry(self.window, width=35)
        self.speed_entry = tk.Entry(self.window, width=35)

        self.name_entry.grid(row=1, column=1, pady=8)
        self.mass_entry.grid(row=2, column=1, pady=8)
        self.fuel_entry.grid(row=3, column=1, pady=8)
        self.speed_entry.grid(row=4, column=1, pady=8)


        button_frame = tk.Frame(self.window)
        button_frame.grid(row=6, column=0, columnspan=2, pady=30)

        tk.Button(button_frame, text="Add Rocket", width=14, command=self.add_rocket).pack(side="left", padx=12)
        tk.Button(button_frame, text="Delete Rocket", width=14, command=self.add_rocket).pack(side="left", padx=12)
        tk.Button(button_frame, text="Update Rocket", width=14, command=self.add_rocket).pack(side="left", padx=12)




        self.window.mainloop()

    def add_rocket(self):
        name = self.name_entry.get()
        mass = self.mass_entry.get()
        fuel = self.fuel_entry.get()
        speed = self.speed_entry.get()

        if not name or not mass or not fuel or not speed:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        from model.rocket import Rocket
        rocket = Rocket(name=name, mass=mass, fuel_capacity=fuel, max_speed=speed)

        try:
            self.rocket_service.add(rocket)
            messagebox.showinfo("Success", "Rocket added successfully!")
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.mass_entry.delete(0, tk.END)
        self.fuel_entry.delete(0, tk.END)
        self.speed_entry.delete(0, tk.END)
