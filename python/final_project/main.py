# from pynput import keyboard
from time import sleep

from clouds import Clouds
from map import Map
from helicopter import Helicopter
import time
import os
import keyboard
import json

TICK_SLEEP = 0.25
TREE_UPDATE = 50
FIRE_UPDATE = 50
CLOUDS_UPDATE = 100
MAP_H, MAP_W = 15, 15

MOVES = {
    'w': (-1, 0),
    'd': (0, 1),
    's': (1, 0),
    'a': (0, -1)
}

# f - save, g - load
helicopter = Helicopter(MAP_W, MAP_H)
field = Map(MAP_W, MAP_H)
field.print_map(helicopter)
tick = 1


def call(event):
    if event.event_type != 'up':
        return

    global helicopter, field, tick
    c = event.name

    if c in MOVES.keys():
        dx = MOVES[c][0]
        dy = MOVES[c][1]
        helicopter.move(dx, dy)

    # Сохранение
    elif c == 'f':
        data = {
            "helicopter": helicopter.export_data(),
            "field": field.export_data(),
            "tick": tick
        }
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # Загрузка
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helicopter.import_data(data["helicopter"])
            field.import_data(data["field"])


keyboard.hook(
    callback=call
)

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
        field.update_fires(helicopter)

    if tick % CLOUDS_UPDATE == 0:
        field.clouds.update_clouds()
