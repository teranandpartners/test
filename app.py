import streamlit as st

def obtener_edad_retiro(sexo):
    if sexo.lower() == 'femenino':
        return 65
    elif sexo.lower() == 'masculino':
        return 67
    else:
        st.error('Sexo no reconocido.')
        return None

def calcular_ahorro(meses, aporte_mensual, tasa_anual):
    tasa_mensual = tasa_anual / 12
    total = 0
    for _ in range(meses):
        total = (total + aporte_mensual) * (1 + tasa_mensual)
    return total

# Interfaz de usuario
st.title("💰 Calculadora de Ahorro para el Retiro")

edad_actual = st.number_input("¿Cuál es tu edad actual?", min_value=0, max_value=100, value=30)
sexo = st.selectbox("¿Cuál es tu sexo?", options=["femenino", "masculino"])
aporte = st.number_input("¿Cuánto deseas aportar mensualmente? ($)", min_value=0.0, step=10.0, value=100.0)

if st.button("Calcular"):
    edad_retiro = obtener_edad_retiro(sexo)
    if edad_retiro and edad_actual < edad_retiro:
        años_restantes = edad_retiro - edad_actual
        meses_restantes = años_restantes * 12
        tasa_anual = 0.0614
        ahorro = calcular_ahorro(meses_restantes, aporte, tasa_anual)
        st.success(f"A los {edad_retiro} años tendrás ahorrado aproximadamente: ${ahorro:,.2f}")
    elif edad_actual >= edad_retiro:
        st.warning("Ya alcanzaste o superaste la edad de retiro.")
