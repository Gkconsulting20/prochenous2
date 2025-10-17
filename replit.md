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
├── init_data.py          # Script to initialize default data
├── database.db           # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template (with modern navbar)
│   ├── index.html       # Landing page (with feature boxes)
│   ├── register.html    # User registration (with location field)
│   ├── login.html       # User login
│   ├── dashboard_user.html    # Client dashboard
│   ├── dashboard_pro.html     # Professional dashboard
│   ├── professionals.html     # List of professionals (card layout)
│   ├── book.html             # Booking interface
│   ├── add_slot.html         # Add time slots (pros only)
│   └── rate.html             # Rating form for professionals
└── static/
    └── style.css        # Modern responsive styling

```

### Database Schema
- **users**: id, name, email, password, role (client/pro), localisation
- **slots**: id, pro_id, date (available time slots)
- **rendezvous**: id, pro_id, client_id, date (booked appointments)
- **avis**: id, pro_id, client_id, note, commentaire, date (reviews/ratings)

## Features
1. User registration (client or professional)
2. User authentication
3. Professional directory browsing with:
   - Geographic location display
   - Average rating and review count
   - Sorted by rating (best first)
   - Username display without contact details
4. Appointment slot management (for professionals)
5. Appointment booking (for clients)
6. Rating system for professionals
7. Dashboard views for both user types

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

### Initial Setup
- Imported project from GitHub
- Configured for Replit environment
- Updated Flask app to bind to 0.0.0.0:5000 for proper port exposure
- Installed Python 3.11 and Flask dependencies
- Initialized SQLite database
- Configured development workflow
- Set up deployment configuration

### New Features Added
- **Geographic Location**: Professionals can now add their location during registration
- **Rating System**: 
  - New "avis" table for storing ratings and reviews
  - Clients can rate professionals (1-5 stars)
  - Average rating and review count displayed on professional listings
  - Professionals sorted by rating (best first)
- **Improved Privacy**: 
  - Display username/pseudo instead of full contact details
  - Email addresses no longer visible in professional listings
- **Enhanced UI**:
  - Location field appears conditionally for professionals during registration
  - Professional cards show location with 📍 icon
  - Rating display with ⭐ icon and review count
  - New rating form (rate.html) for clients to leave reviews

### UI/UX Improvements
- **Modern Design**: 
  - Beautiful gradient background (purple to blue)
  - Card-based layout for professional listings
  - Custom CSS with modern color scheme and shadows
  - Responsive design with Bootstrap 5
- **Home Page**:
  - Hero section with call-to-action buttons
  - Feature boxes showcasing platform benefits
  - Improved navigation with icons
- **Professional Cards**:
  - Grid layout (3 columns on desktop)
  - Hover effects with subtle animations
  - Clear rating badges with visual hierarchy
- **Default Data**:
  - 10 sample professionals with various locations
  - 3 test client accounts
  - Sample reviews and ratings
  - Available time slots for testing
  - Login credentials: client@example.com / demo123

## User Preferences
- Language: French (application interface)
- Database: SQLite (existing choice maintained)

## Notes
- The application uses Flask's development server in debug mode
- **Security Considerations for Production:**
  - Session secret key is currently hardcoded (should use environment variables)
  - Passwords are stored in plain text (should implement hashing with bcrypt or similar)
  - Flask development server is not suitable for production (use Gunicorn/Waitress instead)
