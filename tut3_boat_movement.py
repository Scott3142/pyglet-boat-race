import pyglet
import math
from pyglet.window import mouse


# background image
window_height = 358
window_width = 479
window = pyglet.window.Window(window_width, window_height)
pyglet.gl.glClearColor(0, 0, 1, 1)

# boat
boat_image = pyglet.image.load('assets/boat.png')
boat_image.anchor_x = boat_image.width // 2
boat_image.anchor_y = boat_image.height // 2
boat = pyglet.sprite.Sprite(boat_image, x=36, y=30)

#Coords
Rad2Deg = 180.0 / 3.14159265
Deg2Rad = 3.14159265 / 180.0

#Mouse Handler
mouse_handler = pyglet.window.mouse.MouseStateHandler()

#Speed Variables
y_speed = 0.1
x_speed = 5

def update(dt):
    if window._mouse_in_window:
        x_cord = (boat.rotation / 85) / x_speed
        atan = (window_height - boat.x)
        if is_between(-90, boat.rotation, 90):
            boat.update(y=boat.y + (y_speed), x=boat.x + x_cord)
        else:
            try:
                window._mouse_y
            except AttributeError:
                print("well, it WASN'T defined after all!")
            else:
                if float(window._mouse_y) != float(boat.y):
                    boat.update(y=boat.y - (y_speed));

def is_between(a, x, b):
    return min(a, b) < x < max(a, b)

@window.event
def on_mouse_motion(x, y, dx, dy):
    if window._mouse_in_window:
        # Here be dragons. Thou art forewarned
        atan = math.atan2((x - boat.x), (y - boat.y))
        rotation = atan * Rad2Deg
        boat.update(rotation=rotation)


@window.event
def on_draw():
    window.clear()
    boat.draw()


pyglet.clock.schedule_interval(update, 1 / 220)
pyglet.app.run()
