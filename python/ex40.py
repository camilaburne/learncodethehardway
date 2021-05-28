class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print('_'*10)


happy_bday = Song(["Happy bday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

lady_gaga =Song(["Ra Ra o la la", "ga ga olalá"])

happy_bday.sing_me_a_song()
lady_gaga.sing_me_a_song()
