from copy import deepcopy
import sys
import os
import sqlite3
import pickle
from ShowList import ShowList
import CLI


# initialize database, and return connection


def init_database():
    db_filename = "../data/shows.db"
    db_is_new = not os.path.exists(db_filename)

    if db_is_new:
        with sqlite3.connect(db_filename) as connection:
            with open("../data/ShowTable.sql", 'rt') as f:
                schema = f.read()
                connection.execute(schema)
                return connection

    return sqlite3.connect(db_filename)


# return show_list stored in the database if it exists.
# otherwise return None.


def get_show_list(connection):
    cursor = connection.cursor()

    cursor.execute("select * from ShowTable where id = 1")

    retrieved_data = cursor.fetchall()

    if not len(retrieved_data) == 0:
        for row in retrieved_data:
            idx, show_list = row
            return pickle.loads(show_list)

    return None


# save the show_list object passed, into the database


def save_show_list(connection, show_list):
    pickled_show_list = pickle.dumps(show_list)
    cursor = connection.cursor()

    cursor.execute("select * from ShowTable")
    record_exists = cursor.fetchall()

    query = "update ShowTable set Show_List = ? where id = 1"

    if len(record_exists) == 0:
        query = "insert into ShowTable (Show_List) values (?)"

    cursor.execute(query, (pickled_show_list,))
    connection.commit()


# print user help screen


def help_input():
    print("MalaShowTracker\n" +
          "===============\n" +
          "Commands:\n" +
          "add_show\n" +
          "remove_show\n" +
          "get_show\n" +
          "get_all_shows\n" +
          "increment_show_episode\n" +
          "increment_show_season\n" +
          "help\n" +
          "===============")


# print out show object nicely (calls __str__ of show)


def pretty_print_show(show):
    print("----------------------------------")
    print(show)
    print("----------------------------------")


def main():
    connection = init_database()

    show_list = get_show_list(connection)

    # check to see if the list has been modified, and needs to be saved.
    modify_check_list = deepcopy(show_list)

    if show_list is None:
        show_list = ShowList()

    # remove the name of the script from arguments
    args = sys.argv
    args.remove(sys.argv[0])

    entered_arg_loop = False

    for arg in args:
        entered_arg_loop = True
        arg = arg.lower()

        if arg == "add_show":
            show_list.add_show()

        elif arg == "remove_show":
            show_list.remove_show(CLI.request_show_name())

        elif arg == "get_show":
            pretty_print_show(show_list.find_show(CLI.request_show_name()).show)

        elif arg == "get_all_shows":
            for show in show_list.shows:
                pretty_print_show(show)

        elif arg == "increment_show_episode":
            show_list.increment_show(CLI.request_show_name())

        elif arg == "increment_show_season":
            show_list.increment_show_season(CLI.request_show_name())

        else:
            help_input()

    if not entered_arg_loop:
        help_input()

    if not show_list == modify_check_list:
        save_show_list(connection, show_list)

    connection.close()


if __name__ == "__main__":
    main()
