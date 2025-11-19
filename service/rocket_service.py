from repository.rocket_repository import RocketRepository

class RocketService:
    rocket_repository = RocketRepository()

    @classmethod
    def save(cls, rocket):
        return cls.rocket_repository.save(rocket)

    @classmethod
    def add(cls, rocket):
        return cls.rocket_repository.add(rocket)


    @classmethod
    def update(cls, rocket):
        rocket_result = cls.rocket_repository.find_by_id(rocket.id)
        if rocket_result:
            return cls.rocket_repository.update(rocket)
        else:
            raise Exception("Rocket Not Found !!!")



    @classmethod
    def delete(cls, rocket_id):
        rocket = cls.rocket_repository.find_by_id(rocket_id)
        if rocket:
            cls.rocket_repository.delete(rocket_id)
            return rocket
        else:
            raise Exception("Rocket Not Found !!!")

    @classmethod
    def find_all(cls):
        rocket_list = cls.rocket_repository.find_all()
        if rocket_list:
            return rocket_list
        else:
            raise Exception("No Rockets Found !!!")

    @classmethod
    def find_by_id(cls, rocket_id):
        rocket = cls.rocket_repository.find_by_id(rocket_id)
        if rocket:
            return rocket
        else:
            raise Exception("Rocket Not Found !!!")

    @classmethod
    def find_by_name(cls, name):
        rocket_list = cls.rocket_repository.find_by_name(name)
        if rocket_list:
            return rocket_list
        else:
            raise Exception("No Rockets Found With This Name !!!")

    @classmethod
    def get_all(cls, rocket):
        return cls.rocket_repository.get_all(rocket)


