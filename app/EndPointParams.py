"""
Module contains all the params of the requests
"""
from flask_restful import reqparse

class SignupParams(object):
    """
    Signup endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('username', type=str, required=True)
    param.add_argument('email', type=str, required=True)
    param.add_argument('password', type=str, required=True)
class SigninParams(object):
    """
    Signin endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('email', type=str, required=True)
    param.add_argument('password', type=str, required=False)
class ResetParams(object):
    """
    Password reset endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('email', type=str, required=True)
    param.add_argument('password', type=str, required=True)
class MealParams(object):
    """
    Meals endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('name', type=str, required=False)
    param.add_argument('price', type=str, required=False)
class RetriveEventsParams(object):
    """
    Restrieve events endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('userEmail', type=str, required=True)
class RsvpParams(object):
    """
    Rsvp endpoint params
    """
    param = reqparse.RequestParser()
    param.add_argument('clientEmail')