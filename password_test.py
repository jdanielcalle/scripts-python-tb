from validate_password_script import validate_password  # Importar la función del otro archivo

# Lista de contraseñas a validar
passwords = [
    "d4n189*s_sa",
    "123456789",
    "contraseña",
    "SOYDANIEL",
    "Parc3r0s",
    "t4l3nt0B@"
]

# Validamos cada contraseña
print("Pruebas de validación de contraseñas:")
for pwd in passwords:
    resultado = validate_password(pwd)
    print(f"'{pwd}': {'Fuerte' if resultado else 'Débil'}")
