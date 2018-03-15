import Show


def request_new_show() -> Show.Show:
    """
    Asks user for information to make a new show
    """
    show_name: str = input("Enter the name of the show => ")

    episodes_watched_flag: str = input("Have you already seen some episodes of the show? (y/n) => ")

    if episodes_watched_flag.startswith("y"):
        episodes_watched: int = int(input("Enter how many episodes you have already seen => "))

        season_number_flag: str = input("Does this show have seasons? (y/n) => ")

        if season_number_flag.startswith("y"):
            season_number: int = int(input("Enter the season number you are on => "))
            return Show.create_show(show_name, episodes_watched, season_number)

        else:
            return Show.create_show(show_name, episodes_watched)

    return Show.create_show(show_name)


def help_input():
    """
    Print user help screen
    """
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


def request_show_name() -> str:
    return input("Enter the name of the show => ")


def action_confirmation(confirmation: bool, action_type: str):
    """
    Print whether the user's action was successful or failed
    """
    if confirmation:
        print("Completed " + action_type + " successfully.")
    else:
        print(action_type + " failed.")


def pretty_print_show(show: Show.Show):
    """
    Print out show object nicely (calls __str__ of show)
    """
    print("----------------------------------")
    print(show)
    print("----------------------------------")
