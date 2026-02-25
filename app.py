from flask import Flask, request, jsonify

app = Flask(__name__)

# one-time use keys
licenses = {
    # original
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

    # additional keys
    "9XZ2-PLK8-TR5Q-WE91": False,
    "AB7Q-KL92-XCV4-TY8M": False,
    "P0OI-UY76-TGBV-FR45": False,
    "LKJH-67GF-DSA2-QWER": False,
    "QAZX-SWED-CVFR-TGBY": False,
    "MNBV-CXZL-KJHG-FDSA": False,
    "TREW-QAZX-PLKM-NHBG": False,
    "DFGH-JKLO-98UY-TREW": False,
    "ZXCV-BNM1-ASDF-GHJK": False,
    "GH56-JKLP-90BN-VFRT": False,
    "QW12-ER34-TY56-UI78": False,
    "PO90-LK87-MN65-BV43": False,
    "AS12-DF34-GH56-JK78": False,
    "ZX98-CV76-BN54-MK32": False,
    "YU11-IO22-PL33-KJ44": False,
    "RT55-FG66-VB77-NM88": False,
    "WE99-XS88-CD77-VF66": False,
    "ED55-CV44-BG33-NH22": False,
    "RF11-VT22-GB33-YH44": False,
    "TG55-BY66-HN77-UJ88": False
}

# lifetime keys (never expire)
lifetime_keys = {
    "ixzeliuskey",
    "ScriptzKeyLifeTime"
}

@app.route("/activate", methods=["POST"])
def activate():
    data = request.json
    key = data.get("key")

    print(f"[REQUEST] Key: {key}")

    # Lifetime keys always valid
    if key in lifetime_keys:
        return jsonify({
            "valid": True,
            "type": "lifetime",
            "message": "Lifetime license accepted"
        })

    # One-time keys
    if key in licenses and not licenses[key]:
        licenses[key] = True
        return jsonify({
            "valid": True,
            "type": "single_use",
            "message": "License activated"
        })

    return jsonify({
        "valid": False,
        "message": "Invalid or already used"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
