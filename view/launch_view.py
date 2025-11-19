import tkinter as tk
from tkinter import messagebox

class LaunchView:
    def __init__(self, launch_service, rocket_service, site_service):
        self.launch_service = launch_service
        self.rocket_service = rocket_service
        self.site_service = site_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("launch management")

        tk.Label(self.window, text="rocket id").grid(row=0, column=0)
        tk.Label(self.window, text="site id").grid(row=1, column=0)
        tk.Label(self.window, text="angle").grid(row=2, column=0)
        tk.Label(self.window, text="velocity").grid(row=3, column=0)
        tk.Label(self.window, text="range").grid(row=4, column=0)
        tk.Label(self.window, text="max height").grid(row=5, column=0)

        self.rocket_entry = tk.Entry(self.window)
        self.site_entry = tk.Entry(self.window)
        self.angle_entry = tk.Entry(self.window)
        self.velocity_entry = tk.Entry(self.window)
        self.range_entry = tk.Entry(self.window)
        self.height_entry = tk.Entry(self.window)

        self.rocket_entry.grid(row=0, column=1)
        self.site_entry.grid(row=1, column=1)
        self.angle_entry.grid(row=2, column=1)
        self.velocity_entry.grid(row=3, column=1)
        self.range_entry.grid(row=4, column=1)
        self.height_entry.grid(row=5, column=1)

        tk.Button(self.window, text="add launch", command=self.add_launch).grid(row=6, column=0, columnspan=2)
        tk.Button(self.window, text="list launches", command=self.list_launches).grid(row=7, column=0, columnspan=2)

        self.text_area = tk.Text(self.window, width=60, height=15)
        self.text_area.grid(row=8, column=0, columnspan=2)

        self.window.mainloop()

    def add_launch(self):
        try:
            rocket_id = int(self.rocket_entry.get())
            site_id = int(self.site_entry.get())
            angle = float(self.angle_entry.get())
            velocity = float(self.velocity_entry.get())
            range_ = float(self.range_entry.get())
            max_height = float(self.height_entry.get())
            launch = self.launch_service.create_launch(rocket_id, site_id, angle, velocity, range_, max_height)
            messagebox.showinfo("success", f"launch added with id {launch.launch_id}")
        except Exception as e:
            messagebox.showerror("error", str(e))

    def list_launches(self):
        launches = self.launch_service.get_all_launches()
        self.text_area.delete('1.0', tk.END)
        for l in launches:
            self.text_area.insert(
                tk.END,
                f"id: {l.launch_id}, rocket_id: {l.rocket_id}, site_id: {l.site_id}, "
                f"angle: {l.angle}, velocity: {l.velocity}, range: {l.range}, max_height: {l.max_height}\n"
            )
