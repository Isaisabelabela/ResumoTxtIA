import streamlit as st
from transformers import pipeline

@st.cache_resource
def carregar_modelos():
    resumo = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", framework="pt")
    sentimento = pipeline("sentiment-analysis", framework="pt")
    return resumo, sentimento

resumidor, analisador_sentimento = carregar_modelos()

st.title("🧠📄 Resumo + análise de sentimento com IA (Local)")

entrada = st.radio("Como deseja inserir o texto?", ["Arquivo .txt", "Copiar e colar"])

texto = ""

if entrada == "Arquivo .txt":
    arquivo = st.file_uploader("Selecione um arquivo .txt", type=["txt"])
    if arquivo:
        texto = arquivo.read().decode("utf-8")
else:
    texto = st.text_area("Cole o texto aqui:", height=200)

if texto:
    st.subheader("Texto Original")
    st.text_area("Texto completo", texto, height=200, disabled=True)

    if st.button("Analisar"):
        texto_cortado = texto[:3000]  

        with st.spinner("Gerando resumo..."):
            resumo = resumidor(texto_cortado, max_length=150, min_length=40, do_sample=False)[0]['summary_text']

        with st.spinner("Analisando sentimento..."):
            resultado = analisador_sentimento(texto_cortado)[0]

        st.subheader("📌 Resumo")
        st.success(resumo)

        st.subheader("Análise de Sentimento")
        st.write(f"**Sentimento:** {resultado['label']}")
        st.write(f"**Confiança:** {round(resultado['score'] * 100, 2)}%")
