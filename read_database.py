import duckdb
import time

try:
    print("Trying to lock the database with read only mode.")
    conn = duckdb.connect("test.db", read_only=True)
    print("Acquired the lock.")
    while True:
        time.sleep(10.0)
except KeyboardInterrupt:
    print("Releasing the database lock.")
