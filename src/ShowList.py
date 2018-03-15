import typing

import Show
from CLI import request_new_show


class ShowList:
    def __init__(self):
        self.shows: typing.List[Show.Show] = []

    def add_show(self):
        """
        Get show object, add to shows list
        """
        new_show: Show.Show = request_new_show()
        self.shows.append(new_show)

    def remove_show(self, show_name: str) -> bool:
        """
        Takes the name of a specific show and removes the show with the corresponding name from the instance's show
        list. Returns True if the show is found, False otherwise
        """
        show_with_index: Show.ShowWithIndex = self.find_show(show_name)

        if show_with_index is not None:
            self.shows.remove(show_with_index.show)
            return True

        return False

    def increment_show(self, show_name: str) -> bool:
        """
        Takes a show name, increments its episodes_watched property and updates the instance's show list. Returns
        True if the show is found, False otherwise
        """
        show_with_index: Show.ShowWithIndex = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.episodes_watched += 1
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    def increment_show_season(self, show_name: str) -> bool:
        """
        Takes a show name, increments its season_number property, resets episodes_watched to 0, and updates the
        instance's show list. Returns True if the show is found, False otherwise
        """
        show_with_index: Show.ShowWithIndex = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.season_number += 1
            show_with_index.show.episodes_watched = 0
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    def set_show_episodes(self, show_name: str, episode_value: int) -> bool:
        """
        Takes a show name and episode value, sets the episodes_watched property and updates the instance's show list.
        Returns True if the show is found, False otherwise
        """
        show_with_index: Show.ShowWithIndex = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.episodes_watched = episode_value
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    def set_show_seasons(self, show_name: str, season_value: int) -> bool:
        """
        Takes a show name and season value, sets the season_number property and updates the instance's show list.
        Returns True if the show is found and False otherwise
        """
        show_with_index: Show.ShowWithIndex = self.find_show(show_name)

        if show_with_index is not None:
            show_with_index.show.season_number = season_value
            self.shows[show_with_index.index] = show_with_index.show
            return True

        return False

    def find_show(self, show_name: str) -> Show.ShowWithIndex:
        """
        Takes a show name and looks through the instance's show list for a matching name, assuming that show names
        are unique.
        """
        temp_show_object: Show.ShowWithIndex = None

        for index, show in enumerate(self.shows):
            if show.name.lower() == show_name.lower():
                temp_show_object = Show.ShowWithIndex(show, index)
                break

        return temp_show_object
