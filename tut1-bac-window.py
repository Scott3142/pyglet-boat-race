import pyglet

#background image
window_height = 358
window_width = 479
window = pyglet.window.Window(window_width, window_height)
pyglet.gl.glClearColor(0,0,1,1)

@window.event
def on_draw():
    window.clear()


pyglet.app.run()