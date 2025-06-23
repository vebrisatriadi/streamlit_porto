# portfolio_app.py
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vebri Satriadi | Data Engineer",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
def load_css():
    """Memuat CSS kustom untuk seluruh aplikasi."""
    st.markdown("""
    <style>
        /* CSS UNTUK MEMPERSEMPIT SIDEBAR */
        [data-testid="stSidebar"] {
            width: 250px !important;
            min-width: 250px !important;
            max-width: 250px !important;
        }
        .main-header {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #1f77b4;
            margin-bottom: 2rem;
        }
        .section-header {
            font-size: 2rem;
            font-weight: bold;
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.5rem;
            margin: 2.5rem 0 1.5rem 0;
        }
        /* ... (sisa style CSS Anda yang lain) ... */
        .skill-badge-blue {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 8px 16px;
            margin: 5px;
            border-radius: 20px;
            font-size: 0.95rem;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)

# --- Memuat Aset ---
load_css()

# ====================================================================
# --- KONTEN HALAMAN HOME (VERSI BARU: HANYA GAMBAR) ---
# ====================================================================

# Membuat kolom untuk menengahkan gambar
# Angka [1, 5, 1] berarti kolom tengah 5x lebih lebar dari kolom samping

col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.image("assets/images/header.png", width=800)
with col2:
    st.image("assets/images/1.jpeg", width=800)
with col2:
    st.image("assets/images/2.jpg", width=800)
with col2:
    st.image("assets/images/4.jpg", width=800)
