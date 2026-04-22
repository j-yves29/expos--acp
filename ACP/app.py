import streamlit as st

st.set_page_config(
    page_title="L'Analyse en Composantes Principales",
    page_icon="📊",
    layout="wide"
)

# ── Titre principal ──
st.title("📊 L'Analyse en Composantes Principales (ACP)")
st.subheader("Une méthode puissante pour simplifier les données complexes")
st.markdown("---")

# ── Menu de navigation ──
section = st.sidebar.radio(
    "📌 Navigation",
    [
        "🎤 Présentation",
        "🏠 Introduction",
        "❓ C'est quoi l'ACP ?",
        "🎯 À quoi ça sert ?",
        "⚙️ Comment ça marche ?",
        "🌍 Domaines d'application",
        "✅ Conclusion",
        "🙏 Remerciements"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Utilisez le menu pour naviguer entre les sections.")

# ── Page d'accueil ──
if section == "🎤 Présentation":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='font-size: 60px; color: #1f77b4;'>👨‍🎓 Exposé présenté par</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style='text-align: center; background-color: #1f77b4; 
            padding: 40px; border-radius: 15px;'>
                <h1 style='color: white; font-size: 40px;'>M. BANDAMA</h1>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style='text-align: center; background-color: #1f77b4; 
            padding: 40px; border-radius: 15px;'>
                <h1 style='color: white; font-size: 40px;'>M. TOURÉ</h1>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div style='text-align: center; background-color: #1f77b4; 
            padding: 40px; border-radius: 15px;'>
                <h1 style='color: white; font-size: 40px;'>Mlle CISSÉ</h1>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <h3 style='color: gray;'>📊 Thème : L'Analyse en Composantes Principales (ACP)</h3>
        </div>
    """, unsafe_allow_html=True)

# ── Section : Introduction ──
if section == "🏠 Introduction":
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎓 Contexte de cet exposé")
        st.markdown("""
        Dans le monde actuel, nous sommes entourés de **données massives** :
        - Données médicales
        - Données financières
        - Données scientifiques

        Ces données ont souvent **des dizaines, voire des centaines de variables**.
        Comment les analyser simplement ? C'est là qu'intervient l'**ACP**.
        """)

    with col2:
        st.subheader("📋 Plan de l'exposé")
        st.markdown("""
        1. 🔍 C'est quoi l'ACP ?
        2. 🎯 À quoi ça sert ?
        3. ⚙️ Comment ça marche ?
        4. 🌍 Domaines d'application
        5. ✅ Conclusion
        """)

    st.markdown("---")
    st.success("💡 L'ACP est l'une des techniques les plus utilisées en Data Science et en statistiques.")

# ── Section : C'est quoi l'ACP ? ──
if section == "❓ C'est quoi l'ACP ?":
    st.subheader("❓ C'est quoi l'ACP ?")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📖 Définition simple
        L'ACP (**Analyse en Composantes Principales**) est une technique 
        statistique qui permet de :
        
        > **Résumer un grand tableau de données complexe 
        > en quelques informations essentielles,
        > sans trop perdre d'information.**
        
        C'est comme **compresser une image** : 
        elle devient plus légère mais reste reconnaissable.
        """)

    with col2:
        st.markdown("""
        ### 🧠 Analogie simple
        Imagine que tu veux décrire une personne avec 10 critères :
        - Taille, poids, pointure, longueur des bras...
        
        En réalité, beaucoup de ces critères sont **liés entre eux**.
        Une grande personne a souvent une grande pointure.
        
        L'ACP détecte ces liens et les **résume en 2 ou 3 critères principaux**
        au lieu de 10. ✅
        """)

    st.markdown("---")
    st.markdown("### 📌 En une phrase :")
    st.info("""
    L'ACP transforme un tableau avec beaucoup de colonnes 
    en un tableau plus petit, tout en gardant l'essentiel de l'information.
    """)

    st.markdown("### 🔑 Mots clés à retenir")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.warning("📉 Réduction de dimensions")
    with col2:
        st.warning("🔗 Corrélation entre variables")
    with col3:
        st.warning("📊 Visualisation simplifiée")

# ── Section : À quoi ça sert ? ──
if section == "🎯 À quoi ça sert ?":
    st.subheader("🎯 À quoi ça sert ?")
    st.markdown("---")

    st.markdown("### L'ACP sert principalement à 3 choses :")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("""
        ### 📉 1. Réduire la complexité
        Quand on a trop de variables,
        l'ACP les résume en quelques
        **composantes principales**
        qui contiennent l'essentiel
        de l'information.
        """)

    with col2:
        st.info("""
        ### 👁️ 2. Visualiser les données
        Elle permet de représenter
        des données complexes sur
        un **graphique 2D ou 3D**
        facile à lire et à interpréter.
        """)

    with col3:
        st.warning("""
        ### 🔍 3. Détecter des groupes
        En visualisant les données,
        on peut repérer des **groupes
        naturels** ou des ressemblances
        entre individus.
        """)

    st.markdown("---")
    st.markdown("### 💡 Exemple concret :")
    st.markdown("""
    Un médecin collecte **20 mesures** sur chaque patient 
    (poids, taille, tension, glycémie...).

    Grâce à l'ACP, il peut :
    - Résumer ces 20 mesures en **2 ou 3 indicateurs clés**
    - Visualiser facilement quels patients se ressemblent
    - Détecter des **profils de patients** à risque
    """)

# ── Section : Comment ça marche ? ──
if section == "⚙️ Comment ça marche ?":
    st.subheader("⚙️ Comment ça marche ?")
    st.markdown("---")

    st.markdown("### Les étapes de l'ACP en langage simple :")
    st.markdown("")

    st.info("""
    #### 🟦 Étape 1 — Collecter les données
    On part d'un tableau avec **beaucoup de colonnes** (variables)
    et beaucoup de lignes (individus).
    
    Exemple : 1000 patients × 20 mesures médicales
    """)

    st.info("""
    #### 🟦 Étape 2 — Standardiser les données
    On remet toutes les variables à la **même échelle**
    pour qu'aucune ne domine les autres.
    
    Exemple : la taille (170 cm) et le poids (70 kg)
    sont ramenés à des valeurs comparables.
    """)

    st.info("""
    #### 🟦 Étape 3 — Calculer les corrélations
    L'ACP cherche quelles variables **varient ensemble**.
    
    Exemple : taille et pointure sont souvent liées
    → elles peuvent être résumées en une seule information.
    """)

    st.info("""
    #### 🟦 Étape 4 — Créer les composantes principales
    L'ACP crée de **nouvelles variables** (les composantes)
    qui résument au mieux les données originales.
    
    La 1ère composante capture le maximum d'information,
    la 2ème capture le reste, et ainsi de suite.
    """)

    st.info("""
    #### 🟦 Étape 5 — Visualiser le résultat
    On garde seulement les **2 ou 3 premières composantes**
    et on les affiche sur un graphique simple.
    
    Ce graphique révèle la structure cachée des données ! 🎯
    """)

    st.markdown("---")
    st.success("✅ Résultat : un tableau de 20 colonnes devient un graphique 2D lisible par tous !")

# ── Section : Domaines d'application ──
if section == "🌍 Domaines d'application":
    st.subheader("🌍 Domaines d'application")
    st.markdown("---")

    st.markdown("### L'ACP est utilisée dans de nombreux domaines :")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        ### 🏥 Médecine & Santé
        - Analyse de profils de patients
        - Détection de maladies
        - Génomique et ADN
        - Imagerie médicale
        """)

        st.info("""
        ### 💰 Finance & Économie
        - Analyse de portefeuilles d'actions
        - Détection de fraudes bancaires
        - Segmentation de clients
        - Prévision de marchés
        """)

        st.warning("""
        ### 🌿 Environnement
        - Analyse climatique
        - Surveillance de la pollution
        - Étude de la biodiversité
        - Prévision météorologique
        """)

    with col2:
        st.info("""
        ### 🤖 Intelligence Artificielle
        - Reconnaissance faciale
        - Traitement d'images
        - Compression de données
        - Réduction de bruit
        """)

        st.success("""
        ### 🧬 Biologie & Chimie
        - Classification d'espèces
        - Analyse de molécules
        - Recherche pharmaceutique
        - Étude des protéines
        """)

        st.warning("""
        ### 📱 Marketing & Réseaux sociaux
        - Segmentation de clients
        - Analyse de comportements
        - Recommandations personnalisées
        - Analyse de sentiments
        """)

    st.markdown("---")
    st.success("💡 En résumé : partout où il y a beaucoup de données, l'ACP peut aider !")

# ── Section : Conclusion ──
if section == "✅ Conclusion":
    st.subheader("✅ Conclusion")
    st.markdown("---")

    st.markdown("### 📝 Ce qu'il faut retenir :")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        ### ✅ Les points clés
        - L'ACP est une technique de **réduction de dimensions**
        - Elle résume des données complexes en **quelques composantes**
        - Elle permet de **visualiser** des données invisibles à l'œil nu
        - Elle est utilisée dans **tous les domaines** scientifiques
        - C'est l'un des outils les plus puissants du **Data Science**
        """)

    with col2:
        st.info("""
        ### 🚀 Pourquoi c'est important ?
        - Le monde produit des **données massives** chaque jour
        - Les humains ne peuvent pas analyser des milliers de variables
        - L'ACP aide à **simplifier** sans perdre l'essentiel
        - Elle est la **porte d'entrée** vers le Machine Learning
        - Elle est accessible même sans être mathématicien 😊
        """)

    st.markdown("---")
    st.markdown("### 💬 Citation pour finir :")
    st.warning("""
    *"L'objectif de l'ACP n'est pas de supprimer de l'information,
    mais de révéler ce qui était caché dans la complexité."*
    """)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Domaines d'application", value="100+")
    with col2:
        st.metric(label="Année de création", value="1901")
    with col3:
        st.metric(label="Utilisation en Data Science", value="Indispensable")

    st.markdown("---")
    st.success("🎓 Merci pour votre attention ! Des questions ?")

# ── Page de remerciements ──
if section == "🙏 Remerciements":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='font-size: 55px; color: #1f77b4;'>🙏 Merci pour votre attention !</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center; background-color: #1f77b4; 
        padding: 60px; border-radius: 20px;'>
            <h1 style='color: white; font-size: 70px;'>M. EVILAFO</h1>
            <h3 style='color: #d0e8ff; font-size: 28px;'>
                Le plus génial des professeurs 🏆
            </h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <h3 style='color: gray;'>
                Ce travail vous est dédié avec tout notre respect 🎓
            </h3>
        </div>
    """, unsafe_allow_html=True)