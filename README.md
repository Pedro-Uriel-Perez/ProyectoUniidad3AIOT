

# Proyecto Aplicaciones de IoT
- **Alumnos:** 
# Miguel Angel Alvarez Ibarra
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

### ESP32  
<img src="https://github.com/user-attachments/assets/c650635a-9bcd-4f11-838e-982a7d413050" width="300" alt="ESP32">

- Microcontrolador principal que coordina todo el sistema.

---

### DHT22  
<img src="https://github.com/user-attachments/assets/14b93496-4a37-4430-bae8-318b63246710" width="300" alt="DHT22">

- Sensor de temperatura y humedad de alta precisión.  
- **Rango de medición:** -40°C a 80°C / 0–100% HR

---

### MQ-135  
<img src="https://github.com/user-attachments/assets/7a0789e5-94bd-4a2c-a86e-67c4970373ba" width="300" alt="MQ-135">

- Sensor de calidad del aire.  
- Detecta gases contaminantes como: NH₃, NOₓ, alcohol, benceno, humo, CO₂

---

### Módulo de 4 Relevadores  
<img src="https://github.com/user-attachments/assets/d79e6412-3b3f-487a-9762-34e76300d648" width="300" alt="Módulo Relevadores">

- Controla dispositivos de alto voltaje.  
- Permite activar/desactivar el ventilador, humidificador y sistema de calefacción.

---

## 🔌 Dispositivos Controlados

### Ventilador  
<img src="https://github.com/user-attachments/assets/4cdddb4a-fddc-4ac8-95db-80cf8e2975cc" width="300" alt="Ventilador">

- Se activa cuando la temperatura supera los **20.0 °C**.  
- También se enciende si la calidad del aire es deficiente (**>1200**).

---

### Humidificador  
<img src="https://github.com/user-attachments/assets/739b651a-f66f-4828-99cb-44cd5da8ad5e" width="300" alt="Humidificador">

- Se activa cuando la humedad cae por debajo del **50.0 %**.  
- Ayuda a mantener niveles óptimos de humedad.

---

### Sistema de Calefacción (Lámparas de Calor)  
<img src="https://github.com/user-attachments/assets/035732d0-7977-4c0e-8496-600e121bd5f4" width="300" alt="Lámparas de calor">

- Se activa cuando la temperatura baja de **40.0 °C**.  
- Mantiene la temperatura adecuada para los insectos.

---

### Sistema de Sonido (Buzzer)  
<img src="https://github.com/user-attachments/assets/a0d03c3a-7bc0-4b2d-8148-10f955d66a9d" width="300" alt="Buzzer">

- Emite una alarma sonora cuando el nivel de agua es bajo.  
- Alerta al usuario para rellenar el depósito.

---

### Sistema de Alimentación (Servomotor)  
<img src="https://github.com/user-attachments/assets/14fb29ce-42f9-4ffb-bcae-8b31ba5a93d5" width="300" alt="Servomotor">

- Se activa automáticamente según una programación establecida.  
- Libera alimento para los insectos en intervalos regulares.

---


## 📊 Parámetros
| Parámetro | Valor predeterminado | Descripción |
|-----------|----------------------|-------------|
| TEMP_UMBRAL_ALTO | 20.0°C | Temperatura máxima antes de activar ventilación |
| TEMP_UMBRAL_BAJO | 40.0°C | Temperatura mínima antes de activar calefacción |
| HUM_UMBRAL | 50.0% | Humedad mínima antes de activar humidificador |
| AIR_UMBRAL | 1200 | Umbral de calidad de aire para ventilación |

## Evidencia de funcionamiento
# Video de funcionamiento 
[Video](https://drive.google.com/drive/folders/1AQbpGpi7e0rlrNGNPIrpgBGgKlkwMyw0?usp=sharing)

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








