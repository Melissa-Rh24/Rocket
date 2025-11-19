from repository.launch_repository import LaunchRepository

class LaunchService:
    launch_repository = LaunchRepository()

    @classmethod
    def save(cls, launch):
        return cls.launch_repository.save(launch)

    @classmethod
    def update(cls, launch):
        launch_result = cls.launch_repository.find_by_id(launch.launch_id)
        if launch_result:
            return cls.launch_repository.update(launch)
        else:
            raise Exception("Launch Not Found !!!")

    @classmethod
    def delete(cls, launch_id):
        launch = cls.launch_repository.find_by_id(launch_id)
        if launch:
            cls.launch_repository.delete(launch_id)
            return launch
        else:
            raise Exception("Launch Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.launch_repository.find_all()

    @classmethod
    def find_by_id(cls, launch_id):
        return cls.launch_repository.find_by_id(launch_id)

    @classmethod
    def find_by_rocket_id(cls, rocket_id):
        return cls.launch_repository.find_by_rocket_id(rocket_id)

    @classmethod
    def find_by_site_id(cls, site_id):
        return cls.launch_repository.find_by_site_id(site_id)
