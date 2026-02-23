from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def hello_moon():
    return render_template('index.html')

@app.route("/<path:filename>", methods=["GET"])
def serve_image(filename):
    file_path = os.path.join("/img", filename)

    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(IMG_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
