import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',               # change to your MySQL username
    port=3306,
    password='apurbaict',   # change to your MySQL password
    # database='test_db',        # change to your database name
    # charset='utf8mb4'
)

# Create a cursor
cursor = conn.cursor()

# Run a simple query
cursor.execute("SELECT VERSION();")

# Fetch and print the result
result = cursor.fetchone()
print("MySQL version:", result[0])

# Clean up
cursor.close()
conn.close()
