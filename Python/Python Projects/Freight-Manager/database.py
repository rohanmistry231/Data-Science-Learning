""" Helper function to interact with database"""
import sqlite3
from data_types import Box, Container, Freight


def create_database(filename):
    """ Creating all the tables """
    if not filename:
        filename = ":memory:"


    connection = sqlite3.connect(filename)

    connection.execute("PRAGMA foreign_keys = 1;")
    connection.commit()

    ddl_query = """
        DROP TABLE IF EXISTS boxes;
        CREATE TABLE boxes (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            x REAL NOT NULL,
            y REAL NOT NULL,
            z REAL NOT NULL,
            CONSTRAINT max_volume CHECK(x *y * z < 10)
        );
        DROP TABLE IF EXISTS freight;
        CREATE TABLE freight(
            id INTEGER PRIMARY KEY,
            container_id INTEGER NOT NULL,
            box_id INTEGER NOT NULL REFERENCES boxes(id) ON DELETE CASCADE
        );
        DROP TABLE IF EXISTS app_config;
        CREATE TABLE app_config( 
                id INTEGER PRIMARY KEY,
                key TEXT NOT NULL UNIQUE,
                value TEXT NOT NULL
        );
        
        CREATE VIEW IF NOT EXISTS containers
        AS
            SELECT container_id, round(sum(x * y * z),2) as occupied_volume
            FROM freight f
            LEFT JOIN boxes b on f.box_id = b.id 
            GROUP BY container_id;
        
    """

    connection.executescript(ddl_query)
    return connection


def seed_data(connection):
    """
    Entering box data and configuration details like price, capacity and max volume for further use

    """
    starter_boxes = [
        ('a1', 1.1, 1.2, 2),
        ('a2', 2, 2, 2),
        ('a3', 1, 1, 3),
        ('a4', 3, 2, 1),
    ]

    app_config_data = [
        ('MAX_CONTAINER_STORAGE', 30),
        ('COST_PER_CONTAINER', 200),
        ('CUBIC_METER_CHARGEOUT', 40)
    ]

    connection.executemany("INSERT INTO boxes (name, x, y, z) VALUES (?, ?, ?, ?);",
                           starter_boxes)
    connection.executemany("INSERT INTO app_config(key, value) VALUES(?, ?);", app_config_data)
    connection.commit()


def get_config(connection):
    """ fetching storage, price details from the app_config table"""
    fetched = connection.execute("SELECT key, value from app_config;").fetchall()
    if fetched:
        return {k: v for k, v in fetched}


def add_box(connection, box):
    """
    adding a box in the database
    :param connection:
    :param box:
    :return: insert data and return messages to user
    """
    try:
        connection.execute("""
            INSERT INTO boxes(name, x, y, z) values(?, ?, ?, ?) 
        """, box)
        connection.commit()
        print("\nBox saved successfully!\n")
    except sqlite3.IntegrityError as e:
        print("\nSorry! Could not processed box to the database: ", e, "\n")




def get_all_boxes(connection):
    """
    fetch all boxes

    """
    fetched = connection.execute("SELECT * FROM boxes;").fetchall()
    if fetched:
        return [Box(*b) for b in fetched]
    return fetched


def get_one_box(connection, by_name=None, by_id=None):
    """
    get one box detail

    """
    fetched =None
    if by_name is not None:
        fetched = connection.execute("SELECT * FROM boxes WHERE name=?", (by_name,)).fetchone()
    elif by_id is not None:
        fetched = connection.execute("SELECT * FROM boxes WHERE id=?", (by_id,)).fetchone()
    if fetched:
        return Box(*fetched)



def get_container(connection, by_id=None):
    """
    if found, get a container details.

    """
    fetched = None
    if by_id is not None:
        fetched = connection.execute("SELECT * FROM containers WHERE container_id= ?", (by_id,)).fetchone()
    if fetched:
        return Container(*fetched)

def get_all_containers(connection):
    """ fetching all containers details """
    fetched = connection.execute("SELECT * FROM containers;").fetchall()

    if fetched:
        return [Container(*i) for i in fetched]






def add_box_to_container(connection, box_id=None, container_id=None):
    """
    adding a box to container by id or name
    :param connection:
    :param box_id:
    :param container_id:
    """
    if box_id is not None and container_id is not None:
        connection.execute("""
            INSERT INTO freight (container_id, box_id) VALUES (:cid, :bid)""", {
                "cid": container_id,
                "bid": box_id
            }
        )
        connection.commit()


def get_all_freight(connection):
    fetched = connection.execute("SELECT * FROM freight;").fetchall()
    if fetched:
        return [Freight(*i) for i in fetched]



