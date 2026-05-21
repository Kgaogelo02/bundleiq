import os
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Updated bundle data - edit these prices when networks change them
bundles = [
    # VODACOM
    ("Vodacom", "Vodacom 50MB",   "50MB",  5.00,  "1 day",   0.1000, "prepaid"),
    ("Vodacom", "Vodacom 150MB",  "150MB", 10.00, "1 day",   0.0667, "prepaid"),
    ("Vodacom", "Vodacom 500MB",  "500MB", 25.00, "7 days",  0.0500, "prepaid"),
    ("Vodacom", "Vodacom 1GB",    "1GB",   49.00, "30 days", 0.0490, "prepaid"),
    ("Vodacom", "Vodacom 2GB",    "2GB",   89.00, "30 days", 0.0445, "prepaid"),
    # MTN
    ("MTN", "MTN 60MB",   "60MB",  5.00,  "1 day",   0.0833, "prepaid"),
    ("MTN", "MTN 200MB",  "200MB", 10.00, "7 days",  0.0500, "prepaid"),
    ("MTN", "MTN 750MB",  "750MB", 25.00, "30 days", 0.0333, "prepaid"),
    ("MTN", "MTN 1.5GB",  "1.5GB", 49.00, "30 days", 0.0327, "prepaid"),
    ("MTN", "MTN 3GB",    "3GB",   89.00, "30 days", 0.0297, "prepaid"),
    # CELL C
    ("Cell C", "Cell C 80MB",  "80MB",  5.00,  "1 day",   0.0625, "prepaid"),
    ("Cell C", "Cell C 250MB", "250MB", 10.00, "7 days",  0.0400, "prepaid"),
    ("Cell C", "Cell C 1GB",   "1GB",   25.00, "30 days", 0.0250, "prepaid"),
    ("Cell C", "Cell C 2GB",   "2GB",   49.00, "30 days", 0.0245, "prepaid"),
    ("Cell C", "Cell C 5GB",   "5GB",   89.00, "30 days", 0.0178, "prepaid"),
    # TELKOM
    ("Telkom", "Telkom 100MB", "100MB", 5.00,  "7 days",  0.0500, "prepaid"),
    ("Telkom", "Telkom 350MB", "350MB", 10.00, "30 days", 0.0286, "prepaid"),
    ("Telkom", "Telkom 1.5GB", "1.5GB", 25.00, "30 days", 0.0167, "prepaid"),
    ("Telkom", "Telkom 3GB",   "3GB",   49.00, "30 days", 0.0163, "prepaid"),
    ("Telkom", "Telkom 6GB",   "6GB",   89.00, "30 days", 0.0148, "prepaid"),
]

with engine.connect() as conn:
    conn.execute(text("DELETE FROM bundles"))
    for b in bundles:
        conn.execute(text("""
            INSERT INTO bundles (network, bundle_name, data_amount, price, validity, cost_per_mb, bundle_type)
            VALUES (:network, :bundle_name, :data_amount, :price, :validity, :cost_per_mb, :bundle_type)
        """), {
            "network": b[0], "bundle_name": b[1], "data_amount": b[2],
            "price": b[3], "validity": b[4], "cost_per_mb": b[5], "bundle_type": b[6]
        })
    conn.commit()
    print(">>> Bundles updated successfully:", len(bundles), "bundles")
