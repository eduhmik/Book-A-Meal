"""
This module includes all the logic triggered by endpoints
"""
from functools import wraps
from app.Controller import Controller
from app.EndPointParams import SignupParams, SigninParams, MealParams, ResetParams, RsvpParams

from flask_restful import Resource
from flask import session


CONTROLLER = Controller()

class Signup(SignupParams, Resource):
    """
    Class provides logic for signing up a user
    """
    def post(self):
        """
        listens for a post request then registers user
        """
        args = self.param.parse_args()
        user_data = {
            "username":args['username'],
            "email":args['email'],
            "password":args['password']
        }
        resp = CONTROLLER.sign_up_user(user_data)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
        
class Authentication(SigninParams, Resource):
    """
    Class contains logic that authenticates the users
    """
    def get(self):
        """
        Triggered by a get request and logs out the user
        """
        if 'user' in session:
            session.pop('user')
            session['signed_in'] = False

            return {'success':True, 'message':'user signed out'}
        else:
            return {'success':False, 'message':'Try logging in first :-)'}
    def post(self):
        """
        Triggered by a post request and logs in the user
        """
        args = self.param.parse_args()
        resp = CONTROLLER.sign_in_user(args['email'], args['password'])
        if resp.get('success'):
            session['user'] = args['email']
            session['signed_in'] = True
            return resp, 201
        else:
            return resp, 401
class ForgotPassword(ResetParams, Resource):
    """
    Class contains logic to reset users password
    """
    @auth_required
    def post(self):
        """
        Triggered by a post request and resets users password
        """
        args = self.param.parse_args()
        resp = CONTROLLER.reset_password(args['email'], args['password'])
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401

class add_meal(MealParams, Resource):
    """
    Class contains logic to add and retrieve meal
    """
    @auth_required
    def get(self):
        """
        Triggered by get request and retrieves all meals
        """
        resp = CONTROLLER.retrieve_all_mealss()
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
    @auth_required
    def post(self):
        """
        Triggered by a post request and adds a meal
        """
        args = self.param.parse_args()
        meal_data = {
            'name':args['name'],
            'price':args['price'],
            'rsvp':[]
        }
        resp = CONTROLLER.add_meal(meal_data)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
class Meal(Resource):
    """
    Class contains logic to retrieveeingle meal and delete meals
    """
    @auth_required
    def put(self, mealId):
        """
        Triggered by a put request and retrieves a single meal
        """
        resp = CONTROLLER.retrieve_single_meal(session['user'], mealId)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
    @auth_required
    def delete(self, mealId):
        """
        triggered by a delete request and deletes meal specified
        """
        resp = CONTROLLER.delete_single_meal(session['user'], mealId)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
class Menu(Resource):
    """
    Class contains logic to retrieve menu 
    """
    @auth_required
    def get(self, menu):
        """
        Triggered by a put request and retrieves menu
        """
        resp = CONTROLLER.retriveMenu(session['user'], menu)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
    @auth_required
    def post(self):
        """
        Triggered by a post request and adds a menu
        """
        args = self.param.parse_args()
        meal_data = {
            'name':args['name'],
            'price':args['price'],
            'rsvp':[]
        }
        resp = CONTROLLER.add_meal(meal_data)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 401
   
class Rsvp(RsvpParams, Resource):
    """
    Class manipulates Rsvp of meals
    """
    @auth_required
    def post(self, mealId):
        """
        Triggered by a post method and adds user to rsvp list
        """
        args = self.param.parse_args()
        resp = CONTROLLER.add_rsvp(session['user'], mealId, args['client_email'])
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409
    @auth_required
    def get(self, mealId):
        """
        Triggered ny get and retrieves a single rsvp
        """
        args = self.param.parse_args()
        resp = CONTROLLER.retrieve_rsvp(args['client_email'], mealId)
        if resp.get('success'):
            return resp, 201
        else:
            return resp, 409