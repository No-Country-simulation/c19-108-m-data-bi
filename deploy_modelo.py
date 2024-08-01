import streamlit as st
import joblib


model = joblib.load('data/modelo.pkl')

# Función para realizar predicciones
def predict_riesgo(model,RDT,RDC, RDLP, Rotación_de_Inv, Rotación_de_AT, Rotación_de_C_por_c, Margen_de_UN,
                    Rent_Sobre_los_A, Rent_Sobre_el_Pat_N, Liquidez_Corriente, Prueba_Acida, Liquidez_Inmediata):
    
    """
    
    """
    
    features = [[RDT,RDC, RDLP, Rotación_de_Inv, Rotación_de_AT, Rotación_de_C_por_c, Margen_de_UN,
                    Rent_Sobre_los_A, Rent_Sobre_el_Pat_N, Liquidez_Corriente, Prueba_Acida, Liquidez_Inmediata]]
    prediction = model.predict(features)

    return prediction[0].title()

# 'RDT', 'RDC', 'RDLP', 'Rotación de Inv.', 'Rotación de A.T.', 'Rotación de C. por c.', 'Margen de U.N', 'Rent. Sobre los A.', 
# 'Rent Sobre el Pat. N.', 'Liquidez Corriente', 'Prueba Ácida', 'Liquidez Inmediata', 'Riesgo_Crediticio'


# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Clasificador de Riesgo Crediticio</h1>", unsafe_allow_html=True)

# Encabezado y descripción
st.write("""
Este es un clasificador de Riesgo Crediticio simple basado en un modelo de Logistic Regression.
Introduce los ratios para predecir la condicion crediticia.
""")

# Nota emergente para guiar al usuario
st.info("""A continuación, ingresa los ratios de la empresa. 
        Ajusta los parámetros según sea necesario y haz clic en 'Predecir' para obtener la condicion crediticia. 


        Ponemos a disposición la nomenclatura de los parámetros abreviados:


        RDT: Rentabilidad del total de activos
        RDC: Rentabilidad del capital
        RDLP: Rentabilidad del patrimonio
        Rotación de Inv.: Rotación de inventarios
        Rotación de A.T.: Rotación de activos totales
        Rotación de C. por c.: Rotación de cuentas por cobrar
        Márgen de U.N.: Márgen de utilidad neta
        Rent. Sobre los A.: Rentabilidad sobre los activos (ROA)
        Rent Sobre el Pat. N.: Rentabilidad sobre el patrimonio neto (ROE)""")


# Agregar controles deslizantes para las características de la flor

RDT = st.number_input('Ingrese el valor de RDT (decimales separados por coma)', value=0.0, format="%.2f")
RDC = st.number_input('Ingrese el valor de RDC (decimales separados por coma)', value=0.0, format="%.2f")
RDLP = st.number_input('Ingrese el valor de RDLP (decimales separados por coma)', value=0.0, format="%.2f")
Rotación_de_Inv = st.number_input('Ingrese el valor de Rotación de Inv. (decimales separados por coma)', value=0.0, format="%.2f")
Rotación_de_AT = st.number_input('Ingrese el valor de Rotación de A.T. (decimales separados por coma)', value=0.0, format="%.2f")
Rotación_de_C_por_c = st.number_input('Ingrese el valor de Rotación de C. por c. (decimales separados por coma)', value=0.0, format="%.2f")
Margen_de_UN = st.number_input('Ingrese el valor de Márgen de U.N. (decimales separados por coma)', value=0.0, format="%.2f")
Rent_Sobre_los_A =st.number_input('Ingrese el valor de Rent. Sobre los A. (decimales separados por coma)', value=0.0, format="%.2f")
Rent_Sobre_el_Pat_N =  st.number_input('Ingrese el valor de Rent Sobre el Pat. N. (decimales separados por coma)', value=0.0, format="%.2f")
Liquidez_Corriente =st.number_input('Ingrese el valor de Liquidez Corriente (decimales separados por coma)', value=0.0, format="%.2f")
Prueba_Acida = st.number_input('Ingrese el valor de Prueba Ácida (decimales separados por coma)', value=0.0, format="%.2f")
Liquidez_Inmediata = st.number_input('Ingrese el valor de Liquidez Inmediata (decimales separados por coma)', value=0.0, format="%.2f")

# Realizar la predicción cuando se haga clic en el botón
if st.button('Predecir'):
    riesgo_prediction = predict_riesgo(model, RDT,RDC, RDLP, Rotación_de_Inv, Rotación_de_AT, Rotación_de_C_por_c, Margen_de_UN,
                    Rent_Sobre_los_A, Rent_Sobre_el_Pat_N, Liquidez_Corriente, Prueba_Acida, Liquidez_Inmediata)
    st.write(f'La predicción para el otorgamiento del crédito a la empresa es: {riesgo_prediction}')