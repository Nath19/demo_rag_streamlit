# demo_rag_streamlit# 📚 Assistant IA – Démo RAG avec Streamlit + LangChain + OpenAI

Cette application Streamlit vous permet de tester une **architecture RAG (Retrieval-Augmented Generation)**, utilisée pour enrichir un LLM avec vos propres documents (PDF, TXT, DOCX) et obtenir des réponses fiables et contextualisées.

---

## 🚀 Fonctionnalités

| Fonction | Description |
|----------|-------------|
| 📥 Upload de documents | Déposez des fichiers que l'IA pourra consulter |
| 🔐 Authentification | Fournissez votre clé API OpenAI dans l'app |
| 🧠 Embedding | Les documents sont transformés en vecteurs numériques |
| 🗃️ Indexation vectorielle | Les vecteurs sont stockés dans une base FAISS |
| 🤖 RAG | L’IA interroge la base pour générer des réponses documentées |
| 🧑‍💻 Interface Streamlit | Simple et accessible depuis un navigateur |

---

## 📁 Structure du projet

```bash
.
├── app.py                      # L’application principale Streamlit
├── utils/
│   ├── ingest.py               # Ingestion des documents, découpage et vectorisation
│   ├── qa_chain.py             # Construction de la chaîne RAG LangChain
│   └── embeddings.py           # Initialisation des embeddings OpenAI
├── requirements.txt            # Liste des dépendances Python
└── README.md                   # Ce fichier explicatif



🔧 Installation (en local)

1. Cloner le projet

git clone https://github.com/votre-utilisateur/assistant-rag.git
cd assistant-rag

2. Créer un environnement virtuel

python3 -m venv .venv
source .venv/bin/activate

3. Installer les dépendances

pip install -r requirements.txt

▶️ Lancer l’application

streamlit run app.py

Ouvre automatiquement localhost:8501 dans ton navigateur.

🔐 Configuration de la clé OpenAI

L’interface te demandera d’entrer ta clé API (sk-xxxx...) au lancement.
💡 Tu peux aussi créer un fichier .env et modifier le code pour charger la clé automatiquement :

OPENAI_API_KEY=sk-xxxxxx

🧠 Comment fonctionne chaque fichier Python ?

🧠 Fonctionnement détaillé des fichiers

🔹 app.py (interface utilisateur)
	•	Utilise Streamlit pour créer une interface simple
	•	Permet à l’utilisateur :
	•	D’uploader ses documents
	•	De fournir sa clé OpenAI
	•	De poser une question
	•	De voir la réponse générée par le modèle
	•	Appelle process_documents() (ingestion + vectorisation)
	•	Puis get_chain() (orchestration avec LangChain)

🔹 utils/ingest.py
	•	Gère l’ingestion des documents
	•	Utilise des loaders adaptés (PDF, TXT, DOCX)
	•	Découpe les documents en chunks
	•	Vectorise les chunks avec OpenAI Embeddings
	•	Stocke les vecteurs dans FAISS

🔹 utils/qa_chain.py
	•	Crée une chaîne LangChain RetrievalQA
	•	Combine un LLM (GPT-4) avec un retriever (la base FAISS)
	•	Permet de poser une question → récupération des documents → génération d’une réponse augmentée

🔹 utils/embeddings.py
	•	Initialise un modèle d’embedding OpenAIEmbeddings
	•	Reçoit la clé API en paramètre
	•	Sert à transformer le texte en vecteurs numériques pour la base vectorielle

📌 Cas d’usage typique

	Exemple : “Un collaborateur pose une question sur le télétravail dans l’entreprise”

	•	Le RH a déposé un fichier PDF contenant la charte
	•	Le modèle vectorise le contenu
	•	L’utilisateur demande : “Combien de jours de télétravail sont autorisés ?”
	•	L’IA interroge les vecteurs → trouve la bonne section → génère une réponse fiable et contextualisée ✅


🧪 Idées d’amélioration
	•	🔁 Ajouter une mémoire conversationnelle (Historique)
	•	📤 Export des réponses en PDF ou copier-coller enrichi
	•	🔐 Authentification utilisateur
	•	🌐 Déploiement sur Streamlit Cloud, Render, Vercel…
	•	📂 Intégration d’autres formats (Notion, Airtable, CSV, etc.)


📄 Fichier → 🧹 Nettoyage → 📚 Document → ✂️ Chunk → 🔢 Embedding → 🗃️ FAISS


🙌 Auteur


Nathan Amar – Data & GenAI Expert