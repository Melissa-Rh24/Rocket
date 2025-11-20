from repository.launch_site_repository import LaunchSiteRepository
from model.launch_site import LaunchSite

class LaunchSiteService:
    launch_site_repository = LaunchSiteRepository()

    @classmethod
    def add_site(cls, name, location):
        site = LaunchSite(
            site_id=None,
            name=name,
            location=location
        )
        return cls.launch_site_repository.save(site)

    @classmethod
    def save(cls, site):
        return cls.launch_site_repository.save(site)

    @classmethod
    def update(cls, site):
        site_result = cls.launch_site_repository.find_by_id(site.site_id)
        if site_result:
            return cls.launch_site_repository.update(site)
        else:
            raise Exception("Launch Site Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.launch_site_repository.find_all()

    @classmethod
    def find_by_id(cls, site_id):
        return cls.launch_site_repository.find_by_id(site_id)
