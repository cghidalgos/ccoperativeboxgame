from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
import math

app = Flask(__name__)
socketio = SocketIO(app)

users = {}
waiting_room = {}
object_pos = {"x": 300, "y": 300}  # Punto negro inicial
target_pos = {"x": random.randint(100, 500), "y": random.randint(100, 500)}  # Punto naranja inicial

colors = ["red", "blue", "green", "purple", "brown", "pink", "teal", "gold"]
color_index = 0

DISTANCIA_FIJA = 100  # En píxeles

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list_page():
    username = request.args.get("username")
    return render_template("list.html", username=username)

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/reset")
def reset():
    global object_pos, target_pos
    object_pos = {"x": 300, "y": 300}
    target_pos = {"x": random.randint(100, 500), "y": random.randint(100, 500)}
    socketio.emit("update", {"users": users, "object": object_pos, "target": target_pos})
    return ("", 204)

@socketio.on("join")
def handle_join(data):
    global color_index
    uid = request.sid
    x, y = random.randint(50, 550), random.randint(50, 550)
    users[uid] = {
        "username": data["username"],
        "x": x,
        "y": y,
        "color": colors[color_index % len(colors)]
    }
    color_index += 1
    emit("init", {"users": users, "object": object_pos, "target": target_pos}, room=uid)
    emit("update", {"users": users, "object": object_pos, "target": target_pos}, broadcast=True)

@socketio.on("move")
def handle_move(data):
    uid = request.sid
    if uid not in users: return
    new_x = data["x"]
    new_y = data["y"]
    
    dx = new_x - object_pos["x"]
    dy = new_y - object_pos["y"]
    distancia_actual = math.hypot(dx, dy)

    if distancia_actual != DISTANCIA_FIJA:
        factor_ajuste = DISTANCIA_FIJA / distancia_actual
        new_x = object_pos["x"] + dx * factor_ajuste
        new_y = object_pos["y"] + dy * factor_ajuste

    users[uid]["x"] = new_x
    users[uid]["y"] = new_y

    avg_x = sum(user["x"] for user in users.values()) / len(users)
    avg_y = sum(user["y"] for user in users.values()) / len(users)
    object_pos["x"] = avg_x
    object_pos["y"] = avg_y

    socketio.emit("update", {"users": users, "object": object_pos, "target": target_pos})

    if math.hypot(object_pos["x"] - target_pos["x"], object_pos["y"] - target_pos["y"]) < 20:
        socketio.emit("victory", {"message": "¡Victoria! El punto negro ha llegado al punto naranja."})

@socketio.on("disconnect")
def handle_disconnect():
    uid = request.sid
    if uid in users:
        del users[uid]
        socketio.emit("update", {"users": users, "object": object_pos, "target": target_pos})
    if uid in waiting_room:
        del waiting_room[uid]
        socketio.emit("waiting_update", waiting_room)

@socketio.on("chat_message")
def handle_chat_message(data):
    message = data["message"]
    username = users[request.sid]["username"]
    emit("chat_message", {"username": username, "message": message}, broadcast=True)

@socketio.on("waiting_join")
def waiting_join(data):
    uid = request.sid
    waiting_room[uid] = {
        "username": data["username"],
        "ready": False
    }
    emit("waiting_update", waiting_room, broadcast=True)

@socketio.on("set_ready")
def set_ready(data):
    uid = request.sid
    if uid in waiting_room:
        waiting_room[uid]["ready"] = data["ready"]
        emit("waiting_update", waiting_room, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5004)
