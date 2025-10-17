# Plateforme de Mise en Relation

## Overview
A French professional appointment booking platform built with Flask. The application allows users to register as clients or professionals, with professionals offering available time slots and clients booking appointments.

## Project Type
Flask web application with SQLite database

## Architecture

### Technology Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML templates with Jinja2
- **Styling**: Custom CSS

### Project Structure
```
.
├── app.py                 # Main Flask application
├── database.db           # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Landing page
│   ├── register.html    # User registration
│   ├── login.html       # User login
│   ├── dashboard_user.html    # Client dashboard
│   ├── dashboard_pro.html     # Professional dashboard
│   ├── professionals.html     # List of professionals
│   ├── book.html             # Booking interface
│   └── add_slot.html         # Add time slots (pros only)
└── static/
    └── style.css        # Styling

```

### Database Schema
- **users**: id, name, email, password, role (client/pro)
- **slots**: id, pro_id, date (available time slots)
- **rendezvous**: id, pro_id, client_id, date (booked appointments)

## Features
1. User registration (client or professional)
2. User authentication
3. Professional directory browsing
4. Appointment slot management (for professionals)
5. Appointment booking (for clients)
6. Dashboard views for both user types

## Setup and Configuration

### Environment
- Python 3.11
- Flask development server running on 0.0.0.0:5000
- SQLite database auto-initializes on first run

### Workflow
- **Flask App**: Runs the main application server on port 5000

### Deployment
- Configured for Replit autoscale deployment (basic setup complete)
- Currently uses Flask development server (NOT production-ready)
- **TODO for Production**: Replace with production WSGI server (e.g., Gunicorn, Waitress)

## Recent Changes (October 17, 2025)
- Imported project from GitHub
- Configured for Replit environment
- Updated Flask app to bind to 0.0.0.0:5000 for proper port exposure
- Installed Python 3.11 and Flask dependencies
- Initialized SQLite database
- Configured development workflow
- Set up deployment configuration

## User Preferences
- Language: French (application interface)
- Database: SQLite (existing choice maintained)

## Notes
- The application uses Flask's development server in debug mode
- **Security Considerations for Production:**
  - Session secret key is currently hardcoded (should use environment variables)
  - Passwords are stored in plain text (should implement hashing with bcrypt or similar)
  - Flask development server is not suitable for production (use Gunicorn/Waitress instead)
