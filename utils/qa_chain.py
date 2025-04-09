# 📂 utils/qa_chain.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_chain(vectordb, api_key):
    """
    Création d'une chaîne RetrievalQA qui renvoie :
    - la réponse générée par GPT-4
    - les documents sources ayant servi de contexte
    """

    # Initialisation du LLM (GPT-4)
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=api_key,
        model_name="gpt-4"
    )

    # Création d'une chaîne RetrievalQA avec retour des sources documentaires
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True  # ← Clé magique pour afficher les sources
    )

    return chain