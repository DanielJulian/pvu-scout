# https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
from .query import create_plant_table_query, insert_plant_query
from sqlite3 import Error


class Database():
    
    def __init__(self):
        self.create_table(create_plant_table_query())

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(r"plants_sqlite.db", isolation_level=None)
            # print("Successfully connected to the database. Version:", sqlite3.version)
        except Error as e:
            print(e)
        
        return conn

    def create_table(self, create_table_sql):
        try:
            conn = self.create_connection()
            with conn:
                cur = conn.cursor()
                cur.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_plant(self, plant):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            plant_id = plant['id']
            end_time = None
            if 'water_end_time' in plant:
                end_time = plant['water_end_time'].isoformat()
            cur.execute(insert_plant_query(), (plant_id, end_time))

    def select_all_plants(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT id, water_end_time FROM plant")
            rows = cur.fetchall()
            return rows
    
    def select_already_refreshed_plants(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT id, water_end_time FROM plant WHERE date(water_end_time) < date('now') OR water_end_time = NULL")
            rows = cur.fetchall()
            return rows

    def select_yet_to_refresh_plants(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT id, water_end_time FROM plant WHERE date(water_end_time) > date('now') AND water_end_time IS NOT NULL")
            rows = cur.fetchall()
            return rows