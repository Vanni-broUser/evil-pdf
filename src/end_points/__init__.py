import traceback


ERROR_MESSAGE = 'Errore generico'


def error_catching_decorator(func):

  def wrapper(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception:
      traceback.print_exc()
      return {
        'status': 'ko',
        'error': ERROR_MESSAGE
      }

  wrapper.__name__ = func.__name__
  return wrapper
