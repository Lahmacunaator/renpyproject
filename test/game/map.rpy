#Specificaton
#Grid/Tile Based
#Character Stays Centered, Map Moves
#Enter Keypress next to and facing item interacts
#items are obstacles

#1280 / 80 = 16
#720 / 80 = 9

define tile_size = 80

#19 tiles wide x 12 tiles tall background map

init python:

    class GameMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen

        def unoccupy(self, x, y):
            self.map[y][x].occupant = None

        def moveDenizen(self, x, y, offx, offy):
            if self.isEmpty(x,y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return
            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y + offy][x + offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy
            if self.center_x == x and self.center_y == y:
                self.center_x += offx
                self.center_y += offy

    class MapTile:
        def __init__(self, occupant=None):
            self.occupant = occupant

    class MapOccupant:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def interact(self):
            pass

    class MapDenizen(MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x,y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            self.interaction(self)

    desert_map = []

    for i in range(12):
        new_row = []
        for j in range(19):
            new_row.append(MapTile())
        desert_map.append(new_row)

    map_background = GameMap(desert_map, "background1.png", 2, 8)
    character_sprite = MapDenizen(2, 8, "character", 80, 128, no_op)
    map_background.occupy(2, 8, character_sprite)
    object_sprite = MapDenizen(0, 2, "object_9.png", 256, 256, disappear)

    #walls and obstacles in the map
    o1 = MapOccupant(0, 1)
    map_background.occupy(0, 1, o1)
    o2 = MapOccupant(0, 4)
    map_background.occupy(0, 4, o2)
    o3 = MapOccupant(0, 5)
    map_background.occupy(0, 5, o3)
    o4 = MapOccupant(1, 5)
    map_background.occupy(1, 5, o4)
    o5 = MapOccupant(1, 6)
    map_background.occupy(1, 6, o5)
    o6 = MapOccupant(2, 5)
    map_background.occupy(2, 5, o6)
    o7 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o7)
    o8 = MapOccupant(3, 5)
    map_background.occupy(3, 5, o8)
    o9 = MapOccupant(3, 6)
    map_background.occupy(3, 6, o9)
    o10 = MapOccupant(4, 5)
    map_background.occupy(4, 5, o10)
    o11 = MapOccupant(4, 6)
    map_background.occupy(4, 6, o11)
    o12 = MapOccupant(5, 5)
    map_background.occupy(5, 5, o12)
    o13 = MapOccupant(5, 6)
    map_background.occupy(5, 6, o13)
    o14 = MapOccupant(6, 5)
    map_background.occupy(6, 5, o14)
    o15 = MapOccupant(6, 6)
    map_background.occupy(6, 6, o15)
    o16 = MapOccupant(7, 5)
    map_background.occupy(7, 5, o16)
    o17 = MapOccupant(7, 6)
    map_background.occupy(7, 6, o17)
    o18 = MapOccupant(8, 5)
    map_background.occupy(8, 5, o18)
    o19 = MapOccupant(8, 6)
    map_background.occupy(8, 6, o19)
    o20 = MapOccupant(8, 7)
    map_background.occupy(8, 7, o20)
    o21 = MapOccupant(9, 5)
    map_background.occupy(9, 5, o21)
    o22 = MapOccupant(9, 6)
    map_background.occupy(9, 6, o22)
    o23 = MapOccupant(9, 7)
    map_background.occupy(9, 7, o23)
    o24 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o24)
    o25 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o25)
    o26 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o26)
    o27 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o27)
    o28 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o28)
    o29 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o29)
    o30 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o30)
    o31 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o31)
    o32 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o32)
    o33 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o33)
    o34 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o34)
    o35 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o35)
    o36 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o36)
    o37 = MapOccupant(2, 6)
    map_background.occupy(2, 6, o37)