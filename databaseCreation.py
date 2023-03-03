import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="Roin120350", host="127.0.0.1", port="5432")
cur = conn.cursor()
print("Database Connected....")

#Dropping etl table if already exists.

cur.execute("DROP TABLE IF EXISTS etl")

cur.execute("CREATE TABLE etl(PatientID CHAR(50), ModuleName CHAR(100), ModuleStatus CHAR(50), ValidFrom CHAR(50), ValidTill CHAR(50));")
print("Table Created....")


conn.commit()
conn.close()