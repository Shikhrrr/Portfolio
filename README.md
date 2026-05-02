# Shikhar Kanaujia — Portfolio

A production-ready Django portfolio web application. Single-page frontend with brutalist-editorial design, backed by Django admin for content management.

## Tech Stack
- **Backend**: Django 6 (Python)
- **Templating**: Jinja2 (configured alongside Django's admin templates)
- **Database**: SQLite (default)
- **CSS**: Plain CSS — no Tailwind, no Bootstrap
- **JS**: Vanilla JavaScript

## Setup

### 1. Clone the repository
```bash
git clone <repo-url>
cd Portfolio
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Seed initial portfolio data
```bash
python manage.py seed_portfolio
```

### 6. Create a superuser (for Django admin)
```bash
python manage.py createsuperuser
```

### 7. Start the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** for the portfolio.  
Visit **http://127.0.0.1:8000/admin/** for the admin dashboard.

---

## URLs

| Path | Description |
|---|---|
| `/` | Single-page portfolio (public) |
| `/download-resume/` | Serves resume PDF download |
| `/hire/` | Handles contact form POST |
| `/admin/` | Django admin (superuser only) |
| `/robots.txt` | SEO robots file |

---

## Adding Images

See **IMAGE_PLACEHOLDERS.txt** for full details. Quick summary:

| Image | Where to add |
|---|---|
| Hero profile photo | `static/images/hero_profile.jpg` |
| Contact section photo | `static/images/contact_photo.jpg` |
| Project screenshots | Upload via admin → Projects → [project] → image |

---

## Uploading the Resume

1. Log in at `/admin/`
2. Go to **Portfolio > Site Configuration**
3. Upload the PDF in the **Resume file** field
4. The **Download Resume** button on the hero will now serve the file

---

## Content Management (Django Admin)

All portfolio content is managed through `/admin/`:

- **Site Configuration** — bio, resume, social links, meta description
- **Experiences** — timeline entries (company, role, bullets)
- **Projects** — card grid (name, description, tech stack, image, links)
- **Skills** — tagged skill chips by category
- **Achievements** — hackathon wins, awards, recognitions
- **Hire Requests** — view contact form submissions (read-only, mark as read)

---

## Design

- Background: `#0A0A0A` (near-black)
- Primary accent: `#FF2200` (electric red)
- Secondary accent: `#FFEE00` (acid yellow)
- Tertiary: `#0044FF` (electric blue)
- Typography: **Bebas Neue** (display) + **IBM Plex Mono** (body/mono) + **Syne** (UI)
- Zero gradients. Sharp edges. Hard offset shadows.
