import dht
from machine import Pin, ADC
import time

# Definir pines
DHT_PIN = Pin(4, Pin.IN)      # GPIO4 para el sensor DHT22
RELAY_1 = Pin(21, Pin.OUT)    # GPIO21 para el ventilador (control de temperatura y aire)
RELAY_2 = Pin(22, Pin.OUT)    # GPIO22 para el humidificador (control de humedad)
MQ135_PIN = 34                # GPIO34 (ADC1_6) para el sensor MQ-135

# Inicializar el sensor DHT22
sensor = dht.DHT22(DHT_PIN)

# Inicializar el sensor MQ-135 como entrada analógica
mq135_sensor = ADC(Pin(MQ135_PIN))
# Configurar la atenuación para lecturas de 0-3.3V (ESP32)
mq135_sensor.atten(ADC.ATTN_11DB)
# Configurar resolución a 12 bits (0-4095)
mq135_sensor.width(ADC.WIDTH_12BIT)

# Configurar umbrales
TEMP_UMBRAL = 35.0    # Temperatura en grados Celsius
HUM_UMBRAL = 30.0     # Humedad en porcentaje
AIR_UMBRAL = 1200     # Umbral para calidad del aire (ajustar según calibración)

# Inicialmente, apagar los relés
RELAY_1.value(1)    # Ventilador apagado
RELAY_2.value(1)    # Humidificador apagado

print("Sistema de control automático de temperatura, humedad y calidad del aire")
print(f"El ventilador se encenderá cuando la temperatura > {TEMP_UMBRAL}°C o calidad del aire > {AIR_UMBRAL}")
print(f"El humidificador se encenderá cuando la humedad < {HUM_UMBRAL}%")

try:
    while True:
        try:
            # Leer datos del sensor DHT22
            sensor.measure()
            temperatura = sensor.temperature()
            humedad = sensor.humidity()
            
            # Leer datos del sensor MQ-135
            valor_mq135 = mq135_sensor.read()
            
            # Mostrar lecturas
            print(f"Temperatura: {temperatura:.1f}°C, Humedad: {humedad:.1f}%, Calidad del aire: {valor_mq135}")
            
            # Variable para controlar el estado del ventilador
            activar_ventilador = False
            
            # Verificar si se necesita encender el ventilador por temperatura
            if temperatura > TEMP_UMBRAL:
                print("¡Temperatura alta!")
                activar_ventilador = True
                
            # Verificar si se necesita encender el ventilador por calidad del aire
            if valor_mq135 > AIR_UMBRAL:
                print("¡Calidad del aire deficiente!")
                activar_ventilador = True
            
            # Controlar el ventilador basado en temperatura o calidad del aire
            if activar_ventilador:
                if RELAY_1.value() == 1:  # Si está apagado
                    print("Encendiendo ventilador...")
                    RELAY_1.value(0)      # Encender ventilador
            else:
                if RELAY_1.value() == 0:  # Si está encendido
                    print("Condiciones normales. Apagando ventilador.")
                    RELAY_1.value(1)      # Apagar ventilador
            
            # Control del humidificador basado en humedad
            if humedad < HUM_UMBRAL:
                if RELAY_2.value() == 1:  # Si está apagado
                    print("¡Humedad baja! Encendiendo humidificador...")
                    RELAY_2.value(0)      # Encender humidificador
            else:
                if RELAY_2.value() == 0:  # Si está encendido
                    print("Humedad normal. Apagando humidificador.")
                    RELAY_2.value(1)      # Apagar humidificador
                    
            # Esperar antes de la siguiente lectura
            # El DHT22 no puede leer más rápido que cada 2 segundos
            time.sleep(3)
            
        except Exception as e:
            print(f"Error en la lectura de los sensores: {e}")
            time.sleep(2)
            
except KeyboardInterrupt:
    # Limpiar al salir
    RELAY_1.value(1)  # Apagar ventilador
    RELAY_2.value(1)  # Apagar humidificador
    print("Programa terminado")