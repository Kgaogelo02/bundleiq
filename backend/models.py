from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Bundle(db.Model):
    __tablename__ = "bundles"

    id = db.Column(db.Integer, primary_key=True)
    network = db.Column(db.String(50))
    bundle_name = db.Column(db.String(255))
    data_amount = db.Column(db.String(50))
    price = db.Column(db.Numeric(10,2))
    validity = db.Column(db.String(50))
    cost_per_mb = db.Column(db.Numeric(10,4))
    bundle_type = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)