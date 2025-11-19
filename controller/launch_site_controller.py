class LaunchSiteController:
    def __init__(self, site_service, site_view):
        self.service = site_service
        self.view = site_view

    def add_launch_site(self):
        self.view.add_launch_site()

    def list_launch_sites(self):
        self.view.list_launch_sites()
