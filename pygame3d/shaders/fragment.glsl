varying vec3 vNormal;
varying vec3 vFragPos;

void main() {
    vec3 lightDir = normalize(vec3(1.0, -1.0, -0.3));
    vec3 norm = normalize(vNormal);
    float diff = max(dot(norm, -lightDir), 0.0);
    vec3 baseColor = vec3(0.6, 0.7, 1.0);
    vec3 final = baseColor * diff + baseColor * 0.2;  // diffuse + ambient
    gl_FragColor = vec4(final, 1.0);
}
