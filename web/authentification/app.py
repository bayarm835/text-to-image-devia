import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (LoginError, RegisterError)
from PIL import Image
import io
import numpy as np
from keras.models import load_model
from pretraitement import translate_english_to_french

# Loading config file
with open('../config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

def home_page():
    st.image('../images/welcome.png')
    st.markdown("<h6 style='text-align: center;'>Pour se connecter à votre compte, allez sur la page de connexion dans la barre latérale !</h6>", unsafe_allow_html=True)

def connexion_page():
    # Creating a login widget
    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Bienvenue *{st.session_state["name"]}*')
        st.write(f"Vous pouvez maintenant vous rendre sur la page de prédiction !")
    elif st.session_state["authentication_status"] is False:
        st.error('Nom d\'utilisateur/Mot de passe is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Entrer votre nom d\'utilisateur et votre mot de passe')
    
    if not st.session_state.get("authentication_status"):
        st.write("Pas encore de compte ?")
        if st.button("Inscrivez-vous !"):
            st.session_state.page = "Inscription"

def prediction_page():
    if not st.session_state.get("authentication_status"):
        st.warning("Veuillez vous connecter pour accéder à cette page.")
        return

    uploaded_file = st.file_uploader("Choisissez une image")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()

        # To open image using PIL:
        image = Image.open(io.BytesIO(bytes_data))
        st.image(image, caption='Image chargée avec succès!', use_column_width=True)

        if st.button("Prédire"):
            with st.spinner('Prédiction en cours...'):
                # Resize the image to 224x224
                resized_image = image.resize((224, 224))

                # Convert the resized image to a numpy array
                image_array = np.array(resized_image) / 255.0  # Normalize the image
                image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

                # Load the model
                model = load_model('model.keras')

                # Perform prediction
                prediction = model.predict(image_array)
                predicted_class = np.argmax(prediction, axis=1)[0]

                # Translate prediction
                translation = translate_english_to_french(predicted_class)
                st.write(f'Prediction: {translation}')

def signin_page():
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success('Utilisateur enregistré avec succès')
    except RegisterError as e:
        st.error(e)

    if st.button("Revenir à la page d'accueil"):
        st.session_state.page = "Accueil"

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Accueil"

    with st.sidebar:
        add_selectbox = st.sidebar.selectbox(
            "Choisissez une page :",
            ("Accueil", "Inscription", "Connexion", "Prédiction")
        )

    if add_selectbox == "Accueil":
        st.session_state.page = "Accueil"
    elif add_selectbox == "Inscription":
        st.session_state.page = "Inscription"
    elif add_selectbox == "Connexion":
        st.session_state.page = "Connexion"
    elif add_selectbox == "Prédiction":
        st.session_state.page = "Prédiction"

    if st.session_state.page == "Accueil":
        home_page()
    elif st.session_state.page == "Inscription":
        signin_page()
    elif st.session_state.page == "Connexion":
        connexion_page()
    elif st.session_state.page == "Prédiction":
        prediction_page()

if __name__ == "__main__":
    main()

# Saving config file
with open('../config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)
