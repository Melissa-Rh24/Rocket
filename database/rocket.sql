create table if not exists rocket(
    rocket_id integer primary key autoincrement,
    name text not null,
    mass real,
    fuel_capacity real,
    max_speed real
);

-- table launch_site
create table if not exists launch_site (
    site_id integer primary key autoincrement,
    name text not null,
    location text
);

-- table launch
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
);
