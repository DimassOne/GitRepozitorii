from flask import session
from functools import wraps

def chek(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        if 'user' in session:
            return func(*args, **kwargs)
        return "Вы не авторезированы"
    return wraper









##from flask import session
##from functools import wraps
##
##def check_logged_in(func:object):
##    @wraps(func)
##    def wriper(*argv, **kwargv):
##        if 'logged_in' in session:
##            return func(*argv, **kwargv)
##        return 'Вы не в системе'
##    return wriper


