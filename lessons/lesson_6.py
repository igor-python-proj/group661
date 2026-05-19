from lessons.playlist import Playlist
from lessons.lesson_3 import Car

car_1 = Car("black")
print(car_1)
playlist_pop = Playlist(
    name="Pop",
    songs=["Shape of my heart"]
)
print(playlist_pop)
print(len(playlist_pop))
print("Go" in playlist_pop)
print("Shape of my heart" in playlist_pop)
if playlist_pop:
    print("Плейлист не пустой")
else:
    print("Плейлист пустой")
