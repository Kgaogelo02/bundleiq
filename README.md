# BundleIQ — South Africa Data Bundle Comparison App

A full-stack web application that compares prepaid data bundle prices across all 4 major South African mobile networks in real time. Built to help South Africans stop overpaying for mobile data.

## Live Demo

- **App:** https://bundleiq-xk7b.onrender.com
- **API:** https://bundleiq-api.onrender.com/bundles
- **Admin:** https://bundleiq-xk7b.onrender.com/admin.html

## Networks Covered

| Network | Known For |
|---------|-----------|
| Vodacom | SA's largest network, NXT LVL specials |
| MTN | Strong promos, TikTok and night bundles |
| Cell C | Budget friendly monthly bundles |
| Telkom | Cheapest cost per GB in SA |

## Current Features

- Compare data bundles across all 4 networks
- Filter by bundle type — Monthly, Daily, Weekly, Night, Social, NXT LVL, Hourly
- Search by data size, network or bundle name
- Ranked results sorted by best value (cost per MB)
- Summary cards showing best deal, most data, best validity and savings percentage
- Dark mode toggle with saved preference
- Admin panel — password protected via backend authentication
- Auto scraper that runs every day at 7AM to keep prices updated
- Fully responsive — works on mobile and desktop
- Font Awesome icons throughout — no emojis in code

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
| POST | /admin/verify | Verify admin password |
| POST | /admin/bundle | Add a new bundle |
| PUT | /admin/bundle/\<id\> | Update a bundle by ID |
| DELETE | /admin/bundle/\<id\> | Delete a bundle by ID |

## Setup Instructions

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
ADMIN_PASSWORD=your_admin_password
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

Open `frontend/index.html` in your browser.

## Deployment

### Backend — Render Web Service
- Runtime: Python 3
- Root Directory: `backend`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn run:app`
- Environment Variables: `DATABASE_URL`, `ADMIN_PASSWORD`

### Frontend — Render Static Site
- Root Directory: `frontend`
- Build Command: leave empty
- Publish Directory: `.`

### Database — Supabase
- Free PostgreSQL in the cloud
- Region: Frankfurt EU Central
- Connection: Session Pooler (IPv4 compatible)

## Security

- Admin password is stored as an environment variable on Render — never visible in code
- All admin routes require a valid `X-Admin-Token` header verified by the backend
- `.env` file is excluded from GitHub via `.gitignore`

## Automatic Price Updates

A Windows Scheduled Task runs `scraper.py` every day at 7AM automatically.

To run manually:

```bash
python backend/scraper.py
```

## Roadmap

### Phase 2 — More Useful Features
- Coverage map showing best signal per province
- Price history tracking — see when networks changed prices
- Bundle calculator — enter daily data usage and get a recommendation
- Favourites — save bundles you like

### Phase 3 — Make It a Business
- SMS and email alerts when a network drops prices or adds a special
- User accounts with personalised bundle recommendations
- Network reviews — users rate speed and coverage
- Affiliate links to network websites to earn commission

### Phase 4 — Expand Beyond Data
- Airtime price comparison across networks
- Fibre package comparison — Openserve, Vumatel, Frogfoot
- Load shedding schedule integration
- Prepaid electricity rate comparison by municipality

### Phase 5 — Mobile App
- Convert to React Native app for Android and iOS
- Push notifications for daily best deal alerts
- Home screen widget showing today's best bundle

## Author

**Mabutsi Kgaogelo Kgagara**

Built BundleIQ to solve a real problem — South Africans constantly compare data prices but had no clean, accurate tool to do it in one place.

- GitHub: https://github.com/Kgaogelo02

## License

MIT License — free to use and modify.
