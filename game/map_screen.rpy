#4,3
#offset from center_x = 80 * 4 + 80 / 2 = 360 px
#x of center of the screen = 1280 / 2 = 640 px
# xpos = 640 - 360 = 280 px

#offset from center_y = 80 * 3 + 80 / 2 = 280 px
#y of center of the screen = 720 / 2 = 360 px
# ypos = 360 - 280 = 80 px

screen map_screen(aMap):

    add "backbackground1"

    $offset_x = 640 - (80 * aMap.center_x) + 40
    $offset_y = 280 - (80 * aMap.center_y) + 40
    add aMap.img:
        pos(offset_x, offset_y)

    for i in range(len(aMap.map)):
        $row = aMap.map[i]
        for j in range(len(row)):
            $tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $offx, offy = tile.occupant.getOffset()
                $tile_lc_x = 80 * j + offset_x
                $tile_lc_y = 80 * i + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)

    key "K_UP" action [Function(map_background.moveDenizen, character_sprite.x, character_sprite.y, 0, -1), SetVariable("c_dir", "back")]
    key "K_DOWN" action [Function(map_background.moveDenizen, character_sprite.x, character_sprite.y, 0, 1), SetVariable("c_dir", "front")]
    key "K_RIGHT" action [Function(map_background.moveDenizen, character_sprite.x, character_sprite.y, 1, 0), SetVariable("c_dir", "right")]
    key "K_LEFT" action [Function(map_background.moveDenizen, character_sprite.x, character_sprite.y, -1, 0), SetVariable("c_dir", "left")]
