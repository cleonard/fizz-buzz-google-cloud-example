from flask import Flask, jsonify

app = Flask(__name__)


def gen_fizzbuzz(l):
    def yield_fizzbuzz(i):
        fizz = (i % 3 == 0)
        buzz = (i % 5 == 0)
        if fizz and buzz:
            return 'FIZZBUZZ'
        elif fizz:
            return 'FIZZ'
        elif buzz:
            return 'BUZZ'
        else:
            return str(n)
    n = 0
    while n < l:
        yield yield_fizzbuzz(n + 1)
        n += 1


@app.route("/fizzbuzz/<int:length>")
def fizzbuzz(length):
    if length > 500:
        return jsonify({"fizzbuzz": "{:,}? That's just silly!".format(length)})
    return jsonify({"fizzbuzz": [f for f in gen_fizzbuzz(length)]})


if __name__ == '__main__':
    app.run()
