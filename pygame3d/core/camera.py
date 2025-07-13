import numpy as np
import pygame
from OpenGL.GLU import *

class Camera:
    def __init__(self, speed=5.0, sensitivity=0.1):
        self.position = np.array([0, 0, -5], dtype=np.float32)
        self.forward = np.array([0, 0, 1], dtype=np.float32)
        self.up = np.array([0, 1, 0], dtype=np.float32)
        self.right = np.cross(self.forward, self.up)

        self.pitch = 0.0
        self.yaw = -90.0  # Facing down -Z
        self.speed = speed
        self.sensitivity = sensitivity

        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        velocity = self.speed * dt
        if keys[pygame.K_w]:
            self.position += self.forward * velocity
        if keys[pygame.K_s]:
            self.position -= self.forward * velocity
        if keys[pygame.K_a]:
            self.position -= self.right * velocity
        if keys[pygame.K_d]:
            self.position += self.right * velocity

        mx, my = pygame.mouse.get_rel()
        self.yaw += mx * self.sensitivity
        self.pitch -= my * self.sensitivity
        self.pitch = np.clip(self.pitch, -89.0, 89.0)

        self._update_vectors()

        # Projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800 / 600, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        center = self.position + self.forward
        gluLookAt(*self.position, *center, *self.up)

    def _update_vectors(self):
        rad_yaw = np.radians(self.yaw)
        rad_pitch = np.radians(self.pitch)
        x = np.cos(rad_yaw) * np.cos(rad_pitch)
        y = np.sin(rad_pitch)
        z = np.sin(rad_yaw) * np.cos(rad_pitch)
        self.forward = np.array([x, y, z], dtype=np.float32)
        self.forward = self.forward / np.linalg.norm(self.forward)
        self.right = np.cross(self.forward, self.up)
