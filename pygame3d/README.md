# 🎮 Pygame3D

A minimal, modular, and beginner-friendly 3D framework built using **Pygame + PyOpenGL**.

### ✨ Features
- 3D rendering with OpenGL
- Simple shader system
- Entity/mesh abstraction
- Camera control via GLU
- Clean structure for learning & hacking

---

## 🚀 Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/yourname/pygame3d.git
cd pygame3d
````

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the project:

```bash
python main.py
```

---

## 📁 Project Structure

| File       | Purpose                                     |
| ---------- | ------------------------------------------- |
| `main.py`  | Starts the app, game loop                   |
| `core/`    | Engine logic (camera, shader, entity, mesh) |
| `shaders/` | GLSL shaders                                |
| `assets/`  | Models, textures, future data               |

---

## 💡 Philosophy

> **Simple first, features later.**

* Not a full engine — it’s a learning tool
* Clean enough for beginners
* Hackable enough for pros

---

## 📦 License

MIT — free to use, share, and modify.



---

# ✅ 📅 Pygame3D Development Roadmap

---

## ✅ Phase 1: Core Engine (DONE or In Progress)

| Feature                 | Status       |
| ----------------------- | ------------ |
| Pygame + OpenGL window  | ✅ Done       |
| Basic cube mesh         | ✅ Done       |
| Shader pipeline         | ✅ Done       |
| Camera + movement       | ✅ Done       |
| Lighting (directional)  | ✅ Basic done |
| Model loading (.obj)    | ✅ Ready      |
| VAO/VBO for performance | ✅ Done       |

---

## 🧩 Phase 2: Intermediate Systems (Next Steps)

### 🎮 Player + World

* ☐ Add a player controller entity (jumping, gravity)
* ☐ Basic terrain or grid system
* ☐ Scene saving/loading via JSON or YAML

### 💡 Lighting Upgrades

* ☐ Add **point lights** (position + falloff)
* ☐ Light uniforms in GLSL (use `glUniform3f`)
* ☐ Toggle ambient/diffuse/specular toggles

### 🎨 Materials System

* ☐ Add material class (diffuse, specular, shininess)
* ☐ Per-object uniforms for material properties
* ☐ Texture support (`Texture2D`, UV mapping)

### 🧱 Entity & Scene System

* ☐ Scene graph hierarchy (parents, transforms)
* ☐ Tags or names for entities
* ☐ ECS-lite: simple component-based design

---

## 🔨 Phase 3: Tooling & Polish

### 🧪 Developer Features

* ☐ On-screen FPS + stats
* ☐ Debug render (wireframe, normals)
* ☐ Bounding boxes or selection helpers

### 🧰 Tooling

* ☐ Scene loader/editor (even CLI-based)
* ☐ Script manager (attach behaviors to objects)
* ☐ Config system (JSON or `.ini`)

### 🔊 Audio System

* ☐ Background music and 3D positional sound
* ☐ SFX manager using `pygame.mixer`

---

## 📦 Phase 4: Deployment

### 📱 Desktop Builds

* ☐ PyInstaller `.exe` export script
* ☐ Asset bundling system

### 📱 Android/Mobile (Experimental)

* ☐ Attempt `pygame-ce + python-for-android` + SDL2
* ☐ Touch input layer
* ☐ Mobile camera + virtual joystick

---

## 💻 Optional: Advanced Features (Stretch Goals)

* ☐ Shadows via depth maps
* ☐ Post-processing (bloom, fog)
* ☐ Physics via PyBullet or Pymunk
* ☐ First-person shooter kit
* ☐ Simple UI system (menus, HUD)

---

## 🧠 Final Vision

You're building **a real 3D framework for learning and prototyping** — a stepping stone between raw OpenGL and big engines like Unity. Think:

* 🔓 Fully inspectable
* 💡 Educational by design
* 🛠️ Hackable/modular

