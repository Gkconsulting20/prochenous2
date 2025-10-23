"""
Service FedaPay pour PRO CHEZ NOUS
Gestion des paiements T-Money, Flooz et autres mobile money
"""

import requests
import os
from datetime import datetime

class FedaPayService:
    """
    Service pour gérer les paiements via FedaPay
    Supports: T-Money (Togo), Flooz (Moov), MTN Mobile Money, etc.
    """
    
    def __init__(self):
        self.secret_key = os.environ.get('FEDAPAY_SECRET_KEY', '')
        self.public_key = os.environ.get('FEDAPAY_PUBLIC_KEY', '')
        self.environment = os.environ.get('FEDAPAY_ENV', 'sandbox')  # 'sandbox' or 'live'
        
        if self.environment == 'sandbox':
            self.base_url = 'https://sandbox-api.fedapay.com/v1'
            self.checkout_url = 'https://sandbox-checkout.fedapay.com'
        else:
            self.base_url = 'https://api.fedapay.com/v1'
            self.checkout_url = 'https://checkout.fedapay.com'
        
        self.headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'Content-Type': 'application/json'
        }
    
    def create_transaction(self, user_data, amount=5000, description="Abonnement Premium PRO CHEZ NOUS", callback_url=None):
        """
        Crée une transaction FedaPay
        
        Args:
            user_data (dict): Données de l'utilisateur (name, email, phone)
            amount (int): Montant en centimes (5000 = 50.00 FCFA)
            description (str): Description de la transaction
        
        Returns:
            dict: Résultat avec transaction_id et payment_url
        """
        try:
            # Préparer les données de la transaction
            transaction_data = {
                "description": description,
                "amount": amount,
                "currency": {"iso": "XOF"},  # Franc CFA
                "callback_url": callback_url,
                "customer": {
                    "firstname": user_data.get('name', '').split()[0] if user_data.get('name') else "Client",
                    "lastname": user_data.get('name', '').split()[-1] if user_data.get('name') and len(user_data.get('name', '').split()) > 1 else "PCN",
                    "email": user_data.get('email', f"user{user_data.get('id')}@prochesnous.fr"),
                }
            }
            
            # Ajouter le téléphone si disponible
            if user_data.get('phone'):
                phone = user_data['phone']
                # Déterminer le pays à partir du préfixe
                country = 'tg'  # Par défaut Togo
                if phone.startswith('+228'):
                    country = 'tg'
                elif phone.startswith('+229'):
                    country = 'bj'
                elif phone.startswith('+226'):
                    country = 'bf'
                
                transaction_data['customer']['phone_number'] = {
                    "number": phone,
                    "country": country
                }
            
            # Créer la transaction
            response = requests.post(
                f"{self.base_url}/transactions",
                headers=self.headers,
                json=transaction_data
            )
            
            if response.status_code != 200 and response.status_code != 201:
                return {
                    'success': False,
                    'error': f"Erreur lors de la création de la transaction: {response.text}"
                }
            
            transaction = response.json()
            transaction_id = transaction['v1/transaction']['id']
            
            # Générer le token de paiement
            token_response = requests.post(
                f"{self.base_url}/transactions/{transaction_id}/token",
                headers=self.headers
            )
            
            if token_response.status_code != 200 and token_response.status_code != 201:
                return {
                    'success': False,
                    'error': f"Erreur lors de la génération du token: {token_response.text}"
                }
            
            token_data = token_response.json()
            payment_url = token_data['v1/token']['url']
            token = token_data['v1/token']['token']
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'payment_url': payment_url,
                'token': token
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_transaction(self, transaction_id):
        """
        Récupère les détails d'une transaction
        
        Args:
            transaction_id (int): ID de la transaction
        
        Returns:
            dict: Détails de la transaction
        """
        try:
            response = requests.get(
                f"{self.base_url}/transactions/{transaction_id}",
                headers=self.headers
            )
            
            if response.status_code != 200:
                return {
                    'success': False,
                    'error': f"Transaction non trouvée: {response.text}"
                }
            
            transaction = response.json()
            return {
                'success': True,
                'transaction': transaction['v1/transaction']
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def verify_webhook_signature(self, payload, signature):
        """
        Vérifie la signature d'un webhook FedaPay
        
        Args:
            payload (str): Corps de la requête
            signature (str): Signature envoyée par FedaPay
        
        Returns:
            bool: True si valide
        """
        if not signature or not self.secret_key:
            return False
        
        import hmac
        import hashlib
        
        try:
            expected_sig = hmac.new(
                self.secret_key.encode(),
                payload,
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature, expected_sig)
        except Exception:
            return False
    
    def is_configured(self):
        """
        Vérifie si FedaPay est configuré
        
        Returns:
            bool: True si configuré
        """
        return bool(self.secret_key and self.public_key)


# Instance globale du service
fedapay_service = FedaPayService()


# Tests
if __name__ == '__main__':
    print("🧪 Test du service FedaPay")
    
    service = FedaPayService()
    print(f"Environnement: {service.environment}")
    print(f"Base URL: {service.base_url}")
    print(f"Configuré: {service.is_configured()}")
    
    if service.is_configured():
        # Test de création de transaction
        user_data = {
            'id': 1,
            'name': 'Jean Dupont',
            'email': '[email protected]',
            'phone': '+22890123456'
        }
        
        result = service.create_transaction(user_data)
        if result['success']:
            print(f"\n✅ Transaction créée!")
            print(f"ID: {result['transaction_id']}")
            print(f"URL de paiement: {result['payment_url']}")
        else:
            print(f"\n❌ Erreur: {result['error']}")
    else:
        print("\n⚠️  FedaPay n'est pas configuré.")
        print("Définissez les variables d'environnement:")
        print("  - FEDAPAY_SECRET_KEY")
        print("  - FEDAPAY_PUBLIC_KEY")
        print("  - FEDAPAY_ENV (sandbox ou live)")
