"""
Utilitaires pour PRO CHEZ NOUS
Fonctions de normalisation et validation
"""

import re

# Codes pays pour l'Afrique de l'Ouest
COUNTRY_CODES = {
    'tg': '+228',  # Togo
    'bj': '+229',  # Bénin
    'bf': '+226',  # Burkina Faso
    'ci': '+225',  # Côte d'Ivoire
    'sn': '+221',  # Sénégal
    'ml': '+223',  # Mali
    'ne': '+227',  # Niger
    'gn': '+224',  # Guinée
    'gh': '+233',  # Ghana
    'ng': '+234',  # Nigeria
}

def normalize_phone_number(phone):
    """
    Normalise un numéro de téléphone au format international.
    
    Formats acceptés :
    - +228XXXXXXXX
    - 228XXXXXXXX
    - 00228XXXXXXXX
    - 90XXXXXX (Togo local)
    
    Returns:
        str: Numéro normalisé au format +CCXXXXXXXX ou None si invalide
    
    Examples:
        >>> normalize_phone_number('+22890123456')
        '+22890123456'
        >>> normalize_phone_number('22890123456')
        '+22890123456'
        >>> normalize_phone_number('0022890123456')
        '+22890123456'
        >>> normalize_phone_number('90123456')
        '+22890123456'
    """
    if not phone:
        return None
    
    # Nettoyer le numéro (enlever espaces, tirets, points)
    phone = re.sub(r'[\s\-\.\(\)]', '', phone.strip())
    
    # Cas 1 : Déjà au format international +XXX
    if phone.startswith('+'):
        # Vérifier que le code pays existe
        for code in COUNTRY_CODES.values():
            if phone.startswith(code):
                return phone
        return phone  # Retourner tel quel si code pays non reconnu
    
    # Cas 2 : Format 00XXX (préfixe international)
    if phone.startswith('00'):
        return '+' + phone[2:]
    
    # Cas 3 : Format CCXXXXXXXX (sans +)
    for code in COUNTRY_CODES.values():
        code_without_plus = code[1:]  # Enlever le +
        if phone.startswith(code_without_plus):
            return '+' + phone
    
    # Cas 4 : Numéro local (ex: 90123456 pour Togo)
    # Par défaut, on assume que c'est un numéro togolais si 8 chiffres
    if len(phone) == 8 and phone.isdigit():
        return '+228' + phone
    
    # Si rien ne correspond, retourner le numéro tel quel
    return phone if phone else None


def validate_phone_number(phone):
    """
    Valide qu'un numéro de téléphone est au bon format.
    
    Args:
        phone (str): Numéro à valider
    
    Returns:
        bool: True si valide, False sinon
    """
    if not phone:
        return False
    
    normalized = normalize_phone_number(phone)
    
    # Vérifier format de base : +XXX suivi de 8-10 chiffres
    if normalized and re.match(r'^\+\d{10,13}$', normalized):
        return True
    
    return False


def get_country_from_phone(phone):
    """
    Détermine le pays à partir d'un numéro de téléphone.
    
    Args:
        phone (str): Numéro de téléphone
    
    Returns:
        str: Code pays (ex: 'tg', 'bj') ou None
    """
    normalized = normalize_phone_number(phone)
    
    if not normalized:
        return None
    
    for country, code in COUNTRY_CODES.items():
        if normalized.startswith(code):
            return country
    
    return None


def format_phone_display(phone):
    """
    Formate un numéro pour affichage (avec espaces).
    
    Args:
        phone (str): Numéro normalisé
    
    Returns:
        str: Numéro formaté pour affichage
    
    Example:
        >>> format_phone_display('+22890123456')
        '+228 90 12 34 56'
    """
    if not phone:
        return ''
    
    normalized = normalize_phone_number(phone)
    
    if not normalized:
        return phone
    
    # Format : +228 90 12 34 56
    if normalized.startswith('+228'):  # Togo
        return f"{normalized[:4]} {normalized[4:6]} {normalized[6:8]} {normalized[8:10]} {normalized[10:]}"
    elif normalized.startswith('+229'):  # Bénin
        return f"{normalized[:4]} {normalized[4:6]} {normalized[6:8]} {normalized[8:10]} {normalized[10:]}"
    else:
        # Format générique
        return f"{normalized[:4]} {normalized[4:]}"


# Tests unitaires
if __name__ == '__main__':
    print("🧪 Tests de normalisation de numéros")
    
    test_numbers = [
        '+22890123456',
        '22890123456',
        '0022890123456',
        '90123456',
        '+229 91 23 45 67',
        '229-91-23-45-67',
        '00229 91234567',
    ]
    
    for num in test_numbers:
        normalized = normalize_phone_number(num)
        is_valid = validate_phone_number(num)
        country = get_country_from_phone(num)
        formatted = format_phone_display(num)
        
        print(f"\nOriginal:    {num}")
        print(f"Normalisé:   {normalized}")
        print(f"Valide:      {is_valid}")
        print(f"Pays:        {country}")
        print(f"Affichage:   {formatted}")
