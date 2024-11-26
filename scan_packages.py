from scan_packages import *

# Dependencias inseguras
insecure_packages = {
    "flask": "1.0.2",
    "django": "2.2",
    "requests": "2.19.1"
}

def escanear_dependencias(archivo_reqs):
    """
    Escanea un archivo requirements.txt en busca de dependencias con versiones inseguras.

    :param archivo_reqs: Nombre del archivo requirements.txt
    """
    try:
        with open(archivo_reqs, 'r') as archivo:
            dependencias_inseguras = []
            
            # Leer las dependencias del archivo
            for linea in archivo:
                linea = linea.strip() 
                if not linea or linea.startswith("#"):
                    continue

                # Separar el paquete y la versión
                if "==" in linea:
                    paquete, version = linea.split("==")
                else:
                    paquete, version = linea, None

                # Verificar si está en la lista de inseguras
                if paquete in insecure_packages:
                    version_insegura = insecure_packages[paquete]
                    if version == version_insegura:
                        dependencias_inseguras.append((paquete, version))
            
            # Generar el reporte
            if dependencias_inseguras:
                print("⚠️ Dependencias inseguras encontradas:")
                for paquete, version in dependencias_inseguras:
                    print(f"- {paquete}=={version} está desactualizada e insegura.")
            else:
                print("✅ No se encontraron dependencias inseguras.")
    
    except FileNotFoundError:
        print(f"❌ El archivo {archivo_reqs} no se encontró.")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

archivo_reqs = "requirements.txt"

# Ejecutar el escaneo
escanear_dependencias(archivo_reqs)