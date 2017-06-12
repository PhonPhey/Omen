""" Module for init base layer interface"""

import urwid

def init(location_name):
    """Main function of tui.base module """

    palette = [
        ('banner', 'black', 'light gray'),
        ('top', 'black', 'dark green'),
        ('bg', 'black', 'dark blue'),]

    text = urwid.Text(('banner', location_name), align = 'left')
    location_name_layer =urwid.AttrMap(text, 'banner')
    bg_layer = urwid.AttrMap(urwid.Filler(location_name_layer, 'top'), 'bg')
    main_layer = urwid.MainLoop(bg_layer, palette)
    main_layer.run()