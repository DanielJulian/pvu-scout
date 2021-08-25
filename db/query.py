def create_plant_table_query():
    return """ CREATE TABLE IF NOT EXISTS plant (
                id text PRIMARY KEY,
                water_end_time text
                ); 
            """

def insert_plant_query():
    return  ''' 
            INSERT OR IGNORE INTO plant(id,water_end_time) VALUES(?,?); 
            '''

def delete_plant_query():
    return  ''' 
            DELETE FROM plant WHERE id=?;
            '''

def merge_plant_query():
    return  ''' 
            INSERT OR REPLACE INTO plant (id, water_end_time) VALUES(?,?); 
            '''

def select_already_refreshed_plants():
    return  '''
            SELECT id, water_end_time
            FROM plant 
            WHERE datetime(water_end_time) < datetime('now','localtime') OR water_end_time IS NULL;
            '''

def select_yet_to_refresh_plants():
    return  '''
            SELECT id, water_end_time
            FROM plant 
            WHERE datetime(water_end_time) > datetime('now','localtime') AND water_end_time IS NOT NULL;
            '''