import pyglet


#background image
window_height = 358
window_width = 479
window = pyglet.window.Window(window_width, window_height)
pyglet.gl.glClearColor(0,0,1,1)

#boat
boat_image = pyglet.image.load('assets/boat.png')
boat_image.anchor_x = boat_image.width // 2
boat_image.anchor_y = boat_image.height // 2
boat = pyglet.sprite.Sprite(boat_image, x=36, y=30)

@window.event
def on_draw():
    window.clear()
    boat.draw()


pyglet.app.run()