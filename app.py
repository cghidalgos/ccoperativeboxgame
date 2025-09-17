from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# --- Variables globales ---
users = {}
obj = {"x": 250, "y": 250}
target = {"x": random.randint(50, 450), "y": random.randint(50, 450)}

# --- Rutas ---
@app.route("/")
def index():
    return render_template("index.html")  # pantalla inicial para elegir nombre

@app.route("/game")
def game():
    username = request.args.get("username")
    if not username:
        return redirect(url_for("index"))
    return render_template("game.html", username=username)

@app.route("/list")
def user_list():
    username = request.args.get("username")
    return render_template("list.html", username=username, users=users)

@app.route("/reset")
def reset():
    global obj, target
    obj = {"x": 250, "y": 250}
    target["x"] = random.randint(50, 450)
    target["y"] = random.randint(50, 450)
    socketio.emit("update", {"users": users, "object": obj, "target": target})
    return "ok"

# --- Eventos de Socket.IO ---
@socketio.on("join")
def on_join(data):
    username = data["username"]
    users[request.sid] = {
        "username": username,
        "x": random.randint(50, 450),
        "y": random.randint(50, 450),
        "color": f"#{random.randint(0, 0xFFFFFF):06x}"
    }
    emit("init", {"users": users, "object": obj, "target": target}, to=request.sid)
    socketio.emit("update", {"users": users, "object": obj, "target": target})

@socketio.on("move")
def on_move(data):
    if request.sid in users:
        users[request.sid]["x"] = data["x"]
        users[request.sid]["y"] = data["y"]

        # Verificar victoria (si el objeto está cerca del objetivo)
        if abs(obj["x"] - target["x"]) < 20 and abs(obj["y"] - target["y"]) < 20:
            socketio.emit("victory", {"message": f"{users[request.sid]['username']} ganó 🎉"})

        socketio.emit("update", {"users": users, "object": obj, "target": target})

@socketio.on("disconnect")
def on_disconnect():
    if request.sid in users:
        del users[request.sid]
    socketio.emit("update", {"users": users, "object": obj, "target": target})

# --- Ejecutar ---
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
