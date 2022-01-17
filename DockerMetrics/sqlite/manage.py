import sqlite3
import os

class Database:
    def __init__(self, db_location, db_table):
        self.db_location    = db_location
        self.db_table       = db_table

        self.conn   = sqlite3.connect(self.db_location)
        self.cursor = self.conn.cursor()

    def init_db(self, **db_data):
        num             = 0
        data            = f"CREATE TABLE IF NOT EXISTS {self.db_table}("
        for field_name, data_type in db_data.items():
            num += 1
            if len(db_data) == num:
                data += f"{field_name} {data_type}"
                break
            data += f"{field_name} {data_type},"
        data += ")"
        self.cursor.execute(data)

    def create_entry(self, **db_data):
        try:
            # Database => field names
            num     = 0
            data    = f"INSERT INTO {self.db_table}("
            for field_name, user_data in db_data.items():
                num += 1
                if len(db_data) == num:
                    data    += f"{field_name})"
                    break
                data    += f"{field_name}, "
            # Database => user data
            num     = 0
            data    += "VALUES("
            for field_name, user_data in db_data.items():
                num += 1
                if len(db_data) == num:
                    data    += "?)"
                    break
                data    += "?, "
            index       = 1
            user_arr    = [user_data[index] for user_data in db_data.items()]
            self.cursor.execute(data, tuple(user_arr))
            self.conn.commit()
        except sqlite3.IntegrityError as err:
            return err

    def view_db(self, table):
        self.cursor.execute(
        f"""
        SELECT * FROM {table}
        """
        )
        return self.cursor.fetchall()

    def lookup_entry(self, key, primary_key):
        find_entry = (
            f"""
            SELECT * FROM {self.db_table} WHERE {key} = ?
            """
            )
        self.cursor.execute(find_entry,[(primary_key)])
        return self.cursor.fetchall()

    def is_entry(self, **db_data):
        '''
        Check if an entry exist depending on what is inside
        db_data variable. 
        key     -> field_name
        value   -> user_data
        '''
        num     = 0
        data    = f"SELECT * FROM {self.db_table} WHERE "
        for field_name, user_data in db_data.items():
            num += 1
            if len(db_data) == num:
                data += f"{field_name} = ?"
                break
            data += f"{field_name} = ? AND "

        print(data)
        index       = 1
        user_arr    = [user_data[index] for user_data in db_data.items()]
        self.cursor.execute(data, tuple(user_arr))
        print(user_arr)
        print(self.cursor.fetchall())

    def get_length(self):
        self.cursor.execute(
                            f"""
                            SELECT * FROM {self.db_table}
                            """
                            )
        results = self.cursor.fetchall()
        return len(results)

    def update_db(self):
        pass

    def remove_db(self):
        if os.path.isfile(self.db_name):
            os.remove(self.db_name)

    def close_session(self):
        self.conn.close()
