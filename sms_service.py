"""
Service SMS pour PRO CHEZ NOUS
Support Twilio pour vérification par SMS
"""

import os
import requests
import secrets
import sqlite3
from datetime import datetime, timedelta
from base64 import b64encode

class SMSService:
    """Service pour envoyer des SMS via Twilio"""
    
    def __init__(self):
        self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID', '')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN', '')
        self.phone_number = os.environ.get('TWILIO_PHONE_NUMBER', '')
        self.base_url = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}"
    
    def send_verification_code(self, to_phone, code=None):
        """
        Envoie un code de vérification par SMS
        
        Args:
            to_phone (str): Numéro de téléphone (format +228...)
            code (str): Code à envoyer (généré si None)
        
        Returns:
            dict: Résultat avec le code envoyé
        """
        if not code:
            code = self.generate_verification_code()
        
        message = f"PRO CHEZ NOUS - Votre code de vérification est: {code}\n\nCe code expire dans 10 minutes."
        
        result = self.send_sms(to_phone, message)
        
        if result['success']:
            result['code'] = code
        
        return result
    
    def send_sms(self, to_phone, message):
        """
        Envoie un SMS via Twilio
        
        Args:
            to_phone (str): Numéro destinataire
            message (str): Contenu du message
        
        Returns:
            dict: Résultat de l'envoi
        """
        if not self.is_configured():
            return {
                'success': False,
                'error': 'Twilio non configuré. Définissez TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN et TWILIO_PHONE_NUMBER'
            }
        
        try:
            url = f"{self.base_url}/Messages.json"
            
            # Authentification Basic Auth
            credentials = f"{self.account_sid}:{self.auth_token}"
            auth_header = b64encode(credentials.encode()).decode()
            
            headers = {
                "Authorization": f"Basic {auth_header}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            
            data = {
                "From": self.phone_number,
                "To": to_phone,
                "Body": message
            }
            
            response = requests.post(url, headers=headers, data=data)
            
            if response.status_code in [200, 201]:
                return {
                    'success': True,
                    'message_sid': response.json().get('sid')
                }
            else:
                return {
                    'success': False,
                    'error': f"Erreur Twilio: {response.status_code} - {response.text}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    @staticmethod
    def generate_verification_code(length=6):
        """Génère un code de vérification numérique"""
        return ''.join([str(secrets.randbelow(10)) for _ in range(length)])
    
    @staticmethod
    def store_verification_code(phone, code, db_path='database.db'):
        """Stocke un code de vérification dans la base"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Créer la table si nécessaire
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sms_verifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone TEXT NOT NULL,
                code TEXT NOT NULL,
                expiration TEXT NOT NULL,
                used INTEGER DEFAULT 0
            )
        ''')
        
        expiration = (datetime.now() + timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO sms_verifications (phone, code, expiration, used)
            VALUES (?, ?, ?, 0)
        ''', (phone, code, expiration))
        
        conn.commit()
        conn.close()
    
    @staticmethod
    def verify_code(phone, code, db_path='database.db'):
        """
        Vérifie un code de vérification
        
        Returns:
            bool: True si code valide
        """
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM sms_verifications 
            WHERE phone = ? AND code = ? AND used = 0
            ORDER BY id DESC LIMIT 1
        ''', (phone, code))
        
        verification = cursor.fetchone()
        
        if not verification:
            conn.close()
            return False
        
        expiration = datetime.strptime(verification[3], '%Y-%m-%d %H:%M:%S')
        
        if datetime.now() > expiration:
            conn.close()
            return False
        
        # Marquer comme utilisé
        cursor.execute('''
            UPDATE sms_verifications SET used = 1 WHERE id = ?
        ''', (verification[0],))
        
        conn.commit()
        conn.close()
        
        return True
    
    def is_configured(self):
        """Vérifie si le service SMS est configuré"""
        return bool(self.account_sid and self.auth_token and self.phone_number)


# Instance globale
sms_service = SMSService()


# Tests
if __name__ == '__main__':
    print("📱 Test du service SMS")
    service = SMSService()
    print(f"Configuré: {service.is_configured()}")
    
    # Test de génération de code
    code = service.generate_verification_code()
    print(f"Code généré: {code}")
    
    if not service.is_configured():
        print("\n⚠️  Twilio n'est pas configuré.")
        print("Définissez les variables d'environnement:")
        print("  - TWILIO_ACCOUNT_SID")
        print("  - TWILIO_AUTH_TOKEN")
        print("  - TWILIO_PHONE_NUMBER")
