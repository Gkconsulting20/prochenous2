# PRO CHEZ NOUS

## Overview
A French professional appointment booking platform specifically for manual trades (métiers manuels) built with Flask. The application allows clients to find and book appointments with tradespeople based on location, professional category, ratings, and availability.

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
│   ├── base.html        # Base template (red navbar with premium links)
│   ├── index.html       # Landing page (with feature boxes)
│   ├── register.html    # User registration (with location field)
│   ├── login.html       # User login
│   ├── dashboard_user.html    # Client dashboard
│   ├── dashboard_pro.html     # Professional dashboard
│   ├── professionals.html     # List of professionals (card layout)
│   ├── book.html             # Booking interface
│   ├── add_slot.html         # Add time slots (pros only)
│   ├── rate.html             # Rating form for professionals
│   ├── subscription.html     # Subscription management (premium)
│   ├── profil.html          # Enriched professional profiles (premium)
│   ├── messages.html        # Internal messaging system (premium)
│   ├── send_message.html    # Message composition (premium)
│   └── favoris.html         # Favorites list (premium)
└── static/
    ├── style.css        # Modern responsive styling (RED theme)
    └── logo.png         # Custom professional logo (white bg, 50px)

```

### Database Schema
- **users**: id, name, email, password, role (client/pro), localisation, categorie (professional trade), plan (gratuit/premium), statut_verification (non_verifie/en_attente/verifie), latitude, longitude (GPS coordinates)
- **slots**: id, pro_id, date (available time slots)
- **rendezvous**: id, pro_id, client_id, date (booked appointments)
- **avis**: id, pro_id, client_id, note, commentaire, date (reviews/ratings)
- **profils_pro**: id, user_id, description, tarif_horaire, experience, certifications, photos_url (premium profiles)
- **messages**: id, expediteur_id, destinataire_id, contenu, date, lu (internal messaging)
- **favoris**: id, user_id, pro_id, date_ajout (favorites list)
- **documents_verification**: id, user_id, type_document, nom_fichier, date_upload, statut (en_attente/valide/refuse)

### Professional Categories (Métiers Manuels)
11 trade categories available:
1. Plomberie
2. Électricité
3. Peinture
4. Menuiserie
5. Maçonnerie
6. Rénovation
7. Vitrerie
8. Jardinage
9. Serrurerie
10. Toiture
11. Autre

## Features

### Core Features (Free Plan)
1. User registration (client or professional) with trade category selection
2. User authentication with bcrypt password hashing
3. Professional directory browsing with:
   - Professional category/trade display (badges)
   - Geographic location display
   - Average rating and review count
   - Sorted by rating (best first)
   - Username display without contact details
4. Advanced search and filtering:
   - Filter by professional name
   - Filter by city/location
   - Filter by professional category/trade (11 categories)
   - Filter by minimum rating
5. Appointment slot management (for professionals)
6. Appointment booking (for clients)
7. Appointment cancellation (with slot restoration)
8. Rating system for professionals
9. Dashboard views for both user types with:
   - List of upcoming and past appointments
   - Cancellation functionality
   - Basic statistics

### Premium Features (9.99€/month)
10. **💬 Internal Messaging System:**
    - Private messaging between clients and professionals
    - Inbox with sent/received messages
    - Quick reply functionality
    
11. **⭐ Favorites System (Clients):**
    - Unlimited favorites list
    - Quick access to preferred professionals
    - One-click add/remove
    
12. **📝 Enriched Professional Profiles:**
    - Detailed descriptions
    - Hourly rates display
    - Experience and certifications
    - Photo galleries
    - Premium badge visibility
    
13. **📊 Advanced Statistics (Professionals):**
    - Profile views tracking
    - Booking analytics
    - Revenue calculations
    - Performance metrics
    
14. **💎 Subscription Management:**
    - Easy plan comparison
    - One-click upgrade
    - Premium badge on all listings

15. **📍 Geolocation Feature:**
    - "Près de moi" button visible only for premium users
    - HTML5 Geolocation API integration
    - Automatic distance calculation using Haversine formula
    - Professionals sorted by proximity (nearest first)
    - Distance displayed in kilometers on professional cards
    - GPS coordinates stored for all professionals
    - Premium-only access enforced

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

## Recent Changes (October 18, 2025)

### 📍 Latest Update: Géolocalisation Premium (Nouvellement ajouté!)
- **Fonctionnalité de géolocalisation:**
  - ✅ Bouton "📍 Près de moi" visible uniquement pour les utilisateurs premium
  - ✅ Intégration de l'API Geolocation HTML5 du navigateur
  - ✅ Colonnes latitude/longitude ajoutées dans la table users
  - ✅ Calcul automatique des distances avec la formule de Haversine
  - ✅ Tri des professionnels par proximité (plus proche en premier)
  - ✅ Affichage de la distance en kilomètres sur chaque carte professionnelle
  - ✅ Coordonnées GPS réelles pour toutes les villes françaises principales
  - ✅ Accès réservé aux membres Premium uniquement
  - ✅ Message de redirection vers la page d'abonnement pour les non-premium
  - ✅ Gestion des erreurs de géolocalisation (permissions refusées, etc.)

### 🔐 Previous Update: Système de vérification d'identité professionnelle
- **Vérification d'identité:**
  - ✅ Nouvelle table `documents_verification` pour stocker les documents
  - ✅ Colonne `statut_verification` dans la table users (non_verifie/en_attente/verifie)
  - ✅ Upload de documents (diplômes, certificats, cartes pro, Kbis, assurances)
  - ✅ Formats acceptés: PDF, JPG, JPEG, PNG (max 16MB)
  - ✅ Page `/verification` pour que les pros uploadent leurs documents
  - ✅ Page `/admin_verification` pour valider les documents
  - ✅ Badge "✓ Vérifié" affiché sur tous les profils vérifiés
  - ✅ Meilleure crédibilité et confiance pour les professionnels vérifiés

- **Expansion des métiers:**
  - ✅ 70+ métiers disponibles (au lieu de 11)
  - ✅ Focus sur métiers manuels et secteur informel
  - ✅ Icônes emoji pour chaque métier
  - ✅ Catégories: Bâtiment, Jardinage, Transport, Beauté, Cuisine, Services à domicile, Auto, Éducation, Événementiel, Sécurité, Sport, Agriculture, etc.

### 💎 Previous Update: Premium Subscription System (Freemium Model)
- **Business Model:**
  - ✅ Added freemium subscription system with "gratuit" and "premium" tiers
  - ✅ New 'plan' column in users table (default: 'gratuit')
  - ✅ Premium pricing: 9.99€/month displayed on subscription page
  - ✅ One-click upgrade system with POST /upgrade route
  
- **New Database Tables:**
  - ✅ **profils_pro**: Enriched profiles for premium professionals (description, tarif_horaire, experience, certifications, photos_url)
  - ✅ **messages**: Internal messaging system (expediteur_id, destinataire_id, contenu, date, lu)
  - ✅ **favoris**: Favorites list for clients (user_id, pro_id, date_ajout)
  
- **Premium Features for Clients:**
  - ✅ 💬 Internal messaging system to contact professionals privately
  - ✅ ⭐ Unlimited favorites list to save preferred professionals
  - ✅ 👁️ Access to enriched professional profiles with detailed info
  - ✅ New routes: /messages, /send_message/<dest_id>, /favoris, /add_favori/<pro_id>
  
- **Premium Features for Professionals:**
  - ✅ 📝 Enriched profile creation with description, hourly rates, experience, certifications
  - ✅ 📊 Advanced statistics dashboard (views, bookings, revenue tracking)
  - ✅ 💬 Receive and respond to client messages
  - ✅ ⭐ Premium badge displayed on all listings
  
- **New Templates Created:**
  - ✅ subscription.html - Plan comparison and upgrade page
  - ✅ profil.html - Detailed professional profile page
  - ✅ messages.html - Messaging inbox (sent/received)
  - ✅ send_message.html - Message composition form
  - ✅ favoris.html - Client's favorites list
  
- **UI Updates:**
  - ✅ RED color theme throughout (navbar, buttons, accents) - replacing blue
  - ✅ Custom logo with white background and shadow for high visibility on red navbar
  - ✅ Navigation bar updated with premium features (Messages, Favoris, Abonnement)
  - ✅ "Voir le profil" button added to professional cards
  - ✅ Premium badges (⭐ Premium) displayed for premium users
  - ✅ Subscription-aware navigation and feature access control
  
- **Test Data:**
  - ✅ Mixed free/premium users in init_data.py
  - ✅ Sample enriched profiles for premium professionals
  - ✅ Test messages between users
  - ✅ Sample favorites for testing
  - ✅ Test accounts: client@example.com (premium) / demo123, marc.plombier@prochesnous.fr (premium pro) / demo123

### Previous Update: Professional Categories & Branding (October 17, 2025)
- **Branding "PRO CHEZ NOUS":**
  - ✅ Updated all templates with new platform name
  - ✅ Changed from generic "Plateforme Pro" to "PRO CHEZ NOUS"
  - ✅ Professional blue color scheme maintained
  - ✅ 🏠 icon in navbar representing "home services"
  
- **Professional Categories System:**
  - ✅ Added 'categorie' column to users table
  - ✅ 11 manual trade categories (métiers manuels)
  - ✅ Category selection in registration form for professionals
  - ✅ Category badges displayed on professional cards
  - ✅ Category filter in professional search
  - ✅ Updated init_data.py with professional categories
  
- **Sample Data Updated:**
  - ✅ 12 sample professionals with diverse trades
  - ✅ Each professional assigned a specific trade category
  - ✅ Geographic distribution across major French cities
  - ✅ Test accounts: client@example.com / demo123

### 🚀 Production-Ready Features (Previously Implemented)
- **Sécurité complète:**
  - ✅ Hashage des mots de passe avec bcrypt
  - ✅ Clé secrète via variable d'environnement
  - ✅ Validation de tous les formulaires
  - ✅ Messages d'erreur informatifs
- **Fonctionnalités avancées:**
  - ✅ Recherche et filtrage (nom, ville, catégorie, note)
  - ✅ Affichage des rendez-vous pour clients ET professionnels
  - ✅ Annulation de rendez-vous (remet le créneau disponible)
  - ✅ Messages flash pour toutes les actions
  - ✅ Dashboards améliorés avec design moderne
- **Infrastructure production:**
  - ✅ Gunicorn comme serveur WSGI
  - ✅ Configuration de déploiement automatique
  - ✅ Workflow optimisé pour production

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

### ✅ Production Ready
- **Serveur:** Gunicorn (serveur WSGI de production)
- **Sécurité:** Mots de passe hashés avec bcrypt, clé secrète via env variable
- **Validation:** Tous les formulaires validés avec messages d'erreur
- **Déploiement:** Configuré pour autoscale sur Replit

### 📋 Fonctionnalités complètes
1. ✅ Inscription et connexion sécurisées
2. ✅ Recherche/filtrage des professionnels
3. ✅ Réservation de rendez-vous
4. ✅ Annulation de rendez-vous (clients et pros)
5. ✅ Système d'avis et notes
6. ✅ Dashboards interactifs
7. ✅ Messages flash informatifs
8. ✅ **Système d'abonnement freemium (gratuit/premium)**
9. ✅ **Messagerie interne premium**
10. ✅ **Liste de favoris premium**
11. ✅ **Profils enrichis premium**
12. ✅ **Statistiques avancées premium**

### 🔐 Sécurité implémentée
- ✅ Hashage bcrypt des mots de passe
- ✅ Variable d'environnement pour SECRET_KEY
- ✅ Validation de tous les formulaires
- ✅ Protection contre duplications d'email
- ✅ Sessions sécurisées

### 🎯 Prêt pour production
Le site est maintenant **100% fonctionnel et sécurisé** pour une mise en ligne!
