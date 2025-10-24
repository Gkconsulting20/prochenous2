#!/usr/bin/env python3
"""
Script pour retirer les espaces des numéros de téléphone dans la base de données.
Les numéros doivent être stockés au format normalisé sans espaces : +22890881111
"""

import sqlite3
import re

def remove_phone_spaces():
    """Retire les espaces de tous les numéros de téléphone dans la base."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Récupérer tous les utilisateurs avec un numéro de téléphone
    cursor.execute('SELECT id, phone FROM users WHERE phone IS NOT NULL')
    users = cursor.fetchall()
    
    print(f"📱 Trouvé {len(users)} utilisateurs avec numéro de téléphone")
    print("\n🔧 Normalisation en cours...\n")
    
    updated_count = 0
    for user_id, phone in users:
        # Retirer tous les espaces, tirets, points, parenthèses
        normalized = re.sub(r'[\s\-\.\(\)]', '', phone.strip())
        
        if normalized != phone:
            print(f"  ✓ ID {user_id}: {phone} → {normalized}")
            cursor.execute('UPDATE users SET phone = ? WHERE id = ?', (normalized, user_id))
            updated_count += 1
        else:
            print(f"  ○ ID {user_id}: {phone} (déjà normalisé)")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Terminé ! {updated_count} numéros mis à jour")
    print("\n🎯 Maintenant vous pouvez vous connecter avec:")
    print("   - 90881111")
    print("   - 90 88 11 11")
    print("   - +22890881111")
    print("   - +228 90 88 11 11")
    print("\nTous ces formats fonctionneront ! 🚀")

if __name__ == '__main__':
    remove_phone_spaces()
