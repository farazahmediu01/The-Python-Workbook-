import sys
import os
 
if sys.version_info[0] < 3:
    import Tkinter as tkinter
else:
    import tkinter
 
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
 
gi.require_version('GstVideo', '1.0')
from gi.repository import GstVideo
 
def set_frame_handle(v_bus, message, frame_id):
    if not message.get_structure() is None:
        if message.get_structure().get_name() == 'prepare-window-handle':
            display_frame = message.src
            display_frame.set_property('force-aspect-ratio', True)
            display_frame.set_window_handle(frame_id)
 
window = tkinter.Tk()
window.title("Video Player")
window.geometry('640x380')
 
Gst.init(None)
GObject.threads_init()
 
display_frame = tkinter.Frame(window, bg='')
display_frame.place(relx = 0, rely = 0,
            anchor = tkinter.NW, relwidth = 1, relheight = 1)
frame_id = display_frame.winfo_id()
 
player = Gst.ElementFactory.make('playbin', None)
player.set_property('uri', 'file:///myfolder/mymovie.mp4') # path here
player.set_state(Gst.State.PLAYING)
 
v_bus = player.get_bus()
v_bus.enable_sync_message_emission()
v_bus.connect('sync-message::element', set_frame_handle, frame_id)
 
window.mainloop()