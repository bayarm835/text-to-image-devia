import pendulum
from airflow.decorators import dag, task
from text_to_image_devia import remove_maj_punct_nonalpha, lemmatize_and_tokenize, add_start_end_tokens, preprocess_captions_text

@dag( 
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)

def devia_dag():
    """
    ### Pipeline de prétraitement des données
    ---
    #### Description
    Ce pipeline permet de prétraiter les légendes des images pour les transformer en tokens.

    """
    @task()
    def preprocess_text(text):
        text = remove_maj_punct_nonalpha(text)
        tokens = add_start_end_tokens(lemmatize_and_tokenize(text))
        return text, tokens
    #@task.docker(image):
    
         
    
        
    
    