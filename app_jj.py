from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "jj.pdf"
esilv_logo_path = current_dir / "assets" / "ESILV_logo.jpg"
saclay_logo_path = current_dir / "assets" / "Saclay.jpg"
eureka_logo_path = current_dir / "assets" / "eureka_logo.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digital | Jhon Picka"
PAGE_ICON = ":wave:"
NAME = "Jhon Picka"
DESCRIPTION = """
Polyvalent, organisé et passionné, j'utilise les données pour prendre des décisions qui ont un impact positif, notamment pour les défis techniques liés à l'énergie."""

ALTERNANCE = "Contrat apprentissage 2024/2027, Rythme : 2 jours entreprise / 3 jours école"
EMAIL = "Picka.jhon@hotmail.com"
PHONE = "06 35 43 55 35"
LOCATION = "Paris, France"
AVAILABLE = "Rythme : 2 jours entreprise / 3 jours école"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD PDF & IMAGES ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Load images
esilv_logo = Image.open(esilv_logo_path)
saclay_logo = Image.open(saclay_logo_path)
eureka_logo = Image.open(eureka_logo_path)

# --- PROFILE SECTION ---
st.title(NAME)
st.markdown("<p style='color: #800020;'><strong>INGÉNIEUR DATA ANALYST- ÉNERGIE & VILLES DURABLES</strong></p>", unsafe_allow_html=True)
st.write(DESCRIPTION)
st.markdown(f"<p style='color: green ;'>📫 {EMAIL}</p>", unsafe_allow_html=True)
st.write(f"📞 {PHONE} | 📍 {LOCATION}")
st.write(f"**{AVAILABLE}**")
st.download_button(
    label="📄 Télécharger le CV",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)

# --- MAIN CONTAINER ---
with st.container():
    st.markdown("""<style>
    .stContainer {
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
    }
    </style>""", unsafe_allow_html=True)
    
        # --- EDUCATION ---
    with st.expander("Diplômes & Formations"):
        st.subheader("Diplômes & Formations")
        st.write("---")
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("🎓", "**École d’ingénieur ESILV** | Pôle Léonard de VINCI")
            st.write("Septembre 2024 - Juin 2027 (Majeure : Énergie & Villes Durables)")
            st.write("🎓", "**Licence Physique | Université Paris-Saclay**")
            st.write("Depuis Septembre 2022")
            st.write(
                """
                - ► 1ère année validée mention assez bien.
                - ► 2ème année axée sur la Physique et les Mathématiques.
                """
            )
        with col2:
            st.image(esilv_logo, width=120)
            st.image(saclay_logo, width=120)
            
    # --- SKILLS ---
    with st.expander("Compétences Techniques & Soft Skills"):
        st.subheader("Compétences Techniques & Soft Skills")
        st.write(
            """
            - **Langages Informatiques** : C, Python, VBA.
            - **Modélisation** : Matlab, Solidworks, Sweet Home 3D.
            - **Traitement de Données** : Excel, VBA.
            - **Physique Théorique** : Rhéologie, Électronique.
            """
        )
        st.write(
            """
            - **Organisation**
            - **Sens relationnel**
            - **Polyvalence**
            """
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    with st.expander("Expériences Professionnelles"):
        st.subheader("Expériences Professionnelles")
        st.write("---")
        st.write("🚧", "**Intervenant en Mathématiques et Physique | Mairie de Goussainville**")
        st.write("Juin 2020 - Août 2020")
        st.write(
            """
            - ► Dispenser des cours de mathématiques et physique.
            - ► Approfondir les notions avec les étudiants.
            - ► Collaboration en équipe pour améliorer l'expérience pédagogique.
            """
        )

        st.write("🚧", "**Employé polyvalent | Pizza Time, Gennevilliers**")
        st.write("Août 2019 - Juillet 2022")
        st.write(
            """
            - ► Gestion de la relation client, gestion des stocks et du personnel.
            - ► Livreur et soutien aux opérations quotidiennes.
            """
        )



    # --- HOBBIES & INTERESTS ---
    with st.expander("Loisirs"):
        st.subheader("Loisirs")
        st.write("---")
        st.write(
            """
            - ⚽ **Football** : Club de Goussainville.
            - 🎸 **Guitare** : Conservatoire de Goussainville.
            - 🎵 **Solfège** : Conservatoire de Goussainville.
            """
        )

    # --- FOOTER ---
    with st.expander("Langues"):
        st.write("Langues : Anglais courant, Espagnol débutant")
