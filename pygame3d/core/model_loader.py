import pywavefront

def load_obj(path):
    scene = pywavefront.Wavefront(path, collect_faces=True)
    vertices = []
    indices = []
    offset = 0

    for name, mesh in scene.meshes.items():
        for face in mesh.faces:
            indices.extend([i + offset for i in face])
        for vertex in mesh.vertices:
            vertices.extend(vertex)
        offset = len(vertices) // 3

    return vertices, indices
