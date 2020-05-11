from collections import namedtuple
import datetime
import queue

Coord = namedtuple('Coord', ['x', 'y'])

L = Coord(-1, 0)
U = Coord(0, -1)
R = Coord(1, 0)
D = Coord(0, 1)

compass = {'L': L, 'U': U,'R': R,'D': D}

direction = {'L': '←', 'U': '↑','R': '→','D': '↓'}

def add(a, b):
    return Coord(a.x + b.x, a.y + b.y)

class Grid:
    def __init__(self, width, height):
        self.cells = []
        self.width = width
        self.height = height
        self.cells = [[' ' for x in range(width)] for y in range(height)]
  
    def add_cell(self, x, y, cell):
        self.cells[y][x] = cell

    def get_cell(self, x, y):
        if self.width > x >= 0 and self.height > y >= 0:
            return self.cells[y][x]
        return None

    def BFS_target(self, start, targets):
        q = queue.Queue()
        q.put('')
        while True:
            x = q.get()
            visited = {start}
            for i in list(compass):
                insert = x + i
                print(f'Insert is: {insert}')
                new_pos = start
                for move in insert:
                    new_pos = add(new_pos, compass[move])
                print(f'Analyzing pos ({new_pos.x},{new_pos.y}):')
                if self.get_cell(new_pos.x, new_pos.y) == '#':
                    print('-invalid')
                    continue
                if new_pos in visited:
                    print("-hey, i've been here before...")
                    continue
                elif new_pos in targets:
                    print('\n-match!')
                    new_pos = start
                    k = 0
                    for move in insert:
                        new_pos = add(new_pos, compass[move])
                        k += 1
                        if k < len(insert):
                            game_map.add_cell(new_pos.x, new_pos.y, direction[insert[k]])
                    return new_pos
                else:
                    print('-nothing here, moving on')
                    visited.add(new_pos)
                    q.put(insert)

def print_map():
	for i in range(len(game_map.cells)):
		out = ''
		for j in game_map.cells[i]:
			each = f'[{j}]'
			out = out + '    ' + each
		print(f'{out}')
		print('\n')

game_map = Grid(9, 9)

pellets = [Coord(2, 4), Coord(6, 2)]
foe_pacs = [Coord(1, 7)]
walls = [Coord(3, 3), Coord(4, 3), Coord(5, 3), Coord(3, 4), Coord(3, 5), Coord(4, 5), Coord(5, 5)]

game_map.add_cell(4, 4, '○')

for i in walls:
	x, y = i.x, i.y
	game_map.add_cell(x, y, '#')

for i in pellets:
	x, y = i.x, i.y
	game_map.add_cell(x, y, '∙')

for i in foe_pacs:
	x, y = i.x, i.y
	game_map.add_cell(x, y, '×')

print_map()
init = datetime.datetime.now()
print(game_map.BFS_target(Coord(4, 4), foe_pacs))
elapsed = datetime.datetime.now() - init
print('\n')
print_map()
print(f'elapsed time: {elapsed.microseconds / 1000}ms')
