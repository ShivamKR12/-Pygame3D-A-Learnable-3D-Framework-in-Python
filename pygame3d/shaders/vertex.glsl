varying vec3 vNormal;
varying vec3 vFragPos;

void main() {
    vNormal = gl_NormalMatrix * gl_Normal;
    vFragPos = vec3(gl_ModelViewMatrix * gl_Vertex);
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
