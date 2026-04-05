**MET**

exploser sur le MET Metropolitain museum of art
utiliser streamlit et Nice gui pour mettre sous forme de site web (streamlit).

**A FAIRE :**
- touches pour naviguer entre les diapos, juste pour descendre d'un écran
- images mettre pour chaque diapo
- synthetiser le texte
- mettre la derniere page pour les sources
- changer les liens qui ne vont pas
- mettre des animations legeres

Voila l'architecture:

📁 TonProjetPortfolio/
│
├── 📄 main.py                <-- Le chef d'orchestre (Le menu)


├── 📄 requirements.txt       <-- La liste des outils (nicegui)
│

├── 📁 pages/                 <-- Le dossier qui contient tes pages web
│   
    ├── 📄 accueil.py         <-- Ta page de présentation
│   
    ├── 📄 experiences.py     <-- Ta page avec ton CV / tes stages
│   
    └── 📄 projets.py         <-- Ta page qui montre tes créations (ex: Concorde)
│
└── 📁 assets/                <-- Le dossier pour tes fichiers médias
    
    ├── 🖼️ photo_profil.jpg
    └── 🖼️ logo_lycee.png

Merci gemini prowww

## Deployment sur Hugging Face:

Étape 2 : Créer ton "Space" sur Hugging Face 🚀
Rends-toi sur le site huggingface.co et crée-toi un compte gratuit (si ce n'est pas déjà fait).

En haut à droite (à côté de ta photo de profil), clique sur "New" puis sur "Space".

**Remplis le formulaire :**

Space name : Donne un nom à ton projet (ex: MET-Exposition).

License : Laisse vide ou mets mit.

Select the Space SDK : C'est l'étape la plus importante ! Clique sur Docker, puis sélectionne Blank (vide).

Space Hardware : Laisse sur "Free" (Gratuit).

Clique sur le bouton "Create Space".

## **Étape 3 : Le fichier secret de déploiement (Dockerfile) 🐳**
Ton Space est créé, mais il est vide. Hugging Face a besoin d'un petit mode d'emploi pour savoir comment lancer ton projet. Ce mode d'emploi s'appelle un Dockerfile.

Dans VS Code, crée un nouveau fichier (à côté de app.py et requirements.txt).

Nomme-le exactement Dockerfile (avec un D majuscule, et sans aucune extension à la fin, pas de .txt ou de .py).

Copie-colle ces 6 lignes dedans et sauvegarde :

## **Dockerfile**
### 1. On part d'un ordinateur avec Python 3.10
FROM python:3.10

### 2. On crée notre dossier de travail
WORKDIR /code

### 3. On copie notre liste de courses et on l'installe
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

### 4. On copie tout le reste de nos fichiers (le code, les images...)
COPY . .

### 5. On lance l'application !
CMD ["python", "app.py"]
Étape 4 : Envoyer tes fichiers sur Hugging Face 📤
Hugging Face agit exactement comme GitHub ! Tu as deux options pour y mettre tes fichiers :

Option A (La plus facile pour commencer) : Le glisser-déposer
Sur la page de ton Space Hugging Face, clique sur l'onglet "Files", puis sur "Add file" > "Upload files".
Glisse-dépose simplement tous tes fichiers (app.py, requirements.txt, Dockerfile, et ton dossier assets). Clique sur "Commit changes".

Option B (La méthode Pro avec le terminal) :
Hugging Face te donne un lien Git (exactement comme GitHub). Tu peux connecter ton terminal VS Code directement à Hugging Face pour faire tes git push. (Les instructions sont affichées sur la page d'accueil de ton Space).

Que va-t-il se passer ensuite ? ⏳
Dès que tes fichiers sont en ligne, regarde en haut de la page de ton Space :

Le statut passera à "Building" (en jaune). Le serveur installe Python et lit ton requirements.txt. Ça prend environ 2 à 3 minutes la première fois.

S'il n'y a pas d'erreur, le statut passera à "Running" (en vert).

Ton site va apparaître au centre de l'écran ! Tu auras un lien définitif (du style https://tonpseudo-met-exposition.hf.space) que tu pourras envoyer à ton prof ou mettre sur ton CV !