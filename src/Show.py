from time import asctime, localtime, time


class Show:
    """
    Used to represent a single television show and track the number of episodes watched
    """

    def __init__(self, name: str, season_number: int, episodes_watched: int, date_created: str):
        self.name = name
        self.season_number = season_number
        self.episodes_watched = episodes_watched
        self.date_created = date_created

    def __str__(self) -> str:
        return "Name: " + self.name + "\nEpisodes Seen: " + str(self.episodes_watched) + "\nDate Created: " \
               + str(self.date_created) + "\nSeason Number: " + str(self.season_number)


class ShowWithIndex:
    """
    Holds a Show class and its index in the current show list
    """

    def __init__(self, show: Show, index: int):
        self.show = show
        self.index = index


# create new show with possible sane defaults


def create_show(show_name: str, episodes_watched: int = 0, season_number: int = 1,
                date_created: str = asctime(localtime(time()))) -> Show:
    return Show(show_name, season_number, episodes_watched, date_created)
