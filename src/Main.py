import os
import pickle
import sqlite3
import sys
import typing
from copy import deepcopy

import CLI
import Show
import ShowList


def init_database() -> sqlite3.Connection:
    """
    Initialize database and return connection
    """
    db_filename: str = "../data/shows.db"
    db_is_new: bool = not os.path.exists(db_filename)

    if db_is_new:
        with sqlite3.connect(db_filename) as connection:
            with open("../data/ShowTable.sql", 'rt') as f:
                schema: str = f.read()
                connection.execute(schema)
                return connection

    return sqlite3.connect(db_filename)


def get_show_list(connection: sqlite3.Connection) -> ShowList.ShowList or None:
    """
    Return show_list stored in database if it exists, otherwise return None
    """
    cursor: sqlite3.Cursor = connection.cursor()

    cursor.execute("select * from ShowTable where id = 1")

    retrieved_data: typing.List[sqlite3.Row] = cursor.fetchall()

    if not len(retrieved_data) == 0:
        for row in retrieved_data:
            idx, show_list = row
            return pickle.loads(show_list)

    return None


def save_show_list(connection: sqlite3.Connection, show_list: ShowList.ShowList):
    """
    Save the show_list object given into the database
    """
    pickled_show_list: bytes = pickle.dumps(show_list)
    cursor: sqlite3.Cursor = connection.cursor()

    cursor.execute("select * from ShowTable")
    record_exists: typing.List[sqlite3.Row] = cursor.fetchall()

    query: str = "update ShowTable set Show_List = ? where id = 1"

    if len(record_exists) == 0:
        query = "insert into ShowTable (Show_List) values (?)"

    cursor.execute(query, (pickled_show_list,))
    connection.commit()


def main():
    """
    Handles input from user and calls appropriate functions
    """
    connection: sqlite3.Connection = init_database()

    show_list: ShowList.ShowList or None = get_show_list(connection)

    # check to see if the list has been modified, and needs to be saved.
    modify_check_list: ShowList.ShowList or None = deepcopy(show_list)

    if show_list is None:
        show_list: ShowList.ShowList = ShowList.ShowList()

    # remove the name of the script from arguments
    args: list = sys.argv
    args.remove(sys.argv[0])

    entered_arg_loop: bool = False

    for arg in args:
        entered_arg_loop = True
        arg: str = arg.lower()

        if arg == "add_show":
            show_list.add_show()

        elif arg == "remove_show":
            confirmation: bool = show_list.remove_show(CLI.request_show_name())
            CLI.action_confirmation(confirmation, "show removal")

        elif arg == "get_show":
            requested_show_with_index: Show.ShowWithIndex or None = show_list.find_show(CLI.request_show_name())

            if requested_show_with_index is not None:
                CLI.pretty_print_show(requested_show_with_index.show)

            else:
                print("Entered Show does not exist.")

        elif arg == "get_all_shows":
            for show in show_list.shows:
                CLI.pretty_print_show(show)

        elif arg == "increment_show_episode":
            confirmation: bool = show_list.increment_show(CLI.request_show_name())
            CLI.action_confirmation(confirmation, "incrementing episode")

        elif arg == "increment_show_season":
            confirmation: bool = show_list.increment_show_season(CLI.request_show_name())
            CLI.action_confirmation(confirmation, "incrementing season")

        else:
            CLI.help_input()

    if not entered_arg_loop:
        CLI.help_input()

    if not show_list == modify_check_list:
        save_show_list(connection, show_list)

    connection.close()


if __name__ == "__main__":
    main()
