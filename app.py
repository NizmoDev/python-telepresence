from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from local Python server"

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from Python!",
        "client": request.remote_addr
    })

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({
        "received": data,
        "note": "Echo from local app"
    })

if __name__ == "__main__":
    # IMPORTANT: écouter sur 0.0.0.0 pour Telepresence
    app.run(host="0.0.0.0", port=8080, debug=True)
