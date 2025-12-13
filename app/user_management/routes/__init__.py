from flask import Blueprint
from app.user_management.controllers.registration_controller import registration_blueprint

user_management_blueprint = Blueprint("user_management", __name__)

# Register routes
user_management_blueprint.register_blueprint(registration_blueprint, url_prefix="/user-management")