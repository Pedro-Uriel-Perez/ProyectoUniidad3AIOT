# Guía de Instalación

Esta guía detalla el proceso completo para instalar y configurar el sistema de control automático en tu ESP32.

## Requisitos previos

- ESP32 (cualquier modelo)
- Sensor DHT22
- Sensor MQ-135
- 3 relés (para ventilador, humidificador y calefacción)
- Cable micro-USB para programación
- Software Thonny IDE (recomendado) o similar para programar el ESP32

## Paso 1: Preparar el ESP32

1. **Instalar MicroPython**:
   
   Si tu ESP32 aún no tiene MicroPython, sigue estos pasos:
   
   - Descarga el firmware más reciente de MicroPython para ESP32 desde [micropython.org/download/esp32](https://micropython.org/download/esp32/)
   - Instala esptool para flashear el firmware:
     ```
     pip install esptool
     ```
   - Conecta tu ESP32 y flashea MicroPython:
     ```
     esptool.py --port [PUERTO_COM] erase_flash
     esptool.py --port [PUERTO_COM] --baud 460800 write_flash -z 0x1000 [ARCHIVO_MICROPYTHON.bin]
     ```
     Reemplaza [PUERTO_COM] con tu puerto (ej: COM3 en Windows o /dev/ttyUSB0 en Linux)

## Paso 2: Preparar los archivos

1. **Crear la estructura de directorios**:
   
   Necesitarás crear un directorio llamado `umqtt` en tu ESP32 para la biblioteca MQTT.

   En Thonny IDE:
   - Conéctate a tu ESP32
   - Ejecuta el siguiente código para crear el directorio:
     ```python
     import os
     try:
         os.mkdir('umqtt')
     except OSError:
         pass  # El directorio ya existe
     ```

2. **Subir los archivos**:
   
   Debes subir dos archivos a tu ESP32:
   
   - `main.py` -> Subir a la raíz del ESP32
   - `simple.py` -> Subir al directorio `umqtt` del ESP32

   En Thonny IDE:
   - Crea un nuevo archivo, copia el contenido de `main.py` y guárdalo como `main.py` en el ESP32
   - Crea otro archivo, copia el contenido de `simple.py` y guárdalo como `simple.py` en la carpeta `umqtt` del ESP32

## Paso 3: Configurar el código

1. **Editar credenciales y parámetros**:
   
   Abre `main.py` en tu editor y modifica:
   
   ```python
   # Configuración WiFi
   WIFI_SSID = "TU_SSID"              # Cambia a tu nombre de red WiFi
   WIFI_PASSWORD = "TU_PASSWORD"      # Cambia a tu contraseña WiFi
   
   # Configuración MQTT
   MQTT_CLIENT_ID = "esp32_control"   # Puedes dejarlo así o personalizarlo
   MQTT_TOPIC = "tu_tema/alertas"     # Cambia a un tema único para tus notificaciones
   ```
   
   Opcionalmente, ajusta los umbrales según tus necesidades:
   
   ```python
   TEMP_UMBRAL_ALTO = 20.0   # Ajusta según sea necesario
   TEMP_UMBRAL_BAJO = 40.0   # Ajusta según sea necesario
   HUM_UMBRAL = 50.0         # Ajusta según sea necesario
   AIR_UMBRAL = 1200         # Ajusta según sea necesario
   ```

## Paso 4: Conexiones físicas

1. **Conectar el sensor DHT22**:
   - VCC → 3.3V del ESP32
   - GND → GND del ESP32
   - DATA → GPIO4 del ESP32
   - Añade resistencia pull-up de 10kΩ entre VCC y DATA

2. **Conectar el sensor MQ-135**:
   - VCC → 5V del ESP32 (el sensor necesita 5V para funcionar correctamente)
   - GND → GND del ESP32
   - AOUT → GPIO34 del ESP32

3. **Conectar los relés**:
   - Relé 1: IN → GPIO21 del ESP32
   - Relé 2: IN → GPIO22 del ESP32
   - Relé 3: IN → GPIO23 del ESP32
   - VCC → 5V o 3.3V del ESP32 (según el módulo de relé)
   - GND → GND del ESP32

## Paso 5: Pruebas y verificación

1. **Reiniciar el ESP32**:
   - Presiona el botón de reset en el ESP32 o desconecta y vuelve a conectar la alimentación
   - El programa comenzará a ejecutarse automáticamente

2. **Verificar funcionamiento**:
   - Observa la salida en la consola serie (115200 baud)
   - Deberías ver mensajes como:
     ```
     Conectando a WiFi...
     Conectado a WiFi
     Dirección IP: 192.168.x.x
     Sistema de control automático de temperatura, humedad y calidad del aire
     ```

3. **Verificar las notificaciones MQTT**:
   - Configura un cliente MQTT como se indica en la guía correspondiente
   - Suscríbete al tema configurado en tu código
   - Prueba forzando la activación de algún relé (p.ej. acercando un objeto caliente al sensor DHT22)
   - Deberías recibir notificaciones cuando cambie el estado de los relés

## Solución de problemas

1. **Errores de importación**:
   - Si aparece `ImportError: no module named 'umqtt.simple'`, verifica que el archivo `simple.py` esté correctamente ubicado en la carpeta `umqtt`
   
2. **Problemas de conexión WiFi**:
   - Verifica las credenciales WiFi
   - Asegúrate de que el ESP32 esté dentro del alcance de tu router

3. **Errores de lectura de sensores**:
   - Verifica conexiones físicas
   - Para el DHT22, asegúrate de tener una resistencia pull-up adecuada

4. **Problemas con MQTT**:
   - Si ves errores de conexión MQTT, verifica que tengas acceso a Internet
   - El broker público puede estar ocasionalmente sobrecargado, espera y reintenta

## Calibración del sensor MQ-135

El sensor MQ-135 puede requerir calibración:

1. Coloca el sensor en un ambiente de aire limpio
2. Deja que se caliente durante 24-48 horas
3. Monitorea los valores y ajusta `AIR_UMBRAL` según sea necesario
4. Típicamente, valores por encima de 1000-1500 indican mala calidad del aire

## Mantenimiento

- Realiza limpiezas periódicas de los sensores para evitar lecturas erróneas
- Verifica regularmente las conexiones físicas
- Considera actualizar el firmware MicroPython anualmente

## Avanzado: Configuración de arranque

Para asegurar que el programa se inicie automáticamente:

1. El archivo `main.py` se ejecuta automáticamente al enc
