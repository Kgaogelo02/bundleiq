# BundleIQ

A full-stack web application that compares prepaid data bundle prices across all 4 major South African mobile networks. Built to help South Africans stop overpaying for mobile data.

## Live Demo

- **App:** https://bundleiq-xk7b.onrender.com
- **API:** https://bundleiq-api.onrender.com/bundles
- **Admin:** https://bundleiq-xk7b.onrender.com/admin.html

## What It Does

- Compares data bundles across Vodacom, MTN, Cell C and Telkom
- Sorts results by best value — lowest cost per MB first
- Filters by bundle type: Monthly, Daily, Weekly, Night, Social, NXT LVL, Hourly
- Search by data size, network or bundle name
- Shows summary cards: best deal, most data, best validity, savings percentage
- Dark mode toggle that remembers your preference
- Admin panel to add, edit or delete bundles
- Auto scraper that runs every day at 7AM to keep prices updated
- Fully responsive on mobile and desktop

## Screenshots

> App running at https://bundleiq.onrender.com

## Tech Stack

**Backend**
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-CORS
- PostgreSQL (Supabase)
- psycopg2-binary
- python-dotenv
- BeautifulSoup4
- Requests
- Gunicorn

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome 6 icons

**Infrastructure**
- Supabase — cloud PostgreSQL database (Frankfurt)
- Render — backend and frontend hosting
- GitHub — version control

## Project Structure

```
bundleiq/
    backend/
        run.py              Flask app and all API routes
        scraper.py          Auto scraper — runs daily at 7AM
        updater.py          Manual price updater
        seed_real.py        Seeds database with real SA bundle prices
        requirements.txt    Python dependencies
        .env                Environment variables (not committed)
    frontend/
        index.html          Main comparison app
        admin.html          Admin panel — password protected
    README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /bundles | Get all bundles |
| GET | / | API health check |
| POST | /admin/bundle | Add a new bundle |
| PUT | /admin/bundle/\<id\> | Update a bundle by ID |
| DELETE | /admin/bundle/\<id\> | Delete a bundle by ID |

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kgaogelo02/bundleiq.git
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
pip install -r requirements.txt
```

### 4. Create .env file

Create a file called `.env` inside the `backend` folder:

```
DATABASE_URL=postgresql://your_user:your_password@your_host:5432/your_db
```

### 5. Run the backend

```bash
python run.py
```

### 6. Seed the database

```bash
python seed_real.py
```

### 7. Open the frontend

Open `frontend/index.html` in your browser using Ctrl+O.

## Deployment

### Backend — Render Web Service
- Runtime: Python 3
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn run:app`
- Environment Variable: `DATABASE_URL`

### Frontend — Render Static Site
- Root Directory: `frontend`
- Build Command: leave empty
- Publish Directory: `.`

### Database — Supabase
- Free PostgreSQL in the cloud
- Region: Frankfurt EU Central
- Connection: Session Pooler (IPv4 compatible)

## Automatic Price Updates

A Windows Scheduled Task runs `scraper.py` every day at 7AM automatically.

To run the scraper manually:

```bash
python backend/scraper.py
```

## Admin Panel

Access at `/admin.html` — password protected.

Features:
- View all bundles with stats per network
- Add new bundles with automatic cost per MB calculation
- Edit any bundle price, name, validity or type
- Delete outdated bundles
- Search and filter bundles

## Networks Covered

| Network | Known For |
|---------|-----------|
| Vodacom | SA's largest network, NXT LVL specials |
| MTN | Strong promos, TikTok and night bundles |
| Cell C | Budget friendly monthly bundles |
| Telkom | Cheapest cost per GB in SA |

## Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_URL | Full PostgreSQL connection string |

## Author

**Mabutsi Kgaogelo**

Built BundleIQ to solve a real problem — South Africans constantly compare data prices but had no clean tool to do it in one place.

- GitHub: https://github.com/Kgaogelo02

## License

MIT License — free to use and modify.
