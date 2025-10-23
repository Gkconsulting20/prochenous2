"""
Service d'envoi d'emails pour PRO CHEZ NOUS
Support SendGrid et configuration flexible
"""

import os
import requests

class EmailService:
    """Service pour envoyer des emails via SendGrid"""
    
    def __init__(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY', '')
        self.from_email = os.environ.get('FROM_EMAIL', '[email protected]')
        self.from_name = os.environ.get('FROM_NAME', 'PRO CHEZ NOUS')
    
    def send_password_reset_email(self, to_email, reset_url, user_name):
        """
        Envoie un email de réinitialisation de mot de passe
        
        Args:
            to_email (str): Email du destinataire
            reset_url (str): URL de réinitialisation
            user_name (str): Nom de l'utilisateur
        
        Returns:
            dict: Résultat de l'envoi
        """
        subject = "🔐 Réinitialisez votre mot de passe - PRO CHEZ NOUS"
        
        html_content = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background: #dc3545; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 30px; background: #f8f9fa; }}
                .button {{ 
                    display: inline-block; 
                    padding: 12px 30px; 
                    background: #dc3545; 
                    color: white !important; 
                    text-decoration: none; 
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🔧 PRO CHEZ NOUS</h1>
                </div>
                <div class="content">
                    <h2>Bonjour {user_name},</h2>
                    <p>Vous avez demandé à réinitialiser votre mot de passe.</p>
                    <p>Cliquez sur le bouton ci-dessous pour créer un nouveau mot de passe :</p>
                    <p style="text-align: center;">
                        <a href="{reset_url}" class="button">Réinitialiser mon mot de passe</a>
                    </p>
                    <p><small>Ou copiez ce lien dans votre navigateur :<br>{reset_url}</small></p>
                    <p><strong>⏰ Ce lien expire dans 1 heure.</strong></p>
                    <p>Si vous n'avez pas demandé cette réinitialisation, ignorez cet email.</p>
                </div>
                <div class="footer">
                    <p>© 2024 PRO CHEZ NOUS - Plateforme de réservation de professionnels</p>
                    <p>Togo • Bénin • Burkina Faso</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        Bonjour {user_name},
        
        Vous avez demandé à réinitialiser votre mot de passe PRO CHEZ NOUS.
        
        Cliquez sur ce lien pour créer un nouveau mot de passe :
        {reset_url}
        
        ⏰ Ce lien expire dans 1 heure.
        
        Si vous n'avez pas demandé cette réinitialisation, ignorez cet email.
        
        ---
        PRO CHEZ NOUS
        Plateforme de réservation de professionnels
        Togo • Bénin • Burkina Faso
        """
        
        return self.send_email(to_email, subject, html_content, text_content)
    
    def send_email(self, to_email, subject, html_content, text_content=""):
        """
        Envoie un email via SendGrid
        
        Args:
            to_email (str): Email du destinataire
            subject (str): Sujet de l'email
            html_content (str): Contenu HTML
            text_content (str): Contenu texte (fallback)
        
        Returns:
            dict: Résultat de l'envoi
        """
        if not self.sendgrid_api_key:
            return {
                'success': False,
                'error': 'SendGrid non configuré. Définissez SENDGRID_API_KEY'
            }
        
        try:
            url = "https://api.sendgrid.com/v3/mail/send"
            
            headers = {
                "Authorization": f"Bearer {self.sendgrid_api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "personalizations": [{
                    "to": [{"email": to_email}],
                    "subject": subject
                }],
                "from": {
                    "email": self.from_email,
                    "name": self.from_name
                },
                "content": [
                    {"type": "text/plain", "value": text_content or subject},
                    {"type": "text/html", "value": html_content}
                ]
            }
            
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code in [200, 201, 202]:
                return {'success': True}
            else:
                return {
                    'success': False,
                    'error': f"Erreur SendGrid: {response.status_code} - {response.text}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def is_configured(self):
        """Vérifie si le service email est configuré"""
        return bool(self.sendgrid_api_key)


# Instance globale
email_service = EmailService()


# Tests
if __name__ == '__main__':
    print("📧 Test du service email")
    service = EmailService()
    print(f"Configuré: {service.is_configured()}")
    
    if not service.is_configured():
        print("\n⚠️  SendGrid n'est pas configuré.")
        print("Définissez les variables d'environnement:")
        print("  - SENDGRID_API_KEY")
        print("  - FROM_EMAIL (optionnel)")
        print("  - FROM_NAME (optionnel)")
