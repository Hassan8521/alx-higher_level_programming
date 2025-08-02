#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
