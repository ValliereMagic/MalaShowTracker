from CLI import request_new_show
from Show import ShowWithIndex


class ShowList:
    def __init__(self):
        # shows : Show Objects
        self.shows = []

    # Get show object, add to shows list

    def add_show(self):
        new_show = request_new_show()
        self.shows.append(new_show)

    # takes a list of show objects, and the name of a specific show, then removes the show
    # with the corresponding name if it is found.
    # If a show with that name is not found, then the method returns None.

    def remove_show(self, show_name):
        show_with_index = self.find_show(show_name)

        if show_with_index is not None:
            self.shows.remove(show_with_index.show)
            return True

        return False

    # takes the show list of Show objects and a show name, and increments the episodes_watched
    # property of the object by one, and then, returns the updated list.

    def increment_show(self, show_name):
        show_with_index = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.episodes_watched += 1
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    # get show by name, increment season number, and set
    # episodes_watched to 0.

    def increment_show_season(self, show_name):
        show_with_index = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.season_number += 1
            show_with_index.show.episodes_watched = 0
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    # set the value of the current episode count

    def set_show_episodes(self, show_name, episode_value):
        show_with_index = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.episodes_watched = episode_value
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    # set the value of the current season number (int)

    def set_show_seasons(self, show_name, season_value):
        show_with_index = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.season_number = season_value
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    # takes a list of Show objects and the (string) name of a show, and looks through the list passed
    # to find the object with the show name. Assuming that show names are unique.

    def find_show(self, show_name):
        temp_show_object = None

        for index, show in enumerate(self.shows):
            if show.name.lower() == show_name.lower():
                temp_show_object = ShowWithIndex(show, index)
                break

        return temp_show_object
