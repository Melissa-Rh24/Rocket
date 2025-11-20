import sqlite3
from model.launch import Launch
from model.launch_site import LaunchSite


class LaunchRepository:

    def __init__(self, db_path="database/init.db"):
        self.db_path = db_path

    def connect(self):
        self.connection = sqlite3.connect("rocket.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, launch):
        self.connect()
        self.cursor.execute("""
            insert into launches (name, angle, max_height, rocket_id)
            values (?, ?, ?, ?)""",
         [launch.name, launch.angle, launch.max_height, launch.rocket_id])
        launch.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return launch

    def add(self, launch):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
               insert into launches (name, angle, max_height, rocket_id)
            values (?, ?, ?, ?)""",
           [launch.name, launch.angle, launch.max_height, launch.rocket_id])
        conn.commit()
        conn.close()
        return f"Launch '{launch.name}' added successfully."

    def update(self, launch):
        self.connect()
        self.cursor.execute("""
            update launches
            set name = ?,
                angle = ?,
                max_height = ?,
                rocket_id = ?
            where id = ?""",
         [launch.name, launch.angle, launch.max_height, launch.rocket_id, launch.id])
        self.connection.commit()
        self.disconnect()
        return launch

    def delete(self, launch_id):
        self.connect()
        self.cursor.execute("delete from launches where id = ?", [launch_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from launches")
        launch_list = [Launch(*launch) for launch in self.cursor.fetchall()]
        self.disconnect()
        return launch_list

    def find_by_id(self, launch_id):
        self.connect()
        self.cursor.execute("select * from launches where id = ?", [launch_id])
        launch_id = self.cursor.fetchone()
        self.disconnect()
        if launch_id:
            return Launch(*launch_id)
        return None

    def find_by_rocket_id(self, rocket_id):
        self.connect()
        self.cursor.execute("select * from launches where rocket_id=?", [rocket_id])
        launch_list = [Launch(*rocket) for rocket in self.cursor.fetchall()]
        self.disconnect()
        return launch_list

    def find_by_site_id(self, site_id):
        self.connect()
        self.cursor.execute("select * from sites where site_id=?", [site_id])
        launch_site_list = [LaunchSite(*site) for site in self.cursor.fetchall()]
        self.disconnect()
        return launch_site_list


