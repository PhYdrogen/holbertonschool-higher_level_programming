#!/usr/bin/python3
""" DOCUMENTATIONS """
if __name__ == "__main__":
    import MySQLdb as DB
    import sys

    if len(sys.argv) == 5:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name_searched = sys.argv[4]
        if state_name_searched.find(";") != -1:
            safe = state_name_searched.split(";")[0][:-1]
        else:
            safe = state_name_searched
        db_connect = DB.connect(host="localhost",
                                port=3306,
                                user=mysql_username,
                                passwd=mysql_password,
                                db=database_name)
        db_cursor = db_connect.cursor()
        db_cursor.execute(
            "SELECT * FROM states WHERE \
                states.name LIKE BINARY '{}';"
            .format(safe)
            )
        rows_selected = db_cursor.fetchall()
        for row in rows_selected:
            print(row)
