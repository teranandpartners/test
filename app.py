
import streamlit as st
from PIL import Image

# Cargar y mostrar logo
logo = Image.open("logo.png")
st.image(logo, width=150)

# Título bilingüe
st.title("💰 Calculadora de Ahorro para el Retiro / Retirement Savings Calculator")

# Inputs del usuario
edad_actual = st.number_input("¿Cuál es tu edad actual? / What is your current age?", min_value=0, max_value=100, value=30)
sexo = st.selectbox("¿Cuál es tu sexo? / What is your gender?", options=["femenino / female", "masculino / male"])
aporte = st.number_input("¿Cuánto deseas aportar mensualmente? / How much would you like to save monthly?", min_value=0.0, step=10.0, value=100.0)

# Lógica de retiro
def obtener_edad_retiro(sexo_texto):
    if "femenino" in sexo_texto.lower():
        return 65
    elif "masculino" in sexo_texto.lower():
        return 67
    else:
        st.error("Sexo no reconocido / Unrecognized gender.")
        return None

def calcular_ahorro(meses, aporte_mensual, tasa_anual):
    tasa_mensual = tasa_anual / 12
    total = 0
    for _ in range(meses):
        total = (total + aporte_mensual) * (1 + tasa_mensual)
    return total

# Botón para calcular
if st.button("Calcular / Calculate"):
    edad_retiro = obtener_edad_retiro(sexo)
    if edad_retiro and edad_actual < edad_retiro:
        anios_restantes = edad_retiro - edad_actual
        meses_restantes = anios_restantes * 12
        tasa_anual = 0.09
        ahorro_final = calcular_ahorro(meses_restantes, aporte, tasa_anual)
        st.success(f"A los {edad_retiro} años / At age {edad_retiro} you will have saved approximately: ${ahorro_final:,.2f}")
    elif edad_actual >= edad_retiro:
        st.warning("Ya alcanzaste o superaste la edad de retiro. / You have already reached or passed retirement age.")

# Advertencia
st.warning(
    "📌 **Proyección estimada / Estimated Projection**\n"
    "Esta es una simulación basada en una tasa anual del 9%. Los resultados pueden variar según el comportamiento real del mercado.\n"
    "This is a simulation based on an annual rate of 9%. Results may vary depending on actual market performance."
)

# Información de contacto
st.markdown("---")
st.markdown("**Teran & Partners**")
Mercedes Peña 
st.markdown("Email: mercedes@teranandpartners.com")
st.markdown("Tel: +1 (305) 316 - 8909")


