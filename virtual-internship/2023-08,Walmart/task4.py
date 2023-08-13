import csv
import sqlite3

# CREATE TABLE
def create_table(cursor):
    # CREATE A TABLE FOR DATA IN DATA_0
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_0 (
            origin_warehouse TEXT,
            destination_store TEXT,
            product TEXT,
            on_time BOOLEAN,
            product_quantity INTEGER,
            driver_identifier TEXT
        )
    """)

    # CREATE A TABLE FOR DATA IN DATA_1 AND DATA_2
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_1 (
            shipment_identifier TEXT,
            product TEXT,
            on_time TEXT,
            origin_warehouse TEXT,
            destination_store TEXT
        )
    """)
# INSERT DATA_0
def insert_data_0(cursor):
    with open('data/shipping_data_0.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # skip the first line
        for row in csv_reader:
            origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier = row
            cursor.execute("INSERT INTO shipping_data_0 (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier) VALUES (?, ?, ?, ?, ?, ?)",
                           (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier))
            
# INSERT DATA_1 AND DATA_2
def insert_data_2(cursor):
    with open('data/shipping_data_2.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # skip the first line
        data_2_rows = [row for row in csv_reader] # put the data into variable "data_2_rows"

    with open('data/shipping_data_1.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            shipment_identifier, product, on_time = row
            matching_rows = [r for r in data_2_rows if r[0] == shipment_identifier] # if shipment_identifier matches in a specific row in data_2
            if matching_rows: # if match exists
                origin_warehouse, destination_store, driver_identifier = matching_rows[0][1], matching_rows[0][2], matching_rows[0][3]
                cursor.execute("INSERT INTO shipping_data_1 (shipment_identifier, product, on_time, origin_warehouse, destination_store) VALUES (?, ?, ?, ?, ?)",
                               (shipment_identifier, product, on_time, origin_warehouse, destination_store))

if __name__ == "__main__":
    con = sqlite3.connect('shipment_database.db')
    cur = con.cursor()

    create_table(cur) 
    insert_data_0(cur)
    insert_data_2(cur)

    con.commit()
    con.close()