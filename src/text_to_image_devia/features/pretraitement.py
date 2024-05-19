import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import re
import os
import cv2


# Chemin vers la source
file_path = "../data/raw/Flickr8k_text/Flickr8k_token.txt"
image_path = "../data/raw/Flickr8k_image/Images/"

jpgs = os.listdir(image_path)

# Charger le modèle SpaCy en anglais
nlp = spacy.load("en_core_web_sm")

# Fonction pour nettoyer et prétraiter le texte

def remove_maj_punct_nonalpha(text:str) -> str:
    # Convertir en minuscules
    text = text.lower()
    # Supprimer la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Supprimer les chiffres et autres caractères non alphabétiques
    text = re.sub(r'\d+', '', text)
    return text

# Fonction pour effectuer la lemmatisation et la tokenisation
def lemmatize_and_tokenize(text : str) -> list:
    tokens = []
    # Analyser le texte avec SpaCy
    doc = nlp(text)
    # Lemmatisation et tokenisation
    for token in doc:
        if token.text not in STOP_WORDS and token.text.strip():
            tokens.append(token.lemma_)
    return tokens

# Ajouter les jetons de début et de fin
def add_start_end_tokens(tokens):
    tokens.insert(0, "startseq")
    tokens.append("endseq")
    return tokens

# Fonction principale pour prétraiter les légendes
def preprocess_captions_text(text):
    # Créer une liste pour stocker les légendes prétraitées
    preprocessed_captions = []
    # Diviser la chaîne de caractères en identifiant et texte
    id, text = text.strip().split("\t")
    # Appliquer le prétraitement au texte
    text = remove_maj_punct_nonalpha(text)
    # Lemmatisation et tokenisation
    tokens = lemmatize_and_tokenize(text)
    # Ajouter les jetons de début et de fin
    tokens = add_start_end_tokens(tokens)
    # Ajouter l'identifiant et les tokens prétraités à la liste de légendes prétraitées
    preprocessed_captions.append((id, tokens))
    
    return preprocessed_captions


# Utilisation des fonctions
preprocessed_captions = preprocess_captions_text(file_path)

# Affichage des légendes prétraitées
for id, tokens in preprocessed_captions:
    print(id, tokens)

# Chemin vers le dossier de sortie pour les images redimensionnées
dossier_sortie = "../data/processed/Flickr8k_image_processed/"

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)

# Prétraitement de l'image

# Parcourir tous les fichiers du dossier
#for fichier in os.listdir(image_path):
#    # Vérifier si le fichier est une image (extension .jpg, .png, etc.)
#    if fichier.endswith(".jpg") or fichier.endswith(".png") or fichier.endswith(".jpeg"):
#        # Construire le chemin complet de l'image
#        chemin_image_entree = os.path.join(image_path, fichier)
#        # Charger l'image
#        image = cv2.imread(chemin_image_entree)
#        # Redimensionner l'image à la taille attendue par VGG16 (224x224)
#        image_redimensionnee = cv2.resize(image, (224, 224))
#        # Construire le chemin de sortie pour l'image redimensionnée
#        chemin_image_sortie = os.path.join(dossier_sortie, fichier)
#        # Enregistrer l'image redimensionnée
#        cv2.imwrite(chemin_image_sortie, image_redimensionnee)