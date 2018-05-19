class Song(object):
# "object" is optional
    def __init__(self,lyrics):
        self.lyrics=lyrics
        # self.lyrics is a variable that lives inside the class
        # while lyrics is an argument from outside

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday=Song(["Happy birthday to you",
                 "I don't want to get sued",
                 "So I'll stop right there"])

bulls_on_parade=["They rally around tha family",
                 "With pockets full of shells"]

happy_bday.sing_me_a_song()

sing=Song(bulls_on_parade)
sing.sing_me_a_song()
