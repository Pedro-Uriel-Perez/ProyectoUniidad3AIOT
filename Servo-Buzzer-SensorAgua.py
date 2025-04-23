from machine import Pin, PWM, ADC, Timer
import time
import math

# Definir pines
WATER_SENSOR_PIN = 32       # GPIO32 para el sensor de nivel de agua (ADC)
SERVO_PIN = 13              # GPIO13 para el servomotor
BUZZER_PIN = 15             # GPIO15 para el buzzer

# Configuración del sensor de agua
water_sensor = ADC(Pin(WATER_SENSOR_PIN))
water_sensor.atten(ADC.ATTN_11DB)  # Configurar para rango completo: 0-3.3V
water_sensor.width(ADC.WIDTH_12BIT)  # Resolución de 12 bits (0-4095)

# Valor mínimo y máximo para calibración del sensor de agua (ajustar según tus mediciones)
WATER_MIN = 500   # Lectura cuando el recipiente está vacío
WATER_MAX = 2500  # Lectura cuando el recipiente está lleno

# Umbral para alerta de nivel bajo de agua (20%)
WATER_LOW_THRESHOLD = 20

# Configuración del servomotor - AJUSTADO para movimiento más pequeño
servo = PWM(Pin(SERVO_PIN), freq=50)  # PWM a 50Hz para servomotores estándar

# Valores ajustados para un movimiento más sutil
# Estos valores representan el duty cycle directamente en lugar de ángulos
SERVO_CLOSED = 120    # Posición cerrada/reposo (ajustar según tu servo)
SERVO_OPEN = 115      # Posición ligeramente abierta (muy pequeño cambio)

# Configuración del buzzer
buzzer = PWM(Pin(BUZZER_PIN), freq=2000, duty=0)  # Inicialmente apagado con frecuencia válida

# Variable para seguir el estado del sistema
last_servo_time = 0
agua_porcentaje = 100
servo_active = False

# Función para activar el buzzer
def buzzer_on(freq=2000):
    buzzer.freq(freq)
    buzzer.duty(512)  # 50% de duty cycle

# Función para desactivar el buzzer
def buzzer_off():
    buzzer.duty(0)

# Función para mover el servo gradualmente entre dos valores de duty
def move_servo_slowly(start_duty, end_duty, duration_ms, steps=20):
    global servo_active
    servo_active = True
    
    # Activar buzzer cuando se mueve el motor
    buzzer_on()
    
    # Calcular el incremento por paso
    step_size = (end_duty - start_duty) / steps
    step_time_ms = duration_ms / steps
    
    # Mover gradualmente
    for i in range(steps + 1):
        duty = start_duty + (step_size * i)
        servo.duty(int(duty))
        time.sleep_ms(int(step_time_ms))
    
    buzzer_off()
    servo_active = False

# Configurar el servo en posición inicial
servo.duty(SERVO_CLOSED)  # Posición cerrada inicial

print("Sistema de monitoreo de agua y control de servomotor")
print(f"El servomotor se activará cada 5 minutos con un movimiento muy sutil")
print(f"El buzzer sonará cuando el nivel de agua sea menor al {WATER_LOW_THRESHOLD}%")

try:
    while True:
        # Leer el sensor de agua y convertir a porcentaje
        water_raw = water_sensor.read()
        agua_porcentaje = max(0, min(100, ((water_raw - WATER_MIN) / (WATER_MAX - WATER_MIN)) * 100))
        
        # Mostrar el nivel de agua
        print(f"Nivel de agua: {agua_porcentaje:.1f}%")
        
        # Verificar si el nivel de agua está bajo
        if agua_porcentaje < WATER_LOW_THRESHOLD and not servo_active:
            print("¡ALERTA! Nivel de agua bajo")
            buzzer_on(1500)  # Tono diferente para la alerta de agua
            time.sleep(1)
            buzzer_off()
        
        # Verificar si es momento de activar el servomotor (cada 5 minutos)
        current_time = time.time()
        if current_time - last_servo_time >= 300 and not servo_active:  # 300 segundos = 5 minutos
            print("Activando servomotor...")
            
            # Mover lentamente el servo a la posición ligeramente abierta (3 segundos)
            move_servo_slowly(SERVO_CLOSED, SERVO_OPEN, 3000)
            
            # Volver a cerrar rápidamente (0.5 segundos)
            move_servo_slowly(SERVO_OPEN, SERVO_CLOSED, 500)
            
            # Actualizar tiempo
            last_servo_time = current_time
        
        # Esperar antes de la próxima lectura
        time.sleep(1)
        
except KeyboardInterrupt:
    # Limpiar al salir
    servo.duty(0)
    buzzer_off()
    print("Programa terminado")