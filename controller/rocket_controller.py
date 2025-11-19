class RocketController:
    def __init__(self, rocket_service, rocket_view):
        self.service = rocket_service
        self.view = rocket_view

    def add_rocket(self):
        self.view.add_rocket()

    def list_rockets(self):
        self.view.list_rockets()
