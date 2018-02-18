from time import asctime, localtime, time

# used to represent a single television show that the amount of episodes watched it being
# tracked.


class Show:
    # show_name : string
    # show_season_number: int
    # episodes_watched : int
    # date_created : string

    def __init__(self, name, season_number, episodes_watched, date_created):
        self.name = name
        self.season_number = season_number
        self.episodes_watched = episodes_watched
        self.date_created = date_created

    def __str__(self):
        return "Name: " + self.name + "\nEpisodes Seen: " + str(self.episodes_watched) + "\nDate Created: " \
               + str(self.date_created) + "\nSeason Number: " + str(self.season_number)


# holds a Show Class, and it's index in the current
# show list.


class ShowWithIndex:
    # show : Show Class
    # index : int

    def __init__(self, show, index):
        self.show = show
        self.index = index


# create new show with possible sane defaults


def create_show(show_name, episodes_watched=0, season_number=1, date_created=asctime(localtime(time()))):
    return Show(show_name, season_number, episodes_watched, date_created)
