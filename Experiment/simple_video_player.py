'''
This is the code of media player from book'Python Multimedia Beginner guide 2010'.
'''

import os
import gst
import time
import thread
import gobject
import pygst
pygst.require("0.10")


class VideoPlayer:

    def __init__(self):
        pass


    def constructPipeline(self):
        pass


    def connectSignals(self):
        pass


    def decodebin_pad_added(self, decodebin, pad):
        pass


    def play(self):
        pass


    def message_handler(self, bus, message):
        pass

# Run the program
player = VideoPlayer()
thread.start_new_thread(player.play, ())
gobject.threads_init()
evt_loop = gobject.MainLoop()
evt_loop.run()

