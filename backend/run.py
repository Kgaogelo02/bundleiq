import os
from functools import wraps
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "changeme")

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-Admin-Token")
        if token != ADMIN_PASSWORD:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

class Bundle(db.Model):
    __tablename__ = "bundles"
    id = db.Column(db.Integer, primary_key=True)
    network = db.Column(db.String(50))
    bundle_name = db.Column(db.String(100))
    data_amount = db.Column(db.String(50))
    price = db.Column(db.Numeric(6,2))
    validity = db.Column(db.String(50))
    cost_per_mb = db.Column(db.Numeric(10,4))
    bundle_type = db.Column(db.String(50))

@app.route("/")
def home():
    return {"message": "BundleIQ API Running"}

@app.route("/bundles")
def get_bundles():
    bundles = Bundle.query.all()
    return jsonify([{
        "id": b.id,
        "network": b.network,
        "bundle_name": b.bundle_name,
        "data_amount": b.data_amount,
        "price": float(b.price),
        "validity": b.validity,
        "cost_per_mb": float(b.cost_per_mb),
        "bundle_type": b.bundle_type
    } for b in bundles])

@app.route("/admin/verify", methods=["POST"])
def verify_admin():
    token = request.headers.get("X-Admin-Token")
    if token != ADMIN_PASSWORD:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"message": "OK"}), 200

@app.route("/admin/bundle", methods=["POST"])
@require_auth
def add_bundle():
    d = request.json
    mb = float(d["data_mb"])
    b = Bundle(
        network=d["network"],
        bundle_name=d["bundle_name"],
        data_amount=d["data_amount"],
        price=float(d["price"]),
        validity=d["validity"],
        cost_per_mb=round(float(d["price"]) / mb, 4),
        bundle_type=d["bundle_type"]
    )
    db.session.add(b)
    db.session.commit()
    return jsonify({"message": "Bundle added", "id": b.id})

@app.route("/admin/bundle/<int:bundle_id>", methods=["PUT"])
@require_auth
def update_bundle(bundle_id):
    b = Bundle.query.get_or_404(bundle_id)
    d = request.json
    b.network = d.get("network", b.network)
    b.bundle_name = d.get("bundle_name", b.bundle_name)
    b.data_amount = d.get("data_amount", b.data_amount)
    b.price = float(d.get("price", b.price))
    b.validity = d.get("validity", b.validity)
    b.bundle_type = d.get("bundle_type", b.bundle_type)
    if "data_mb" in d:
        b.cost_per_mb = round(float(d["price"]) / float(d["data_mb"]), 4)
    db.session.commit()
    return jsonify({"message": "Bundle updated"})

@app.route("/admin/bundle/<int:bundle_id>", methods=["DELETE"])
@require_auth
def delete_bundle(bundle_id):
    b = Bundle.query.get_or_404(bundle_id)
    db.session.delete(b)
    db.session.commit()
    return jsonify({"message": "Bundle deleted"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print(">>> Tables ready")
    app.run(debug=True)
