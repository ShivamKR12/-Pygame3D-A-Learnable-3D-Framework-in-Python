import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from core.camera import Camera
from core.entity import Entity
from core.mesh import CubeMesh
from core.shader import Shader

# Init window
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Pygame3D Starter")
clock = pygame.time.Clock()
glEnable(GL_DEPTH_TEST)

# Shader, camera, cube
shader = Shader("shaders/vertex.glsl", "shaders/fragment.glsl")
shader.use()
camera = Camera()
cube = Entity(CubeMesh(), shader)

# Main loop
running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    camera.update()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.draw(camera)
    pygame.display.flip()

pygame.quit()

