'''Uses all functionality provided by the classes in the interface module.
Draws a bouncing cube in perspective, desktop or vr; using a shader pipeline.
'''

from __future__ import (print_function, division, absolute_import)

from gl import *
from glm import mat4x4, vec3
from math import sin

from interface import Interface
from primitivelib import Cube
from renderer import Program, RenderHandle, create_shader, draw_handles
from universe import Agent


class HappyCube(Cube):
    def __init__(self):
        super(HappyCube, self).__init__()
        self.rot_vel = 0.5  # Half turn per second
        self.rotation = ((1,0.7,0.3), 0.0)
        self.translation = (0, 0, -10)
        self.cumtime = 0

    def tick(self, dt):
        self.cumtime += dt
        self.rotation = (self.rotation[0], self.rotation[1] + self.rot_vel*2*3.14*dt)
        self.translation = (
                self.translation[0],
                -5 + 7 * abs(sin(3 * self.cumtime)),
                self.translation[2],
                )


class MyUniverse(Agent):
    """This universe is redundant. Written to show how things should work."""
    def __init__(self):
        self.cube = HappyCube()

    def get_render_handles(self):
        # get_render_handles is implemented for all primitives in primitivelib
        return self.cube.get_render_handles()

    def tick(self, dt):
        self.cube.tick(dt)


################################################################################


def new(interface_class):
    """This is how we define a new game.
    interface_class can be a Desktop interface or a
    Rift interface, but we don't care. We just want to inherit from it.
    In this case, we do the only essential thing: Specifying a universe.
    """
    class SimpleGame(interface_class):
        def begin(self):
            super(SimpleGame, self).begin()
            self.universe = MyUniverse()
    return SimpleGame

