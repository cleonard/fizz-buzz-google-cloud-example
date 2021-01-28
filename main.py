import json
import logging
import traceback

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


def fizzbuzz(request):
    error_response = {'error': 'Please provide a positive interger with the key `length` in the URLs querystring.'}
    try:
        length = int(request.args.get('length'))
    except:
        return json.dumps(error_response)

    if length < 1:
        return json.dumps(error_response)

    if length > 500:
        return json.dumps({'fizzbuzz': "{:,}? That's just silly!".format(length)})
    return json.dumps({"fizzbuzz": [f for f in gen_fizzbuzz(length)]})


class Request:
    def __init__(self, args):
        self.args = args


if __name__ == '__main__':
    request = Request({'length': 100})
    print(fizzbuzz(request))
