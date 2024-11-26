import re

def validate_password(password):
    
    # Regla 1: Longitud mínima de 8 caracteres
    if len(password) < 8:
        return False

    # Regla 2: Al menos una letra mayúscula
    if not re.search(r'[A-Z]', password):
        return False

    # Regla 3: Al menos una letra minúscula
    if not re.search(r'[a-z]', password):
        return False

    # Regla 4: Al menos un número
    if not re.search(r'[0-9]', password):
        return False

    # Regla 5: Al menos un carácter especial (!@#$%^&*)
    if not re.search(r'[!@#$%^&*]', password):
        return False

    # Si cumple todas las reglas
    return True
