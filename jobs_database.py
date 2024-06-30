import sqlite3


class JobsDatabase:
    def create_database(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT,
                price INTEGER
        )""")
    
        cursor.execute("""INSERT INTO products(name, price) VALUES("GTA VI", "20000")""")
        cursor.execute("""INSERT INTO products(name, price) VALUES("Monrtal Combat", "1200")""")
        
        connection.commit()
        connection.close()
        
    def delete_database(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        cursor.execute("DROP TABLE products")

        connection.commit()
        connection.close()
        
    def working_database(self, request_to_database = False):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        if request_to_database:
            cursor.execute(request_to_database)
            connection.commit()
    
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()

        connection.close()
        return data
    def get_operation(self, request_to_database):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        
        cursor.execute(request_to_database)
        data = cursor.fetchone()

        connection.close()
        return data


def generation_table(data):
    result_table = ""
    
    for i in data:
        result_table += "<tr>"
        for j in i:
            result_table += f"<td>{j}</td>"
    
        result_table += f"<td><input type='checkbox' onchange='on_check_box(this)' id='{i[0]}'/></td></tr>"
    
    return result_table