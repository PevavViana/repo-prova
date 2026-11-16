import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Leito Ocupação", layout="wide", page_icon="🐍")
caminho_arquivo = "esus-vepi.LeitoOcupacao_2020.csv"

@st.cache_data
def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, sep=";")
    df["mes"]    = df["dataNotificacao"].astype(str).str[5:7]
    df["estado"] = "MinasGerais"
    df["ocupacao"] = df["ocupacaoConfirmadoUti"].mul(df["mes"].astype(int))
    
    return df

try:
    df = carregar_dados(caminho_arquivo)

    st.sidebar.header("🔍 Filtros")

    # Filtro dos tipos de visualização
    graficos_selecionados = st.sidebar.selectbox(
        "Selecione o tipo de visualização:",
        options=["Tabela", "Grafico"],
    )

    st.title("📊 Leito Ocupação")
    df

except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.info("Certifique-se de que o arquivo 'esus-vepi.LeitoOcupacao_2020.csv' está no mesmo diretório do script.")

