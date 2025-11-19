import tkinter as tk
from view.rocket_view import RocketView
from view.launch_site_view import LaunchSiteView
from view.launch_view import LaunchView

class LoginView:
    def __init__(self, rocket_service, site_service, launch_service):
        self.rocket_service = rocket_service
        self.site_service = site_service
        self.launch_service = launch_service

    def show(self):
        self.window = tk.Tk()
        self.window.title("login view")

        tk.Label(self.window, text="welcome to rocket launch management").pack(pady=10)

        tk.Button(self.window, text="rocket management", width=30, command=self.open_rocket_view).pack(pady=5)
        tk.Button(self.window, text="launch site management", width=30, command=self.open_site_view).pack(pady=5)
        tk.Button(self.window, text="launch management", width=30, command=self.open_launch_view).pack(pady=5)
        tk.Button(self.window, text="exit", width=30, command=self.window.destroy).pack(pady=20)

        self.window.mainloop()

    def open_rocket_view(self):
        self.window.destroy()
        rocket_view = RocketView(self.rocket_service)
        rocket_view.show()

    def open_site_view(self):
        self.window.destroy()
        site_view = LaunchSiteView(self.site_service)
        site_view.show()

    def open_launch_view(self):
        self.window.destroy()
        launch_view = LaunchView(self.launch_service, self.rocket_service, self.site_service)
        launch_view.show()
