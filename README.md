# Sistema de Control Ambiental con ESP32

Este proyecto implementa un sistema automático de monitoreo y control de ambiente utilizando un ESP32, sensores de temperatura, humedad y calidad del aire, y un sistema de notificaciones MQTT.

## 📋 Descripción

El sistema monitorea constantemente las condiciones ambientales y controla automáticamente los siguientes dispositivos:

- **Ventilador**: Se activa cuando la temperatura supera el umbral establecido o cuando la calidad del aire es deficiente
- **Humidificador**: Se activa cuando la humedad es baja
- **Sistema de calefacción**: Se activa cuando la temperatura es baja

Cada vez que un dispositivo se enciende o apaga, el sistema envía una notificación detallada a través de MQTT.

## 🔧 Componentes

- **ESP32**: Microcontrolador principal
- **DHT22**: Sensor de temperatura y humedad
- **MQ-135**: Sensor de calidad del aire
- **Relés (x3)**: Para controlar ventilador, humidificador y sistema de calefacción

## 📊 Parámetros configurables

| Parámetro | Valor predeterminado | Descripción |
|-----------|----------------------|-------------|
| TEMP_UMBRAL_ALTO | 20.0°C | Temperatura máxima antes de activar ventilación |
| TEMP_UMBRAL_BAJO | 40.0°C | Temperatura mínima antes de activar calefacción |
| HUM_UMBRAL | 50.0% | Humedad mínima antes de activar humidificador |
| AIR_UMBRAL | 1200 | Umbral de calidad de aire para ventilación |

## 🔌 Conexiones

| Componente | Pin ESP32 |
|------------|-----------|
| DHT22 | GPIO4 |
| Relé ventilador | GPIO21 |
| Relé humidificador | GPIO22 |
| Relé calefacción | GPIO23 |
| MQ-135 | GPIO34 (ADC) |

## Evidencia 

## Evidencia

![Descripción de la imagen 1](https://github.com/user-attachments/assets/435de6a5-ac59-4ff5-bcae-536a2d2264bf)
![Descripción de la imagen 2](https://github.com/user-attachments/assets/f3acc4ae-f941-4ffe-bffb-8c2f0a156e00)



## 📡 Sistema de notificaciones MQTT

El sistema utiliza el protocolo MQTT para enviar notificaciones en tiempo real cuando cambia el estado de cualquier dispositivo. 

### Configuración MQTT
- **Broker**: broker.hivemq.com (público)
- **Puerto**: 1883
- **Tema (Topic)**: criadero/alertas
- **Cliente ID**: esp32_control

### Cómo recibir las notificaciones
Para ver las notificaciones, puedes usar cualquier cliente MQTT:

1. Instala una aplicación cliente MQTT (MQTT Explorer, MQTT Dashboard, etc.)
2. Conéctala al broker: broker.hivemq.com:1883
3. Suscríbete al tema: criadero/alertas

## 📁 Estructura del proyecto

- **main.py**: Programa principal
- **umqtt/simple.py**: Biblioteca MQTT para MicroPython

## ⚙️ Instalación

1. Crea la carpeta `umqtt` en tu ESP32
2. Copia el archivo `simple.py` dentro de la carpeta `umqtt`
3. Copia el archivo `main.py` en la raíz del ESP32

## 🚀 Uso

El sistema inicia automáticamente al conectar el ESP32. La información del sistema se muestra a través del puerto serie:

- Lecturas de temperatura, humedad y calidad del aire
- Estado de los dispositivos controlados
- Información de conexión WiFi y MQTT

## 🔄 Funcionamiento

El sistema sigue un ciclo simple de operación:

1. Lee los valores de los sensores
2. Compara con los umbrales establecidos
3. Activa/desactiva los dispositivos según sea necesario
4. Envía notificaciones cuando cambia el estado de un dispositivo
5. Espera 3 segundos y repite

## 📝 Notas

- El sensor DHT22 requiere al menos 2 segundos entre lecturas
- Los relés en este sistema funcionan con lógica invertida (1 = apagado, 0 = encendido)
- El sistema reconecta automáticamente WiFi y MQTT si se pierde la conexión

## 🔒 Seguridad

Este proyecto utiliza un broker MQTT público para demostración. Para un entorno de producción, considere usar un broker privado con autenticación.
