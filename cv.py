from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.jpg"
video_file_path = current_dir / "assets" / "video.mp4"
qrcode_image_path = current_dir / "assets" / "qrcode.jpg"
eureka_logo_path = current_dir / "assets" / "eureka_logo.jpeg"
efrei_logo_path = current_dir / "assets" / "logo_efrei.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digital | Adiba Ghani"
PAGE_ICON = ":wave:"
NAME = "Adiba Ghani"
DESCRIPTION = """Hello, je m'appelle Adiba et je suis à la recherche d'un nouveau défi en tant que Chargée de communication. Diplômée d'un Baccalauréat STMG avec une spécialisation en Ressources Humaines et Communication, j'ai été acceptée à l'EFREI Paris pour un BTS Communication."""
EMAIL = "ghaniadiba7@gmail.com"
DATE = "Disponible à partir de Septembre 2024"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)
qrcode_image = Image.open(qrcode_image_path)
eureka_logo = Image.open(eureka_logo_path)
efrei_logo = Image.open(efrei_logo_path)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.markdown(f"**{DATE}**", unsafe_allow_html=True)  # Ajout de la date
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Expérience & Qualifications")
st.write(
    """
- ✔️ Expérience en animation d'ateliers et de cours pour des collégiens
- ✔️ Compétences en gestion de projets de communication
- ✔️ Connaissances solides en Photoshop, Excel, et Microsoft Office
- ✔️ Maîtrise des outils de gestion de médias sociaux comme TikTok, Instagram et Facebook
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Compétences Techniques")
st.write(
    """
- 📊 Visualisation de données : Excel
- 🌐 Outils de gestion de contenu : Wordpress, Wix
- 🎨 Design : Photoshop, Illustrator, Canva
- 📱 Médias sociaux : TikTok, Instagram, Facebook, LinkedIn
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Historique Professionnel")
st.write("---")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("🚧", "**Volontaire | Eureka, Goussainville**")
    st.write("Septembre 2022 - Août 2024")
    st.write(
        """
    - ► Préparation d'ateliers et de leçons en anglais et en français pour des collégiens avec un tuteur
    - ► Aide à l'organisation d'événements communautaires et d'activités
    """
    )
with col2:
    st.image(eureka_logo, width=100)

# --- EDUCATION ---
st.write('\n')
st.subheader("Formation")
st.write("---")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("🎓", "**BTS Communication | EFREI Paris**")
    st.write("2024 - 2026 (acceptée)")
    st.write(
        """
    - ► Formation aux stratégies de communication, techniques de production et de diffusion de contenus, gestion de projets de communication, utilisation des outils numériques et des médias sociaux
    """
    )
with col2:
    st.image(efrei_logo, width=100)

st.write("🎓", "**Baccalauréat STMG, Spécialisation Ressources Humaines et Communication**")
st.write("2022 - 2024")
st.write(
    """
- ► Management des organisations
- ► Sciences de gestion et numérique
- ► Droit et économie
- ► Communication et gestion des ressources humaines
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projets & Réalisations")
st.write("---")
st.video(str(video_file_path), format="video/mp4")
st.write("""
Cette vidéo a été réalisée avec Canva et la musique a été générée à l'aide de l'outil UdIO, un générateur de musique à partir d'un prompt. 
Produire avec des outils numériques est l'une de mes passions, et je suis enthousiaste à l'idée d'explorer les possibilités offertes par l'intelligence artificielle pour augmenter la productivité et la créativité.
""")
st.image(qrcode_image, width=150)
st.markdown("""
<p style="color: red; font-weight: bold;">
<a href="https://www.tiktok.com/@tech_chan/video/7381408176266087713" style="color: red; font-weight: bold; text-decoration: none;">
Vidéo TikTok utilisant l'IA générative
</a>
</p>
""", unsafe_allow_html=True)
st.write("""
Pour cette vidéo, j'ai utilisé l'IA générative UdIO pour écrire une chanson dont les paroles ont été rédigées par ChatGPT. J'ai ensuite envoyé ces paroles au modèle UdIO pour créer une musique destinée à rendre plus ludique l'apprentissage de la philosophie sur le thème de la "justice".
""")
st.markdown(
    """
    <style>
    .side-image {
        position: fixed;
        right: 0;
        top: 0;
        width: 25%;
        height: auto;
        opacity: 0.95;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the side image
st.markdown(
    """
    <img src="https://img.freepik.com/vecteurs-premium/stylo-plume-or-fer_105895-332.jpg" class="side-image">
    """,
    unsafe_allow_html=True
)