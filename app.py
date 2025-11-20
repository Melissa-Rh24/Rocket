from repository.rocket_repository import RocketRepository
from repository.launch_site_repository import LaunchSiteRepository
from repository.launch_repository import LaunchRepository
from service.rocket_service import RocketService
from service.launch_site_service import LaunchSiteService
from service.launch_service import LaunchService
from view.login_view import LoginView

def main():
    rocket = RocketRepository()
    site = LaunchSiteRepository()
    launch = LaunchRepository()

    rocket_service = RocketService()
    site_service = LaunchSiteService()
    launch_service = LaunchService()

    login_view = LoginView(rocket_service, site_service, launch_service)
    login_view.show()

if __name__ == "__main__":
    main()
