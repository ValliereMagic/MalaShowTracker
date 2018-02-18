from Show import create_show

# asks user for information to make a new show
# returns a new Show class


def request_new_show():
    # show_name : string
    # optional: episodes_watched : int
    # episodes_watched_flag : string
    # optional: season_number : int
    # season_number_flag : string

    show_name = input("Enter the name of the show => ")

    episodes_watched_flag = input("Have you already seen some episodes of the show? (y/n) => ")

    if episodes_watched_flag.startswith("y"):
        episodes_watched = input("Enter how many episodes you have already seen => ")

        season_number_flag = input("Does this show have seasons? (y/n) => ")

        if season_number_flag.startswith("y"):
            season_number = input("Enter the season number you are on => ")
            return create_show(show_name, int(episodes_watched), int(season_number))

        else:
            return create_show(show_name, int(episodes_watched))

    return create_show(show_name)


def request_show_name():
    return input("Enter the name of the show => ")
