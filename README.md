# Proyecto Aplicaciones de IoT
- **Alumnos:** 
## Miguel Angel Alvarez Ibarra
- **N.Control:**  12231004533
# Pedro Uriel Perez Monzon
- **N.Control:**  1223100428
# Zaida Fernada 
- **N.Control:**  1223458878
- **Grupo:** GDS0653
- **Materia:**  Aplicaciones de IoT
 
## 📋 Descripción del proyecto
Este proyecto implementa un sistema automático de monitoreo y control de ambiente utilizando ESP32, sensores de temperatura, humedad, sensor de calidad del aire y sensor de agua.
El sistema monitorea constantemente las condiciones ambientales y controla automáticamente los siguientes dispositivos:
- **Ventilador**: Se activa cuando la temperatura supera el umbral establecido o cuando la calidad del aire es deficiente
- **Humidificador**: Se activa cuando la humedad es baja
- **Sistema de calefacción (Lamparas de calor)**: Se activa cuando la temperatura es baja
- **Sistema de sonido (Buzzer)**: Se activa cuando el nivel de agua es bajo
- **Sistema de Alimentacion (Servomotor)**: Se abre cada cierto tiempo, para la alimentacion de los insectos  

## 🔧 Componentes
- **ESP32**: Microcontrolador principal
- **DHT22**: Sensor de temperatura y humedad
- **MQ-135**: Sensor de calidad del aire
- **Modulo de 4 Relevadores**: Para controlar ventilador, humidificador y sistema de calefacción

## 📊 Parámetros
| Parámetro | Valor predeterminado | Descripción |
|-----------|----------------------|-------------|
| TEMP_UMBRAL_ALTO | 20.0°C | Temperatura máxima antes de activar ventilación |
| TEMP_UMBRAL_BAJO | 40.0°C | Temperatura mínima antes de activar calefacción |
| HUM_UMBRAL | 50.0% | Humedad mínima antes de activar humidificador |
| AIR_UMBRAL | 1200 | Umbral de calidad de aire para ventilación |

## Evidencia de funcionamiento
# [Video](https://drive.google.com/drive/folders/1AQbpGpi7e0rlrNGNPIrpgBGgKlkwMyw0?usp=sharing)

![Imagen 1](https://github.com/user-attachments/assets/435de6a5-ac59-4ff5-bcae-536a2d2264bf)
![Imagen 2](https://github.com/user-attachments/assets/f3acc4ae-f941-4ffe-bffb-8c2f0a156e00)

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

## 🚀 Uso
El sistema inicia automáticamente al conectar el ESP32. La información del sistema se muestra a través del puerto serie:
- Lecturas de temperatura, humedad y calidad del aire
- Estado de los dispositivos controlados

## 🔄 Funcionamiento
El sistema sigue un ciclo simple de operación:
1. Lee los valores de los sensores
2. Compara con los umbrales establecidos
3. Activa/desactiva los dispositivos según sea necesario
4. Envía notificaciones cuando cambia el estado de un dispositivo
