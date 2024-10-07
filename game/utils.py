# utils.py

import random

# Корабли: 1 корабль - 4 клетки, 2 корабля - 3 клетки, 3 корабля - 2 клетки, 4 корабля - 1 клетка
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

def create_empty_field(size=9):
    return [[0 for _ in range(size)] for _ in range(size)]



def can_place_ship(field, ship_size, row, col, horizontal):
    if horizontal:
        if col + ship_size > len(field):
            return False
        for i in range(ship_size):
            if field[row][col + i] != 0:
                return False
    else:
        if row + ship_size > len(field):
            return False
        for i in range(ship_size):
            if field[row + i][col] != 0:
                return False
    return True

def place_ship(field, ship_size, row, col, horizontal):
    if horizontal:
        for i in range(ship_size):
            field[row][col + i] = 1
    else:
        for i in range(ship_size):
            field[row + i][col] = 1

def generate_field():
    field = create_empty_field()
    for ship_size in ships:
        placed = False
        while not placed:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            horizontal = random.choice([True, False])
            if can_place_ship(field, ship_size, row, col, horizontal):
                place_ship(field, ship_size, row, col, horizontal)
                placed = True
    return field
