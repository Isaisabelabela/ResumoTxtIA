# 📄🔍 Resumo e Análise de Sentimentos de Textos com IA

Este aplicativo em Python usa **Streamlit** e **Transformers (Hugging Face)** para gerar **resumos automáticos** e realizar **análise de sentimentos** de textos (.txt ou colados diretamente).

---

## 🚀 Funcionalidades

- ✅ Upload de arquivos `.txt` ou entrada de texto manual
- ✅ Geração de **resumo automático**
- ✅ Análise de **sentimento** (positivo, neutro ou negativo)
- ✅ Interface simples com **Streamlit**
- ✅ Processamento local via Hugging Face com cache

---

## 🛠️ Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Crie um ambiente virtual (opcional, mas recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows

4. Instale as dependências
   ```bash
   pip install -r requirements.txt

## 🔐 Configuração da API (Hugging Face)
1. Crie uma conta gratuita em: https://huggingface.co
2. Gere seu token pessoal de acesso: https://huggingface.co/settings/tokens
3. Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
   ```ini
    HF_HOME=./models
    HF_TOKEN=sua_chave_aqui


## ▶️ Como executar
  ```bash
    streamlit run app.py
```
A aplicação será aberta automaticamente


## 🧪 Exemplo de texto
```css
A empresa apresentou resultados positivos no último trimestre, surpreendendo os analistas. As ações subiram após o anúncio.
```
A saída incluirá um resumo (quando o texto for longo) e o sentimento: positivo

## 📦 Requisitos
Python 3.8+

Conexão com a internet para baixar os modelos da primeira vez

## 👩‍💻 Autora

Feito com 💙 por **Isabela**

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/isabeladepaulabarbosa)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Isaisabelabela)

