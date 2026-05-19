class Playlist:
    # магические методы, dunder(double underscore)
    def __init__(self, name, songs=None):
        self.name = name
        self.__songs = songs

    def __str__(self):
        return f"<Playlist name='{self.name}'>"

    def __len__(self):
        return len(self.__songs)

    def __contains__(self, item):
        return item in self.__songs

    def __bool__(self):
        return bool(self.__songs)

