from airflow.decorators import dag, task
from text_to_image_devia.features.pretraitement import remove_maj_punct_nonalpha, lemmatize_and_tokenize, add_start_end_tokens, preprocess_captions_text
import pandas as pd

@dag(
    schedule=None,
    catchup=False,
    tags=["data-preparation"]
)
def prepare_data():
    """
    ## DAG to prepare the data for the text-to-image model.
    
    """
    @task.python
    def run_prepare_data():
        """
        Run the data preparation pipeline.
        
        Returns:
            - Preprocessed captions text.
            - 
        """
        # Load the data
        captions = pd.read_csv("data/raw/captions.csv")
        # Remove non-alphabetic characters, lower case and lemmatize the text
        captions["caption"] = captions["caption"].apply(remove_maj_punct_nonalpha)
        captions["caption"] = captions["caption"].apply(lemmatize_and_tokenize)
        # Add start and end tokens to the captions
        captions["caption"] = captions["caption"].apply(add_start_end_tokens)
        # Save the preprocessed captions
        captions.to_csv("data/processed/captions_preprocessed.csv", index=False)
        return captions
    
    run_prepare_data() 