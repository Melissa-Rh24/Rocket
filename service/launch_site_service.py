from repository.launch_site_repository import LaunchSiteRepository

class LaunchSiteService:
    launch_site_repository = LaunchSiteRepository()

    @classmethod
    def save(cls, launch_site):
        return cls.launch_site_repository.save(launch_site)

    @classmethod
    def update(cls, launch_site):
        launch_site_result = cls.launch_site_repository.find_by_id(launch_site.launch_site_id)
        if launch_site_result:
            return cls.launch_site_repository.update(launch_site)
        else:
            raise Exception("Launch Site Not Found !!!")

    @classmethod
    def delete(cls, launch_site_id):
        launch_site = cls.launch_site_repository.find_by_id(launch_site_id)
        if launch_site:
            cls.launch_site_repository.delete(launch_site_id)
            return launch_site
        else:
            raise Exception("Launch Site Not Found !!!")


    @classmethod
    def find_by_name(cls, name):
        return cls.launch_site_repository.find_by_name(name)

    @classmethod
    def find_by_id(cls, launch_site_id):
        return cls.launch_site_repository.find_by_id(launch_site_id)

    @classmethod
    def find_all(cls):
        return cls.launch_site_repository.find_all()
