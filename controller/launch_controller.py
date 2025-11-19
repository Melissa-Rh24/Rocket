class LaunchController:
    def __init__(self, launch_service, launch_view):
        self.service = launch_service
        self.view = launch_view

    def add_launch(self):
        self.view.add_launch()

    def list_launches(self):
        self.view.list_launches()
