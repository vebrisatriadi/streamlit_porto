import streamlit as st
from groq import Groq
from chatbot_knowledge import get_knowledge_base_string

st.set_page_config(page_title="Chat with AI Vebri", page_icon="🤖")
st.markdown('<h2 class="section-header">Chat with AI Vebri</h2>', unsafe_allow_html=True)
st.write(
    "Ask me anything about Vebri's professional experiences, skills, or projects."
    "Me, as AI's version of Vebri will answer as you want!"
)
st.markdown("---")

knowledge_base = get_knowledge_base_string()

try:
    client = Groq(api_key=st.secrets["groq"]["api_key"])
except Exception as e:
    st.error("Gagal menginisialisasi klien Groq. Pastikan API Key Anda sudah benar di secrets.toml.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! I'm AI's version of Vebri Satriadi. Can I help you with?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about my professional experience, skills, or projects..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

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

    Knowledge base:
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
            st.error(f"An error occurred while processing your request: {e}")