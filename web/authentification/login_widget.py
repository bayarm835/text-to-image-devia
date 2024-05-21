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

# Define if a user is connected
def authenticate_user(username, password):
    try:
        authenticator.login(fields={"username": username, "password": password})
        return True
    except Exception as e:
        return False

# Creating a login widget
if st.session_state.get("authentication_status") is None:
    username = st.text_input("Username")

    # Button for username forgot
    if st.button("Forgot Username?"):
        try:
            authenticator.forgot_username()
            #st.success("Username retrieval instructions sent to your email")
        except ForgotError as e:
            st.error(e)

    password = st.text_input("Password", type="password")

    # Button for password reset
    if st.button("Forgot Password?"):
        try:
            authenticator.forgot_password()
            st.success("Password reset instructions sent to your email")
        except ForgotError as e:
            st.error(e)

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state["authentication_status"] = True
            st.write(f'Welcome *{st.session_state["name"]}*')
            st.title('Some content')
        else:
            st.error('Username/password is incorrect')

    if st.button("Inscription"):
        try:
            st.switch_page("pages/nouvel_utilisateur.py")
        except LoginError as e:
            st.error(e)

# Creating a password reset widget
if st.session_state["authentication_status"]:
    try:
        if st.button("Réinitialisation du mot de passe"):
            try:
                st.switch_page("pages/mdp_reset.py")
            except Exception as e:
                st.error(e)
    except Exception as e:
        st.error(e)

# Saving config file
with open('../config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)