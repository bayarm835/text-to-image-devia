import yaml
import streamlit as st
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 

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
    st.write("Bienvenue sur la page d'accueil!")
    st.image('../images/welcome.png')
    st.markdown("<h6 style='text-align: center;'>Pour se connecter à votre compte, allez sur la page de connexion dans la barre latérale !</h6>", unsafe_allow_html=True)

def connexion_page():
    st.write("Bienvenue sur la page de connexion!")
    # Creating a login widget
    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    st.write("Pas encore de compte ?")
    st.page_link("pages/nouvel_utilisateur.py", label="Inscrivez-vous !")

def prediction_page():
    st.write("Bienvenue sur la page de prédiction!")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Accueil"

    with st.sidebar:
        add_selectbox = st.sidebar.selectbox(
            "Choisissez une page :",
            ("Accueil", "Connexion", "Prédiction")
        )

    if add_selectbox == "Accueil":
        st.session_state.page = "Accueil"
    elif add_selectbox == "Connexion":
        st.session_state.page = "Connexion"
    elif add_selectbox == "Prédiction":
        st.session_state.page = "Prédiction"

    if st.session_state.page == "Accueil":
        home_page()
    elif st.session_state.page == "Connexion":
        connexion_page()
    elif st.session_state.page == "Prédiction":
        prediction_page()

if __name__ == "__main__":
    main()

# Saving config file
with open('../config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)
