def create_plant_table_query():
    return """ CREATE TABLE IF NOT EXISTS plant (
                id text PRIMARY KEY,
                water_end_time text
                ); 
            """

def insert_plant_query():
    return  ''' INSERT OR IGNORE INTO plant(id,water_end_time) VALUES(?,?) 
            '''