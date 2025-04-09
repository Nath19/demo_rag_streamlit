# 📂 utils/ingest.py

# Modules standards
import os
import tempfile  # Pour stocker temporairement les fichiers uploadés

# Loaders de documents selon leur format
from langchain.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader

# Pour découper les documents en morceaux exploitables
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Embedding via OpenAI (conversion texte → vecteur)
from langchain.embeddings import OpenAIEmbeddings

# Stockage vectoriel (indexation et recherche par similarité)
from langchain.vectorstores import FAISS


def process_documents(uploaded_files, api_key):
    """
    Pipeline de traitement des documents :
    1. Sauvegarde temporaire
    2. Chargement (PDF, TXT, DOCX)
    3. Découpage en chunks
    4. Embedding OpenAI
    5. Stockage dans FAISS (vectorstore)
    
    Paramètres :
    - uploaded_files : liste de fichiers uploadés via Streamlit
    - api_key : clé API OpenAI pour l'embedding

    Retour :
    - vectordb : base FAISS contenant les vecteurs prêts pour la recherche
    """

    documents = []  # Stocke tous les documents chargés

    for file in uploaded_files:
        # Extension du fichier (.pdf, .txt, .docx)
        suffix = os.path.splitext(file.name)[1]

        # Création d’un fichier temporaire pour le traitement
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file.read())        # Écriture du contenu dans le fichier temporaire
            tmp_path = tmp.name           # Chemin du fichier temporaire

        # Sélection du bon loader selon le type de fichier
        if suffix == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(tmp_path)
        else:
            loader = TextLoader(tmp_path)  # Pour les fichiers .txt

        # Chargement du contenu du fichier en documents LangChain
        docs = loader.load()
        documents.extend(docs)

    # Découpage des documents en chunks de 1000 caractères avec 100 de recouvrement
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    # Initialisation du modèle d’embedding OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # Indexation vectorielle avec FAISS (recherche rapide par similarité)
    vectordb = FAISS.from_documents(chunks, embedding=embeddings)

    return vectordb  # On retourne la base vectorielle prête à être interrogée