from collections import Counter

# Función para analizar los logs
def analizar_logs(archivo_log):
    ip_counter = Counter()
    errores_404 = 0

    # Leer el archivo línea por línea
    try:
        with open(archivo_log, 'r') as archivo:
            for linea in archivo:
                partes = linea.split()
                if len(partes) < 9:
                    continue
                
                ip = partes[0]
                codigo_http = partes[-2]

                ip_counter[ip] += 1

                if codigo_http == "404":
                    errores_404 += 1

        # Obtener las 5 IPs más frecuentes
        top_5_ips = ip_counter.most_common(5)

        # Imprimir resultados
        print("Las 5 IPs más frecuentes:")
        for ip, cuenta in top_5_ips:
            print(f"{ip}: {cuenta} veces")
        
        print(f"\nTotal de errores 404: {errores_404}")

    except FileNotFoundError:
        print(f"El archivo {archivo_log} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo_log = "access.log"

# Llamar a la función de análisis
analizar_logs(archivo_log)