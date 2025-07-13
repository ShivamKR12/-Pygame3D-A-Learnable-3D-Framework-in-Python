from OpenGL.GL import *

class CubeMesh:
    def __init__(self):
        self.vertices = [
            -1, -1, -1,  1, 0, 0,
             1, -1, -1,  0, 1, 0,
             1,  1, -1,  0, 0, 1,
            -1,  1, -1,  1, 1, 0,
            -1, -1,  1,  0, 1, 1,
             1, -1,  1,  1, 0, 1,
             1,  1,  1,  1, 1, 1,
            -1,  1,  1,  0, 0, 0,
        ]
        self.indices = [
            0, 1, 2, 2, 3, 0,
            1, 5, 6, 6, 2, 1,
            5, 4, 7, 7, 6, 5,
            4, 0, 3, 3, 7, 4,
            3, 2, 6, 6, 7, 3,
            4, 5, 1, 1, 0, 4
        ]
        self.vertices = (GLfloat * len(self.vertices))(*self.vertices)
        self.indices = (GLuint * len(self.indices))(*self.indices)

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 6 * 4, self.vertices)
        glColorPointer(3, GL_FLOAT, 6 * 4, self.vertices[3:])
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, self.indices)
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

