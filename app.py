from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from api.extensions import db  # ✅ Import from extensions
from api.routes import routes  # ✅ Import Blueprint only after initializing db
import os

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for frontend

# Configure database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///timesheet.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# Register Blueprints
app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
