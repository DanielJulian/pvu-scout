# https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
import db.query as query
from datetime import datetime
from sqlite3 import Error


class Database():
    
    def __init__(self):
        self.create_table(query.create_plant_table_query())

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            if (col[0] == 'water_end_time' and row[idx]):
                d[col[0]] = datetime.strptime(row[idx].split(".")[0], '%Y-%m-%dT%H:%M:%S')
            else:
                d[col[0]] = row[idx]
        return d


    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(r"plants_sqlite.db", isolation_level=None)
            conn.row_factory = self.dict_factory
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
            cur.execute(query.insert_plant_query(), (plant_id, end_time))

    def merge_plant(self, plant):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            plant_id = plant['id']
            end_time = None
            if 'water_end_time' in plant:
                end_time = plant['water_end_time'].isoformat()
            cur.execute(query.merge_plant_query(), (plant_id, end_time))
    
    def select_already_refreshed_plants(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(query.select_already_refreshed_plants())
            rows = cur.fetchall()
            return rows

    def select_yet_to_refresh_plants(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(query.select_yet_to_refresh_plants())
            rows = cur.fetchall()
            return rows