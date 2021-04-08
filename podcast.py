from Media import Media


class Podcast_episode(Media):

    def __init__(self, title, speaker, publish_year, time, price, language, status=None, listen_time=None, progress=0):
        Media.__init__(self, title, publish_year, price, language)
        self.speaker = speaker
        self.time = time
        self.status = status
        self.listen_time = listen_time
        self.progress = progress


    def listen(self, time):
        self.listen_time = time
        self.progress = (self.listen_time * 100) / self.time
        if time < self.time:
            print('\033[29m' + f"you have listen {time} more minutes from {self.title}."
                               f"There are {self.time - self.listen_time} minutes left")
        elif time == self.time:
            print('\033[29m' + f' {self.title} is finished.')
        else:
            print('\033[29m' + "you can not listen more than Podcast's times")
        self.get_status()

    def get_status(self):
        """ this function is status rach time ."""
        if self.listen_time == 0:
            self.status = "unlistened"
        elif self.listen_time == self.time:
            self.status = "finished"
        else:
            self.status = "listening"
        return self.status

    def get_data(number_podcast):
        """ this function get data from the user """
        for i in range(number_podcast):
            print('\033[35mEnter information.')
            title = input("Enter title :")
            speaker = input("Enter speaker : ")
            publish_year = int(input("Enter publish_year :"))
            time = int(input("Enter time :"))
            language = input("Enter language :")
            price = float(input("Enter price : "))
            podcast = Podcast_episode(title, speaker, publish_year, time, price, language)
            return podcast