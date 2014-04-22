from functools import wraps

from flask import g, flash, redirect, url_for, request

def requires_login(f):
    """
    This decorator is checking that g.user has a value assigned to it, 
    otherwise it means that the user isn't authenticated, we then add 
    a message to be displayed to the user on the next page and redirect
    him to the login view. You probably wonder how g.user gets defined,
    it's in the user's views.py, through the before_request. You'll 
    realize later that if you pull a lot of information from your user's 
    profile (historical data, friends, messages, activities...) this
    might become a bottle neck and caching user through their id might 
    be a good solution (as long as you centralize your object modifications 
    and clear this cache on every update).
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function