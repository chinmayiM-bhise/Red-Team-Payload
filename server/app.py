import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify
from client_manager import register_client, get_clients
from command_handler import execute_command
from utils.logger import log_event

app = Flask(__name__)


@app.route("/")
def home():
    return "Red Team Simulation Server Running"


@app.route("/register", methods=["POST"])
def register():

    data = request.json

    hostname = data.get("hostname")
    ip = data.get("ip")

    client = register_client(hostname, ip)

    log_event(f"Client registered: {hostname} ({ip})")

    return jsonify(client)


@app.route("/clients")
def clients():

    return jsonify(get_clients())


@app.route("/command", methods=["POST"])
def command():

    data = request.json
    cmd = data.get("command")

    result = execute_command(cmd)

    log_event(f"Command executed: {cmd}")

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(port=5000, debug=True)