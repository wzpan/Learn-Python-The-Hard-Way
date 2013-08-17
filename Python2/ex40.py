#!/bin/python2
# -*- coding: utf-8 -*-

# ex40: Modules, Classes, and Objects

# a first class example

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

song1 =  ["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"]           

song2 = ["They rally around the family",
"With pockets full of shells"
]

song3 = ["Never mind I find",
"Some one like you"
]
                
happy_bday = Song(song1)
bulls_on_parade = Song(song2)
someone_like_you = Song(song3)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

someone_like_you.sing_me_a_song()
