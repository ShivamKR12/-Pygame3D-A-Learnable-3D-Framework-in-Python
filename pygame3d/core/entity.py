class Entity:
    def __init__(self, mesh, shader):
        self.mesh = mesh
        self.shader = shader

    def draw(self, camera):
        self.shader.use()
        self.mesh.draw()

