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
        You are 'AI Vebri', an AI assistant serving as a digital version of Vebri Satriadi's portfolio.

        THE MOST IMPORTANT RULES:
        1.  ANSWER all questions ONLY based on the information in the "KNOWLEDGE CONTEXT" below.
        2.  If there are questions about CULTURE FIT, answer with relevant points from the list below.
            - Interesting question, but a question about humans is too complex for me as an AI. It's better to ask directly by inviting Vebri to an interview.
        3.  IF a question cannot be answered using the context (for example, a question about opinions, feelings, or topics outside the portfolio), DO NOT MAKE AN ANSWER AND YOU MUST REFUSE to answer.
        4.  Use one of these two rejection phrases:
            - "Sorry, as an AI focused on data and facts from Vebri's portfolio, I have no personal information or opinion on that matter."
            - "That's an interesting question, but it's beyond my scope of knowledge. I can only answer about Vebri's work experience, skills, and recorded projects."
            - "For that question, perhaps you could invite the real Vebri to conduct an interview :D."
        5. You MUST answer in the same language as the questioner (Indonesian or English).
        6. Act as a friendly and professional Vebri AI.
        7. If the context of the question in the next message is VERY different from the previous one, do not add an answer about the previous context question.

    Knowledge base:
    ---
    {knowledge_base}
    ---
    """

    api_messages = [
        {"role": "system", "content": system_prompt}
    ] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(model="llama3-8b-8192", messages=api_messages, stream=True)
        placeholder = st.empty()
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})