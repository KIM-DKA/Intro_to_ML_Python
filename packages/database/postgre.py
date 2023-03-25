import psycopg2
import pandas as pd
import numpy as np 
import tqdm

class PostgreSQL:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to PostgreSQL")
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

    def close(self):
        if(self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

    def execute(self,query): 
        self.cursor.execute(query)
        self.connection.commit()
        print("Run query")

    def read_data(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(rows, columns=column_names)
        print("Read data")
        return df

    def write_data(self, data, table_name, chunk_size=100):
        data = data.replace({np.nan:None})
        for i in tqdm.tqdm(range(0, len(data), chunk_size)):
            chunk = data[i:i+chunk_size]
            records = chunk.to_dict('records')
            query = f"INSERT INTO {table_name} ({','.join(records[0].keys())}) VALUES ({','.join(['%s'] * len(records[0]))});"
            self.cursor.executemany(query, [tuple(record.values()) for record in records])
        self.connection.commit()
        print("Data written to PostgreSQL")

if __name__ == "__main__":
    # Initialize the PostgreSQL class
    postgres = PostgreSQL(host="localhost", database="database_name", user="user_name", password="password", port="80")
    # Connect to the database
    postgres.connect()
    # Retrieve data
    df = postgres.read_data("SELECT * FROM table_name;")
    print(df)
    # Write data
    data = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
    postgres.write_data(data, "table_name")
    # Close the connection
    postgres.close()

