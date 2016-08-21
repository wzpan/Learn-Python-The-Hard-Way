#!/usr/bin/env python3

# ex40: Modules, CLasses, and Objects

class Song(object):

    def __init__(self, disk):
        self.index = 0
        self.disk = disk
        self.jump()

    def next(self):
        ''' next song. '''
        self.index = (self.index + 1) % len(self.disk)
        self.jump()

    def prev(self):
        ''' prev song. '''
        self.index = (self.index - 1) % len(self.disk)
        self.jump()
            
    def jump(self):
        ''' jump to the song. '''
        self.lyrics = self.disk[self.index]

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# construct a disk      
song1 =  ["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"]           

song2 = ["They rally around the family",
"With pockets full of shells"
]

song3 = ["Never mind I find",
"Some one like you"
]

disk = [song1, song2, song3]

mycd = Song(disk)
mycd.sing_me_a_song()

mycd.next()
mycd.sing_me_a_song()

mycd.next()
mycd.sing_me_a_song()

mycd.next()
mycd.sing_me_a_song()

mycd.prev()
mycd.sing_me_a_song()

mycd.prev()
mycd.sing_me_a_song()

mycd.prev()
mycd.sing_me_a_song()

mycd.prev()
mycd.sing_me_a_song()