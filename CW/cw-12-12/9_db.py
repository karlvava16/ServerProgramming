import json
import mysql.connector

class Db:
    def __init__(self, config):
        if isinstance(config, dict):
            if "db" in config:
                self.connection = mysql.connector.connect(**config["db"])
            else:
                self.connection = mysql.connector.connect(**config)
        elif isinstance(config, str):
            try:
                with open(config, 'r') as file:
                    file_config = json.load(file)
                if "db" in file_config:
                    self.connection = mysql.connector.connect(**file_config["db"])
                else:
                    self.connection = mysql.connector.connect(**file_config)
            except FileNotFoundError:
                raise ValueError(f"Configuration file '{config}' not found.")
            except json.JSONDecodeError:
                raise ValueError(f"Configuration file '{config}' contains invalid JSON.")
        else:
            raise TypeError("Config must be a dictionary or a string (file path).")

    def get_connection(self):
        return self.connection

def main():
    try:
        db = Db('db_config.json')
        print("DB connected")

        # db = Db({
        #     'host': 'localhost',
        #     'port': 3308,
        #     'user': 'py213_user',
        #     'password': 'py213_pass',
        #     'database': 'py_knp_213',
        #     'charset': 'utf8mb4',
        #     'collation': 'utf8mb4_unicode_ci',
        # })
        # print("DB connected")

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")

if __name__ == "__main__":
    main()
