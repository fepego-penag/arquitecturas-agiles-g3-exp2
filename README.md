# Experimento II: Seguridad 

## Dependencias
  * Docker
  * python 3.9
  * venv

## Como ejecutar el programa
* Descargar el codigo fuente
* Navegar hasta la carpeta root y ejecutar los siguentes comandos
<br> <code>docker-compose build</code>
<br> <code>docker-compose up</code>

Para ejecutar las pruebas luego de haber iniciado el programa
<br> <code>python script_pruebas.py</code>

## URL para consumo de servicios
Consumo microservicio Historia Clinica
localhost:5000/historia_clinica/<Any integer>

Consumo microservicio Modulo financiero
localhost:5000/reportes/<Any integer>

Obtener JWT o token de acceso
localhost:5000/jwt
