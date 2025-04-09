# 📂 utils/embeddings.py

# On importe le module OpenAIEmbeddings depuis LangChain
# Ce composant permet de convertir du texte en vecteurs numériques (embeddings)
from langchain.embeddings import OpenAIEmbeddings


def get_embedding_model(api_key):
    """
    Initialise un modèle d'embedding basé sur l'API OpenAI.

    Paramètres :
    - api_key (str) : Clé API OpenAI fournie par l'utilisateur

    Retour :
    - Instance de OpenAIEmbeddings prête à être utilisée pour vectoriser des documents
    """
    return OpenAIEmbeddings(openai_api_key=api_key)