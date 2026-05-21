import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))

from run import app, db, Bundle

bundles = [
    # VODACOM
    Bundle(network="Vodacom", bundle_name="Vodacom 50MB", data_amount="50MB", price=5.00, validity="1 day", cost_per_mb=0.1000, bundle_type="prepaid"),
    Bundle(network="Vodacom", bundle_name="Vodacom 150MB", data_amount="150MB", price=10.00, validity="1 day", cost_per_mb=0.0667, bundle_type="prepaid"),
    Bundle(network="Vodacom", bundle_name="Vodacom 500MB", data_amount="500MB", price=25.00, validity="7 days", cost_per_mb=0.0500, bundle_type="prepaid"),
    Bundle(network="Vodacom", bundle_name="Vodacom 1GB", data_amount="1GB", price=49.00, validity="30 days", cost_per_mb=0.0490, bundle_type="prepaid"),
    Bundle(network="Vodacom", bundle_name="Vodacom 2GB", data_amount="2GB", price=89.00, validity="30 days", cost_per_mb=0.0445, bundle_type="prepaid"),

    # MTN
    Bundle(network="MTN", bundle_name="MTN 60MB", data_amount="60MB", price=5.00, validity="1 day", cost_per_mb=0.0833, bundle_type="prepaid"),
    Bundle(network="MTN", bundle_name="MTN 200MB", data_amount="200MB", price=10.00, validity="7 days", cost_per_mb=0.0500, bundle_type="prepaid"),
    Bundle(network="MTN", bundle_name="MTN 750MB", data_amount="750MB", price=25.00, validity="30 days", cost_per_mb=0.0333, bundle_type="prepaid"),
    Bundle(network="MTN", bundle_name="MTN 1.5GB", data_amount="1.5GB", price=49.00, validity="30 days", cost_per_mb=0.0327, bundle_type="prepaid"),
    Bundle(network="MTN", bundle_name="MTN 3GB", data_amount="3GB", price=89.00, validity="30 days", cost_per_mb=0.0297, bundle_type="prepaid"),

    # CELL C
    Bundle(network="Cell C", bundle_name="Cell C 80MB", data_amount="80MB", price=5.00, validity="1 day", cost_per_mb=0.0625, bundle_type="prepaid"),
    Bundle(network="Cell C", bundle_name="Cell C 250MB", data_amount="250MB", price=10.00, validity="7 days", cost_per_mb=0.0400, bundle_type="prepaid"),
    Bundle(network="Cell C", bundle_name="Cell C 1GB", data_amount="1GB", price=25.00, validity="30 days", cost_per_mb=0.0250, bundle_type="prepaid"),
    Bundle(network="Cell C", bundle_name="Cell C 2GB", data_amount="2GB", price=49.00, validity="30 days", cost_per_mb=0.0245, bundle_type="prepaid"),
    Bundle(network="Cell C", bundle_name="Cell C 5GB", data_amount="5GB", price=89.00, validity="30 days", cost_per_mb=0.0178, bundle_type="prepaid"),

    # TELKOM
    Bundle(network="Telkom", bundle_name="Telkom 100MB", data_amount="100MB", price=5.00, validity="7 days", cost_per_mb=0.0500, bundle_type="prepaid"),
    Bundle(network="Telkom", bundle_name="Telkom 350MB", data_amount="350MB", price=10.00, validity="30 days", cost_per_mb=0.0286, bundle_type="prepaid"),
    Bundle(network="Telkom", bundle_name="Telkom 1.5GB", data_amount="1.5GB", price=25.00, validity="30 days", cost_per_mb=0.0167, bundle_type="prepaid"),
    Bundle(network="Telkom", bundle_name="Telkom 3GB", data_amount="3GB", price=49.00, validity="30 days", cost_per_mb=0.0163, bundle_type="prepaid"),
    Bundle(network="Telkom", bundle_name="Telkom 6GB", data_amount="6GB", price=89.00, validity="30 days", cost_per_mb=0.0148, bundle_type="prepaid"),
]

with app.app_context():
    db.session.add_all(bundles)
    db.session.commit()
    print(">>> Seeded", len(bundles), "bundles successfully!")
