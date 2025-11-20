import sqlite3

def init_db():
    conn = sqlite3.connect("rocket.db")
    cursor = conn.cursor()

    cursor.execute("""
    create table if not exists rocket(
    rocket_id integer primary key autoincrement,
    name text not null,
    mass real,
    fuel_capacity real,
    max_speed real
)
""")

    cursor.execute("""
    create table if not exists launch_site (
    site_id integer primary key autoincrement,
    name text not null,
    location text
)
""")

    cursor.execute("""
    create table if not exists launch (
    launch_id integer primary key autoincrement,
    rocket_id integer,
    site_id integer,
    angle real,
    velocity real,
    range real,
    max_height real,
    foreign key (rocket_id) references rocket(rocket_id) on delete cascade,
    foreign key (site_id) references launch_site(site_id) on delete cascade
)
""")

    conn.commit()
    conn.close()
    print("database initialized successfully")

if __name__ == "__main":
    init_db()





