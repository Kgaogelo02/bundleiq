# BundleIQ — South Africa Data Bundle Comparison App

A full-stack web application that compares prepaid data bundle prices across all 4 major South African mobile networks in real time.

## Networks Covered

- Vodacom
- MTN
- Cell C
- Telkom

## Features

- Compare data bundles across all 4 networks
- Filter by bundle type — Monthly, Daily, Weekly, Night, Social, NXT LVL, Hourly
- Search by data size, network or bundle name
- Ranked results sorted by best value (cost per MB)
- Summary cards showing best deal, most data, best validity and savings percentage
- Dark mode toggle with saved preference
- Admin panel to add, edit or delete bundles
- Auto scraper that runs every day at 7AM to keep prices updated
- Fully responsive — works on mobile and desktop

## Tech Stack

### Backend
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- PostgreSQL
- psycopg2
- python-dotenv
- BeautifulSoup4
- Requests

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome 6 icons

## Project Structure

```
bundleiq/
    backend/
        run.py          — Flask app and API routes
        models.py       — Database models
        config.py       — Configuration
        seed_real.py    — Seed database with real SA bundle prices
        scraper.py      — Auto scraper that updates prices daily
        updater.py      — Manual price updater
        .env            — Environment variables (not committed to git)
        requirements.txt
    frontend/
        index.html      — Main comparison app
        admin.html      — Admin panel to manage bundles
    README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /bundles | Get all bundles |
| POST | /admin/bundle | Add a new bundle |
| PUT | /admin/bundle/<id> | Update a bundle |
| DELETE | /admin/bundle/<id> | Delete a bundle |

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/yourusername/bundleiq.git
cd bundleiq
```

### 2. Create and activate virtual environment

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-cors psycopg2-binary python-dotenv beautifulsoup4 requests lxml
```

### 4. Create .env file

Create a file called `.env` inside the `backend` folder:

```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/bundleiq_db
```

### 5. Create the database

Open pgAdmin and create a database called `bundleiq_db`.

### 6. Run the app

```bash
python run.py
```

### 7. Seed the database

```bash
python seed_real.py
```

### 8. Open the frontend

Open `frontend/index.html` in your browser.

## Automatic Price Updates

The scraper runs automatically every day at 7AM via Windows Task Scheduler.

To run it manually:

```bash
python scraper.py
```

## Admin Panel

Open `frontend/admin.html` to:

- View all bundles
- Add new bundles
- Edit existing bundle prices
- Delete outdated bundles

## Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_URL | Full PostgreSQL connection string |

## Author

Built by Mabutsi Kgaogelo— BundleIQ helps South Africans find the best data deals and stop overpaying for mobile data.

## License

MIT License
