# 📂 app.py
# Importation des modules nécessaires
import streamlit as st  # Interface utilisateur
from utils.ingest import process_documents  # Fonction d’ingestion et vectorisation
from utils.qa_chain import get_chain        # Fonction de création de la chaîne LangChain (LLM + Retriever)

# Configuration de la page Streamlit (titre et icône de l’onglet navigateur)
st.set_page_config(page_title="Assistant RAG", page_icon="🤖")

# Titre principal affiché dans l'app
st.title("📚 Assistant IA – RAG Demo")

# Zone de saisie pour que l'utilisateur fournisse sa clé API OpenAI
api_key = st.text_input("🔑 Clé OpenAI", type="password")

# Zone de dépôt de fichiers (multi-upload autorisé) – accepte PDF, TXT et DOCX
uploaded_files = st.file_uploader(
    "📄 Déposez vos documents",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)

# Si des fichiers sont uploadés ET une clé API est fournie...
if uploaded_files and api_key:
    # Affichage d’un message de succès
    st.success("📥 Documents reçus, traitement en cours…")

    # Étape 1 : Ingestion des documents (lecture + découpage + embedding + FAISS)
    vectordb = process_documents(uploaded_files, api_key)

    # Étape 2 : Création de la chaîne LangChain pour faire du Retrieval-Augmented Generation
    chain = get_chain(vectordb, api_key)

    # Séparateur visuel
    st.markdown("---")

    # Sous-titre pour l'espace de chat
    st.subheader("💬 Posez une question sur vos documents")

    # Champ de saisie pour poser une question à l'IA
    question = st.text_input("❓ Question")

    # Si une question est posée...
    if question:
        # Affiche un spinner pendant que l'IA réfléchit
        with st.spinner("Réflexion en cours..."):
            # Lancement de la chaîne LangChain (LLM + recherche vectorielle)
            result = chain({"query": question})  # Renvoie réponse + sources

            # Affichage de la réponse
            st.markdown(f"### 🤖 Réponse :\n{result['result']}")

            # Affichage des sources
            if result.get("source_documents"):
                st.markdown("### 📎 Sources utilisées :")
                for i, doc in enumerate(result["source_documents"], 1):
                    metadata = doc.metadata
                    path = metadata.get('source', 'Document inconnu')
                    st.markdown(f"- **Document {i}** : `{path}`")