import tkinter as tk
from tkinter import messagebox

class LaunchView:
    def __init__(self, launch_service):
        self.launch_service = launch_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("Launch Management")
        self.window.geometry("480x380")
        self.window.resizable(False, False)

        tk.Label(self.window, text="Launch Information", font=("Arial", 13, "bold")).grid(
            row=0, column=0, columnspan=2, pady=15
        )


        tk.Label(self.window, text="Rocket ID:").grid(row=1, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Launch Site ID:").grid(row=2, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Angle (°):").grid(row=3, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Velocity (m/s):").grid(row=4, column=0, padx=20, pady=8, sticky="e")
        tk.Label(self.window, text="Range :").grid(row=5,column=0, padx=20, pady=8, sticky="e")


        self.rocket_id_entry = tk.Entry(self.window, width=35)
        self.site_id_entry = tk.Entry(self.window, width=35)
        self.angle_entry = tk.Entry(self.window, width=35)
        self.velocity_entry = tk.Entry(self.window, width=35)
        self.range = tk.Entry(self.window, width=35)




        self.rocket_id_entry.grid(row=1, column=1, pady=8)
        self.site_id_entry.grid(row=2, column=1, pady=8)
        self.angle_entry.grid(row=3, column=1, pady=8)
        self.velocity_entry.grid(row=4, column=1, pady=8)
        self.range.grid(row=5, column=1, pady=8)


        btn_frame = tk.Frame(self.window)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=35)

        tk.Button(btn_frame, text="Add Launch", width=14, command=self.add_launch).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Delete Launch", width=14, command=self.add_launch).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Update Launch", width=14, command=self.add_launch).pack(side="left", padx=12)



        self.window.mainloop()

    def add_launch(self):
        rocket_id = self.rocket_id_entry.get()
        site_id = self.site_id_entry.get()
        angle = self.angle_entry.get()
        velocity = self.velocity_entry.get()

        if not rocket_id or not site_id or not angle or not velocity:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        self.launch_service.add_launch(rocket_id, site_id, angle, velocity)
        messagebox.showinfo("Success", "Launch added successfully!")
        self.clear_inputs()

    def clear_inputs(self):
        self.rocket_id_entry.delete(0, tk.END)
        self.site_id_entry.delete(0, tk.END)
        self.angle_entry.delete(0, tk.END)
        self.velocity_entry.delete(0, tk.END)

