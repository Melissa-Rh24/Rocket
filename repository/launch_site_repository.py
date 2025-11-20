import sqlite3
from model.launch_site import LaunchSite


class LaunchSiteRepository:

    def __init__(self, db_path="database/init.db"):
        self.db_path = db_path

    def connect(self):
        self.connection = sqlite3.connect("rocket.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, site):
        self.connect()
        self.cursor.execute("""
            insert into launch_sites (name, location)
            values (?, ?)""",
         [site.name, site.location])
        site.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return site

    def update(self, site):
        self.connect()
        self.cursor.execute("""
            update launch_sites
            set name = ?,
                location = ?
            where id = ?""",
         [site.name, site.location, site.id])
        self.connection.commit()
        self.disconnect()
        return site

    def delete(self, site_id):
        self.connect()
        self.cursor.execute("delete from launch_sites where id = ?", [site_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from launch_sites")
        site_list = [LaunchSite(*site) for site in self.cursor.fetchall()]
        self.disconnect()
        return site_list

    def find_by_id(self, site_id):
        self.connect()
        self.cursor.execute("select * from launch_sites where id = ?", [site_id])
        site_id = self.cursor.fetchone()
        self.disconnect()
        if site_id:
            return LaunchSite(*site_id)
        return None

    def find_by_name(self, name):
        self.connect()
        self.cursor.execute("select * from launch_sites where name like ?", [name + "%"])
        site_list = [LaunchSite(*site) for site in self.cursor.fetchall()]
        self.disconnect()
        return site_list

