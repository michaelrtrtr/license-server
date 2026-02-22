from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "X9F3-7KQ2-ZL8W-1MNP": False,
    "A7D2-VQ91-XC4R-8TLM": False,
    "P4ZX-88LK-2QWE-R9TN": False,
    "H2JK-4PL9-7SDF-3YTR": False,
    "M9QA-1ZXC-5VBN-8WPL": False,
    "T7YU-3REW-9KLM-2XCV": False,
    "Q2WX-6EDC-4RFV-8TGB": False,
    "Z8PL-3KJH-6NMB-1QAZ": False,
    "L0MK-9IJN-4UHB-7YGV": False,
    "W3ER-8TYU-2IOP-6ASD": False,
    "N5BV-7CXZ-1LKJ-9HGF": False,
    "R4TF-2GHY-8UJW-6QAZ": False,
    "S8PL-0OKM-3NIJ-7BHU": False,
    "E2DC-9RFV-6TGB-4YHN": False,
    "C7XZ-1ASD-8QWE-5RTY": False,
    "V3BN-6MJK-2LOP-9UIH": False,
    "K8IJ-4UHY-7GTB-1RFV": False,
    "B9NM-3LKJ-5HGF-2DSA": False,
    "Y6TR-8EWQ-1ZXA-4SDF": False,
    "U2IO-9PLM-7KJN-5BHV": False
}

@app.route("/activate", methods=["POST"])
def activate():
    data = request.json
    print("Received:", data)

    key = data.get("key")

    print("Key status:", licenses.get(key))

    if key in licenses and licenses[key] is False:
        licenses[key] = True
        return jsonify({"valid": True})

    return jsonify({"valid": False})


app.run(host="0.0.0.0", port=5000)
