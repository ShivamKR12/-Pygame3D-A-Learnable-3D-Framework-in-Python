from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

class Camera:
    def __init__(self):
        self.position = np.array([0, 0, -5], dtype=np.float32)
        self.target = np.array([0, 0, 0], dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)

    def update(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800 / 600, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(*self.position, *self.target, *self.up)

