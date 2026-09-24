from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "Лабораторная работа 2",
        "routes": ["/calc", "/profile", "/convert"]
    })


@app.route("/calc")
def calc():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None:
        return jsonify({
            "ok": False,
            "error": "Укажите числовые параметры a и b"
        }), 400

    return jsonify({
        "ok": True,
        "a": a,
        "b": b,
        "sum": a + b,
        "difference": a - b,
        "product": a * b
    })


@app.route("/profile")
def profile():
    name = request.args.get("name", "").strip()
    group = request.args.get("group", "").strip()
    age = request.args.get("age", type=int)

    if name == "" or group == "" or age is None:
        return jsonify({
            "ok": False,
            "error": "Укажите name, group и целочисленный age"
        }), 400

    return jsonify({
        "ok": True,
        "name": name,
        "group": group,
        "age": age
    })


@app.route("/convert")
def convert():
    celsius = request.args.get("celsius", type=float)

    if celsius is None:
        return jsonify({
            "ok": False,
            "error": "Укажите числовой параметр celsius"
        }), 400

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15

    return jsonify({
        "ok": True,
        "celsius": celsius,
        "fahrenheit": round(fahrenheit, 2),
        "kelvin": round(kelvin, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
