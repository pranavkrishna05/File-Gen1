from flask import Flask
from app.auth.controllers.register_controller import register_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(register_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

"""
This file integrates the register controller with the Flask application by registering it as a blueprint.
"""