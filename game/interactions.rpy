init python:

    def no_op(denizen):
        pass

    def disappear(denizen):
        map_background.unoccupy(denizen.x, denizen.y)
