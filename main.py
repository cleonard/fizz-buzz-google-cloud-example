import logging
import traceback

from flask import Flask, jsonify

app = Flask(__name__)


def try_catch_log(wrapped_func):
  def wrapper(*args, **kwargs):
    try:
      response = wrapped_func(*args, **kwargs)
    except Exception:
      # Replace new lines with spaces so as to prevent several entries which
      # would trigger several errors.
      error_message = traceback.format_exc().replace('\n', '  ')
      logging.error(error_message)
      return 'Error';
    return response;
  return wrapper;


def gen_fizzbuzz(length):
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
            return str(i)
    n = 0
    while n < length:
        yield yield_fizzbuzz(n + 1)
        n += 1


@app.route("/fizzbuzz/<int:length>")
def fizzbuzz(length):
    if length > 500:
        return jsonify({"fizzbuzz": "{:,}? That's just silly!".format(length)})
    return jsonify({"fizzbuzz": [f for f in gen_fizzbuzz(length)]})


if __name__ == '__main__':
    app.run()
