# from pynput import keyboard
from time import sleep

from map import Map
from helicopter import Helicopter
import time
import os
import keyboard

TICK_SLEEP = 0.25
TREE_UPDATE = 50
FIRE_UPDATE = 50
MAP_H, MAP_W = 15, 15

MOVES = {
    'w' : (-1, 0),
    'd' : (0, 1),
    's' : (1, 0),
    'a' : (0, -1)
}


helicopter = Helicopter(MAP_W, MAP_H)

field = Map(MAP_W, MAP_H)
field.print_map(helicopter)


def call(event):
    if event.event_type != 'up':
        return

    global helicopter
    c = event.name

    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helicopter.move(dx, dy)

keyboard.hook(
    callback=call
)

tick = 1

while True:
    os.system("clear")  # clr
    print("TICK", tick)
    print("Helico", helicopter.x, helicopter.y)
    field.process_helicopter(helicopter)
    helicopter.print_stats()
    field.print_map(helicopter)
    tick += 1
    time.sleep(TICK_SLEEP)

    if tick % TREE_UPDATE == 0:
        field.generate_tree()

    if tick % FIRE_UPDATE == 0:
        field.update_fires()
