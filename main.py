from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/gnavi/search_rest")
def gnavi_search_rest():
    greet = "gnavi search_rest"
    result = {
        "Result": {
            "Greeting": greet
        }
    }
    return jsonify(ResultSet=result)

if __name__ == '__main__':
    app.run(debug=True)

