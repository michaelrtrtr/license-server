from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "KEY123": False,
    "KEY456": False,
    "KEY789": False
}

@app.route("/activate", methods=["POST"])
def activate():
    data = request.json
    print("Received:", data)   # 👈 debug

    key = data.get("key")

    print("Key status:", licenses.get(key))

    if key in licenses and licenses[key] is False:
        licenses[key] = True
        return jsonify({"valid": True})

    return jsonify({"valid": False})

app.run(host="0.0.0.0", port=5000)