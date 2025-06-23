import streamlit as st
from groq import Groq
# --- 1. IMPORT FUNGSI BARU DARI FILE KNOWLEDGE ---
from chatbot_knowledge import get_knowledge_base_string

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Chat with AI Vebri", page_icon="🤖")
st.markdown('<h2 class="section-header">Chat with AI Vebri</h2>', unsafe_allow_html=True)
st.write(
    "Ajukan pertanyaan apa pun tentang pengalaman profesional, skill, atau proyek saya. "
    "Saya, sebagai versi AI dari Vebri, akan mencoba menjawabnya!"
)
st.markdown("---")

# --- 2. HAPUS BLOK KNOWLEDGE_BASE YANG LAMA ---
# --- GANTI DENGAN SATU BARIS INI ---
knowledge_base = get_knowledge_base_string()

# --- LOGIKA CHATBOT (Tidak ada perubahan di bawah ini) ---

# Inisialisasi Klien Groq
try:
    client = Groq(api_key=st.secrets["groq"]["api_key"])
except Exception as e:
    st.error("Gagal menginisialisasi klien Groq. Pastikan API Key Anda sudah benar di secrets.toml.")
    st.stop()

# Inisialisasi chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Saya adalah AI Vebri. Ada yang bisa saya bantu terkait portfolio Vebri Satriadi?"}
    ]

# Tampilkan chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Terima input dari pengguna
if prompt := st.chat_input("Tanyakan tentang pengalaman saya..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- VERSI BARU YANG LEBIH TEGAS ---

# Kita buat variabel system_prompt agar lebih rapi
    system_prompt = f"""
    Anda adalah 'AI Vebri', sebuah asisten AI yang bertugas sebagai versi digital dari portfolio Vebri Satriadi.

    ATURAN PALING PENTING:
    1.  JAWAB semua pertanyaan HANYA berdasarkan informasi yang ada di dalam "KONTEKS PENGETAHUAN" di bawah.
    2.  JIKA sebuah pertanyaan tidak bisa dijawab menggunakan konteks tersebut (misalnya pertanyaan tentang opini, perasaan, atau topik di luar portfolio), JANGAN MENGARANG JAWABAN DAN ANDA WAJIB MENOLAK untuk menjawab.
    3.  Gunakan salah satu dari dua kalimat penolakan ini:
        - "Maaf, sebagai AI yang berfokus pada data dan fakta dari portfolio Vebri, saya tidak memiliki informasi atau opini pribadi mengenai hal tersebut."
        - "Itu pertanyaan yang menarik, namun berada di luar cakupan pengetahuan yang saya miliki. Saya hanya bisa menjawab seputar pengalaman kerja, skill, dan proyek Vebri yang tercatat."
        - "Untuk pertanyaan itu mungkin anda bisa mengundang Vebri yang asli untuk melakukan wawancara :D. "
    4.  HARUS menjawab dalam bahasa yang sama dengan bahasa yang digunakan penanya (Indonesia atau Inggris).
    5.  Berperanlah sebagai AI Vebri yang ramah dan profesional.
    6.  Jika konteks pertanyaan di pesan selanjutnya SANGAT berbeda dengan sebelumnya, jangan tambahkan jawaban tentang pertanyaan konteks sebelumnya.

    KONTEKS PENGETAHUAN:
    ---
    {knowledge_base}
    ---
    """

    api_messages = [
        {"role": "system", "content": system_prompt}
    ] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(model="llama3-8b-8192", messages=api_messages, stream=True)
            placeholder = st.empty()
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menghubungi API Groq: {e}")