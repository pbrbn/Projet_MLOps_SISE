import streamlit as st
import requests

#Eléments interface Streamlit
st.title("Classification Iris")
st.write("Vous devez entrer les caractéristiques de votre fleur pour avoir votre prédiction.")

#Entrée des valeurs des variables
sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width", min_value=0.0, max_value=10.0, step=0.1)

#Bouton pour la prédicition via le server FastAPI
if st.button('Predict'):

    data = {
        "sepal_length":sepal_length,
        "sepal_width":sepal_width,
        "petal_length":petal_length,
        "petal_width":petal_width
    }

    response = requests.post("http://server:8000/predict", json=data)

    if response.status_code == 200 :
        prediction = response.json().get("prediction")
        st.write(f"Prédiction : {prediction}")
    else:
        st.write("Erreur dans la prédiction")
        st.write(response)




