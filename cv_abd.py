from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_abd.pdf"
profile_pic_path = current_dir / "assets" / "pic.jpg"
ece_logo_path = current_dir / "assets" / "ECE_Logo.jpg"
eureka_logo_path = current_dir / "assets" / "eureka_logo.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digital | Abdullah Ghani"
PAGE_ICON = ":wave:"
NAME = "Abdullah Ghani"
DESCRIPTION = """Elève ingénieur en Systèmes d'Information, Cybersécurité, Data et IA. À la recherche d'une alternance de 1 à 3 ans à partir de septembre 2024."""
EMAIL = "abdullah.ghani352001@gmail.com"
PHONE = "0621514565"
LOCATION = "Île de France, Paris"
BIRTHDATE = "03/05/2001"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)
ece_logo = Image.open(ece_logo_path)
eureka_logo = Image.open(eureka_logo_path)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(f"📫 {EMAIL}")
    st.write(f"📞 {PHONE}")
    st.write(f"📍 {LOCATION}")
    st.write(f"🎂 {BIRTHDATE}")
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Compétences Informatiques")
st.write(
    """
- 🖥️ Python
- 📊 GeoGebra, Excel, PackOffice
"""
)

st.write('\n')
st.subheader("Langues")
st.write(
    """
- Français : Langue maternelle
- Hindi : Niveau C2
- Anglais : Niveau C1
- Espagnol : Niveau B2
- Ourdou : Niveau C2
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Expériences Professionnelles et Associatives")
st.write("---")
st.write("🚧", "**Tuteur de mathématiques et de physique-chimie | EURÊKA, Goussainville**")
st.write("Depuis 2021")
st.write(
    """
- ► Enseignement des mathématiques et de la physique-chimie à des classes d'élèves allant du collège au lycée.
"""
)
st.image(eureka_logo, width=100)

st.write("🚧", "**Logistique | LA POSTE, Roissy Charles de Gaulle, France**")
st.write("Septembre 2021 - Septembre 2023")

# --- EDUCATION ---
st.write('\n')
st.subheader("Diplômes et Formations")
st.write("---")
st.write("🎓", "**Diplôme d'ingénieur | ECE Paris**")
st.write("2024 - 2027 (prévu)")
st.write("Spécialisation en Système d'information, Cybersécurité, Data et IA")
st.image(ece_logo, width=100)

st.write("🎓", "**Licence 1 et 2 Physique Mathématique renforcé | Université Paris-Saclay**")
st.write("2022 - 2024")
st.write("Mention très bien")

st.write("🎓", "**PACES (Première Année Commune aux Etudes de Santé) | Université Sorbonne Paris Nord**")
st.write("2019 - 2021")

st.write("🎓", "**Baccalauréat scientifique | Lycée Romain Rolland, Goussainville**")
st.write("2018 - 2019")
st.write("Option informatique et science du numérique")

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projets Académiques")
st.write("---")
st.write(
    """
- Création d'un automate cellulaire Turing complet
- Simulation du "Jeu de la vie" selon John Horton Conway (Python)
- Création d'un jeu vidéo sur Python (Pygame, Tkinter)
"""
)

st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write("Azure Data Fundamentals | Microsoft | Depuis 2024")
st.write("Azure AI Fundamentals | Microsoft | Depuis 2024")
st.write("EUGLOH - Communication Interculturelle | Université Paris-Saclay | Mars 2024 - Mai 2024")

st.write('\n')
st.subheader("Centres d'intérêt")
st.write("---")
st.write(
    """
- Club Karaté
- Club Rugby : Numéro 2, Talonneur
- Club Théâtre : Rôle principal dans la pièce "Le Petit Prince"
"""
)
