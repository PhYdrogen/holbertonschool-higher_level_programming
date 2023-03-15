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

        db_connect = DB.connect(host="localhost",
                                port=3306,
                                user=mysql_username,
                                passwd=mysql_password,
                                db=database_name)
        db_cursor = db_connect.cursor()
        db_cursor.execute(
            " SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON states.id = cities.state_id \
                WHERE states.name = '{}'"
            .format(state_name_searched)
            )
        rows_selected = db_cursor.fetchall()
        sep = ""
        for row in rows_selected:
            print(sep, end="")
            print(row[0], end="")
            sep = ", "
        print()