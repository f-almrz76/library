from colorama import Fore
from Media import Media

"""This class inherits from Media."""


class Podcast_episode(Media):
    podcast_shelves = []

    def __init__(self, title, speaker, publish_year, time, price, language, status=None, listen_time=0, progress=0):
        Media.__init__(self, title, publish_year, price, language)
        self.speaker = speaker
        self.time = time
        self.status = status
        self.listen_time = listen_time
        self.progress = progress

    def listen(self, time):
        """ This function get time that you listen and calculate how much time remain.
                    it calculates progress too."""
        self.listen_time = time

        if time < self.time:
            print(Fore.WHITE  + f"you have listen {time} more minutes from {self.title}."
                               f"There are {self.time - self.listen_time} minutes left")
        elif time == self.time:
            print(Fore.WHITE  + f' {self.title} is finished.')
        else:
            print(Fore.WHITE + "you can not listen more than Podcast's times")
        """We call function get_status for updating status. and uses it for calculating progress."""
        self.get_status()
        if self.status == "finished":
            self.progress = 100
        else:
            self.progress = (self.listen_time * 100) / self.time

    def get_status(self):
        """ This function checks out status. and returns it """
        if self.listen_time == 0:
            self.status = "unlistened"
        elif self.listen_time >= self.time:
            self.status = "finished"
        else:
            self.status = "listening"
        return self.status

def get_data():
    """This function get information from user and build a object by them."""
    print('\033[35mEnter information.')
    title = input("Enter title :")
    speaker = input("Enter speaker : ")
    publish_year = int(input("Enter publish_year :"))
    time = int(input("Enter time :"))
    language = input("Enter language :")
    price = float(input("Enter price : "))
    podcast = Podcast_episode(title, speaker, publish_year, time, price, language)
    Podcast_episode.podcast_shelves.append(podcast)
    return podcast
