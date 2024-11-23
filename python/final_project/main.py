# from pynput import keyboard
from map import Map
from helicopter import Helicopter
import time
import os
import keyboard

TICK_SLEEP = 0.10
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_H, MAP_W = 15, 15

helicopter = Helicopter(MAP_W, MAP_H)

field = Map(MAP_W, MAP_H)
field.generate_forest(2, 10)
field.generate_river(10)
field.generate_river(15)
field.print_map(helicopter)


def call(event):
    if event.event_type != 'up':
        return

    print(event.name)


keyboard.hook(
    callback=call
)

tick = 1

while True:
    os.system("clear")  # clr
    print("TICK", tick)
    field.print_map(helicopter)
    tick += 1
    time.sleep(TICK_SLEEP)

    if tick % TREE_UPDATE == 0:
        field.generate_tree()

    if tick % FIRE_UPDATE == 0:
        field.update_fires()
