# URL Shortener API

A scalable URL shortening service built with FastAPI and PostgreSQL.

## Tech Stack
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **JWT** - Authentication
- **Docker** - Containerization

## Features
- ✨ Create short URLs
- 🔄 Redirect to original URLs
- 📊 Click analytics
- 🔐 User authentication
- ⚡ Redis caching (coming soon)

## API Endpoints

### Health Check
\\\
GET / → Welcome message
GET /health → Service status
\\\

### Authentication (Coming Day 2)
\\\
POST /auth/signup - Create account
POST /auth/login - Get JWT token
\\\

## Setup Locally

1. **Clone the repository**
\\\ash
git clone https://github.com/Anshumank229/URL-Shortner.git
cd URL-Shortner
\\\

2. **Create virtual environment**
\\\ash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
\\\

3. **Install dependencies**
\\\ash
pip install -r requirements.txt
\\\

4. **Set up environment variables**
Create a \.env\ file with:
\\\
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/urlshortener
SECRET_KEY=your-secret-key
\\\

5. **Run the server**
\\\ash
uvicorn app.main:app --reload
\\\"

6. **Visit API docs**
http://localhost:8000/docs

## Project Status
- ✅ Day 1: Project setup, database connection
- ⏳ Day 2: Authentication
- ⏳ Day 3: URL shortening
- ⏳ Day 4: Redirect service

## License
MIT

## Author
Anshuman Kumar
