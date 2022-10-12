#   This software is completely free and open-source under the terms of the
#   GNU General Public License as published by the Free Software Foundation,
#   either version 3 of the license, or any later version.

# region Modules

import bge
import mathutils
from collections import OrderedDict

# endregion


class PlayerMovement(bge.types.KX_PythonComponent):
    args = OrderedDict([("Movement Speed", 0.025), ("Turning Speed", 0.025)])

    # region BGE functions

    # start() is called when the script is first loaded.
    def start(self, args):
        self.movementSpeed = args["Movement Speed"]
        self.turn_speed = args["Turning Speed"]

    #  update() is called once per frame.
    def update(self):
        keyboard = bge.logic.keyboard
        inputs = keyboard.inputs

        horizontal = 0.0
        vertical = 0.0

        # Horizontal
        if inputs[bge.events.SKEY].values[-1]:
            vertical += self.movementSpeed * float(bge.logic.getRealTime())
        if inputs[bge.events.WKEY].values[-1]:
            vertical -= self.movementSpeed * float(bge.logic.getRealTime())
        # Vertical
        if inputs[bge.events.AKEY].values[-1]:
            horizontal += self.movementSpeed * float(bge.logic.getRealTime())
        if inputs[bge.events.DKEY].values[-1]:
            horizontal -= self.movementSpeed * float(bge.logic.getRealTime())

        direction = mathutils.Vector((horizontal, vertical, 0.0)).normalized()
        self.object.applyMovement((direction.x / 10, direction.y / 10, 0), True)

    # endregion
