# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Short-Link-API/blob/main/LICENSE

from flask import Flask, redirect, render_template, request, jsonify, json
from shortener import short


app = Flask(__name__, template_folder="public")


@app.route("/")
def main():
    if request.args.get('query'):
        query = request.args.get('query')
    else:
        return render_template("index.html")
    results = short(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": "Something wrong"}
        )


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
