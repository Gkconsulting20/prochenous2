# PRO CHEZ NOUS

## Overview
PRO CHEZ NOUS is a French professional appointment booking platform designed for manual trades (métiers manuels). It connects clients with skilled tradespeople, enabling them to find, book, and manage appointments based on location, professional category, ratings, and availability. The platform aims to streamline the booking process for both clients and professionals, offering a freemium model with enhanced features for premium subscribers.

**Pricing:** 5000 FCFA/month for Premium plan
**Payment Methods:** T-Money (Togocel) and Flooz (Moov Africa)

## User Preferences
- Language: French (application interface)
- Database: SQLite (existing choice maintained)

## System Architecture

### Technology Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML templates with Jinja2, Custom CSS
- **Deployment**: Configured for Replit autoscale deployment, designed for production with Gunicorn.

### Core Design Decisions
- **UI/UX**: Modern, responsive design with a RED theme, card-based layouts, and custom logos. Features intuitive dashboards for both clients and professionals.
- **Security**: Robust security measures including bcrypt password hashing, environment variable for secret key, and comprehensive form validation.
- **Freemium Model**: Implements a "gratuit" and "premium" subscription system (5000 FCFA/month), gating advanced features like internal messaging, favorites, enriched profiles, advanced statistics, and geolocation. Payment via T-Money or Flooz.
- **Geolocation**: Premium-only feature utilizing HTML5 Geolocation API, Haversine formula for distance calculation, and sorting professionals by proximity.
- **Professional Verification**: System for professionals to upload verification documents, with statuses and a "✓ Vérifié" badge for verified profiles.
- **Scalability**: Designed with a clear project structure and plans for production-grade WSGI server (Gunicorn).

### Feature Specifications
- **User Management**: Secure registration and authentication for both clients and professionals.
- **Professional Discovery**: Browsing, advanced search, and filtering by name, city, category, and minimum rating. Professionals are sorted by rating by default, and by proximity for premium users.
- **Appointment Management**: Professionals manage time slots, clients book and cancel appointments, with automatic slot restoration.
- **Rating System**: Clients can rate and review professionals.
- **Dashboards**: Interactive dashboards for both user types displaying appointments, statistics (for premium professionals), and quick actions.
- **Internal Messaging (Premium)**: Private communication between clients and professionals.
- **Favorites System (Premium)**: Clients can save preferred professionals.
- **Enriched Professional Profiles (Premium)**: Detailed profiles with descriptions, rates, experience, certifications, and photo galleries.
- **Advanced Statistics (Premium)**: For professionals, includes profile views, booking analytics, and revenue tracking.
- **Subscription Management**: Easy upgrade path to premium.

### Database Schema Highlights
- `users`: Stores user data, role, location, plan, verification status, and GPS coordinates.
- `slots`, `rendezvous`: Manages available and booked appointments.
- `avis`: Stores client ratings and reviews.
- `profils_pro`: Extends professional profiles for premium users.
- `messages`, `favoris`: Supports premium messaging and favorites features.
- `documents_verification`: Manages professional verification documents.

### Professional Categories
The platform supports a wide range of manual trade categories (e.g., Plomberie, Électricité, Peinture, Menuiserie, Rénovation, Jardinage).

## External Dependencies
- **Flask**: Main web framework.
- **SQLite**: Database system.
- **Jinja2**: Templating engine.
- **Bcrypt**: For password hashing.
- **HTML5 Geolocation API**: Used for the premium geolocation feature.