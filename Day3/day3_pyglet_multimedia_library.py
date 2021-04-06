"""
INSTALLATION:

pip3 install pyglet

KEY FEATURES:
1. No external installation requirements or dependencies.
2. Take benefit of multiple windows and multi-monitor.
3. It can load images, sound, music, and video in any format.
4. Pyglet is provided under the BSD open-source license.
"""

import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label('Day 3 in Gaming World', font_name='Inter', font_size=22,
x = window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()
pyglet.app.run()