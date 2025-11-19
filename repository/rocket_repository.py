import sqlite3
from model.rocket import Rocket


class RocketRepository:

    def connect(self):
        self.connection = sqlite3.connect("rocket.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, rocket):
        self.connect()
        self.cursor.execute("""
            insert into rockets (name, mass, fuel_capacity, max_speed)
            values (?, ?, ?, ?)""",
                            [ rocket.name, rocket.mass, rocket.fuel_capacity, rocket.max_speed])
        rocket.rocket_id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()

    def add(self, rocket):
        self.rocket.append(rocket)
        return f"Rocket '{rocket.name}' added successfully."


    def update(self,rocket):
        self.connect()
        self.cursor.execute( """update rockets
            set name = ?,
                mass = ?,
                fuel_capacity = ?,
                max_speed = ?
            where id = ?""",
               [rocket.name, rocket.mass, rocket.fuel_capacity, rocket.max_speed])
        self.connection.commit()
        self.disconnect()
        return rocket

    def delete(self, rocket_id):
        self.connect()
        self.cursor.execute("delete from rockets where id = ?", [rocket_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from rockets")
        rocket_list = [Rocket(*rocket) for rocket in self.cursor.fetchall()]
        self.disconnect()
        return rocket_list

    def find_by_id(self, rocket_id):
        self.connect()
        self.cursor.execute("select * from rockets where id = ?", [rocket_id])
        rocket = self.cursor.fetchone()
        self.disconnect()
        if rocket:
            return Rocket(*rocket)
        return None


    def find_by_name(self, name):
        self.connect()
        self.cursor.execute("select * from rockets where name like ?", [name + "%"])
        rocket_list = [Rocket(*rocket) for rocket in self.cursor.fetchall()]
        self.disconnect()
        return rocket_list


    def get_all(self):
        return self.rocket

