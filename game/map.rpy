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
    wall = MapOccupant(8, 10)
    map_background.occupy(8, 10, wall)
    object_sprite = MapDenizen(0, 2, "object_9.png", 256, 256, disappear)
