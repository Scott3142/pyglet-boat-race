import pyglet
import math
from pyglet.window import mouse
from pyglet import shapes

batch = pyglet.graphics.Batch()
timer = 60

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

# Coords
Rad2Deg = 180.0 / 3.14159265
Deg2Rad = 3.14159265 / 180.0

speed = 0.25
progress = 0

# Level Design
shapes_arr_game_over = []
obj1 = shapes.Rectangle(0, 0, 10, window_height, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj1)
obj2 = shapes.Rectangle(0, window_height - 10, window_width, 10, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj2)
obj3 = shapes.Rectangle(80, 0, window_width, 10, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj3)
obj4 = shapes.Rectangle(80, 0, 10, window_height - 90, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj4)
obj5 = shapes.Rectangle(160, 90, 10, window_height - 90, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj5)
obj6 = shapes.Rectangle(240, 0, 10, window_height - 90, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj6)
obj7 = shapes.Rectangle(320, 90, 10, window_height - 90, color=(65, 42, 42), batch=batch)
shapes_arr_game_over.append(obj7)
#evil_block = shapes.Rectangle(50, 90, 10, 50, color=(65, 42, 42), batch=batch)
#shapes_arr_game_over.append(evil_block)
spinning_block_of_doom = evil_block = shapes.Rectangle(400, 90, 10, 50, color=(65, 42, 42), batch=batch)
spinning_block_of_doom.anchor_x = spinning_block_of_doom.width // 2
spinning_block_of_doom.anchor_y = spinning_block_of_doom.height // 2

shapes_game_success = []
circle = shapes.Circle(window_width, window_height, 100, color=(50, 225, 30), batch=batch)

# Win Game Over message

label = pyglet.text.Label('Gamer Over',
                          font_name='Times New Roman',
                          font_size=36,
                          x=900, y=900,
                          anchor_x='center', anchor_y='center')

# Mouse Handler
mouse_handler = pyglet.window.mouse.MouseStateHandler()

# Speed Variables
y_speed = 0.5
x_speed = 1
end_game = 0

def collide(a, b, offset):
    if (a.y - offset) + a.height < b.y:
        return False
    if (a.y - offset) > (b.y - offset) + b.height:
        return False
    if (a.x - offset) + a.width < b.x:
        return False
    if (a.x - offset) > b.x + b.width:
        return False

    return True


def update(dt):
    spinning_block_of_doom.rotation += 2
    end_game = 0



    for x in shapes_arr_game_over:
        if collide(boat, x, 20):
            label.text = "Game Over"
            label.x = window.width // 2
            label.y = window.height // 2
            end_game = 1

    if collide(boat, x, 120):
        label.text = "Winner"
        label.x = window.width // 2
        label.y = window.height // 2
        end_game = 1

    if end_game == 0:
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
    else:
        boat.rotation = 90
        if boat.scale >= 2:
            boat.scale = 1
        else:
            boat.scale +=0.01


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
    batch.draw()
    boat.draw()
    label.draw()


pyglet.clock.schedule_interval(update, 1 / 220)
pyglet.app.run()
