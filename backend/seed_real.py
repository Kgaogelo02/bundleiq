import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

bundles = [
    # VODACOM - real 2026 prices
    ("Vodacom", "Vodacom Hourly 50MB",        "50MB",   5.00,  "1 hour",   0.1000, "hourly"),
    ("Vodacom", "Vodacom Daily 20MB",          "20MB",   5.00,  "1 day",    0.2500, "daily"),
    ("Vodacom", "Vodacom 240MB Monthly",       "240MB",  29.00, "30 days",  0.1208, "monthly"),
    ("Vodacom", "Vodacom 420MB Monthly",       "420MB",  49.00, "30 days",  0.1167, "monthly"),
    ("Vodacom", "Vodacom 1.2GB Monthly",       "1.2GB",  85.00, "30 days",  0.0708, "monthly"),
    ("Vodacom", "Vodacom 20GB+20GB Night Owl", "40GB",  229.00, "30 days",  0.0057, "monthly"),
    ("Vodacom", "Vodacom 50GB+50GB Night Owl", "100GB", 349.00, "30 days",  0.0035, "monthly"),

    # MTN - real 2026 prices
    ("MTN", "MTN TikTok 100MB Daily",  "100MB",  5.00,  "1 day",   0.0500, "social"),
    ("MTN", "MTN Night 250MB",         "250MB",  8.00,  "1 night", 0.0320, "night"),
    ("MTN", "MTN TikTok 1GB Monthly",  "1GB",   50.00,  "30 days", 0.0500, "social"),
    ("MTN", "MTN Monthly 50GB",        "50GB",  299.00, "30 days", 0.0060, "monthly"),

    # TELKOM - real 2026 prices (cheapest in SA)
    ("Telkom", "Telkom WhatsApp 250MB Daily", "250MB",  4.00,  "1 day",   0.0160, "social"),
    ("Telkom", "Telkom Night Surfer 1GB",     "1GB",   10.00,  "1 night", 0.0100, "night"),
    ("Telkom", "Telkom 10GB Monthly",         "10GB",  89.00,  "30 days", 0.0089, "monthly"),
    ("Telkom", "Telkom 20GB Monthly",         "20GB",  99.00,  "30 days", 0.0050, "monthly"),
    ("Telkom", "Telkom 40GB Monthly",         "40GB",  189.00, "30 days", 0.0047, "monthly"),

    # CELL C - real 2026 prices
    ("Cell C", "Cell C Daily 100MB",    "100MB",  7.00,  "1 day",   0.0700, "daily"),
    ("Cell C", "Cell C 30GB Monthly",   "30GB",  299.00, "30 days", 0.0100, "monthly"),
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
    print(">>> Real SA bundle prices loaded:", len(bundles), "bundles")
