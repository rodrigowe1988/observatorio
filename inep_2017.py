#importando as bibliotecas
import pandas as pd
import streamlit as st

#importando os dados de 2017
df_17 = pd.read_csv("DM_CURSO.csv", delimiter='|')

st.title("Cursos disponíveis nas Universidades brasileiras (2017)")
st.text('')
st.text('')
st.image('inep.jpg')
st.markdown("""
    Esse bancos de dados foi extraído do [site do INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior) 
    corresponde aos mais de **35 mil** cursos ofertados pelas Universidades Brasileiras.
""")

#soma da coluna QT_MATRICULA_TOTAL com os seguintes filtros:
#- TP-CATEGORIA_ADMINISTRATIVA == 2)
#- TP_ORGANIZACAO_ACADEMICA == 1
#- CO_UF == 42 (equivalente ao Estado de SANTA CATARINA)
#- TP-GRAU_ACADEMICO == 2

if st.sidebar.checkbox('Visualizar cabeçalho da tabela? '):
    st.header("Cabeçalho da tabela DM_CURSO.csv:")
    st.write(df_17.head())
    st.markdown("""
        **Fonte:** INEP
        """)

st.sidebar.info(f"O Dataset de 2017 completo possui {df_17.shape[0]} linhas e {df_17.shape[1]} colunas.")

if st.sidebar.checkbox('Visualizar colunas da tabela? '):
    st.header('Variáveis da tabela e seus respectivos tipos: ')
    st.write(df_17.dtypes)

if st.sidebar.checkbox('Dados faltantes: '):
    st.header('Quantidade de dados faltantes no dataset(%): ')
    st.write((df_17.isnull().sum() / df_17.shape[0] * 100).sort_values(ascending=False))

#filtros que a Dani solicitou a comparação com o banco de dados da Digitro e do Inep
df_dani = (df_17[(df_17.CO_UF == 42) & (df_17.TP_CATEGORIA_ADMINISTRATIVA == 2) & (df_17.TP_ORGANIZACAO_ACADEMICA == 1) & (df_17.TP_GRAU_ACADEMICO == 2)])
df_dani_2 = (df_17[(df_17.CO_UF == 29) & (df_17.TP_CATEGORIA_ADMINISTRATIVA == 2) & (df_17.TP_ORGANIZACAO_ACADEMICA == 1) & (df_17.TP_GRAU_ACADEMICO == 2)])
df_dani_3 = (df_17[(df_17.CO_UF == 51) & (df_17.TP_CATEGORIA_ADMINISTRATIVA == 2) & (df_17.TP_ORGANIZACAO_ACADEMICA == 1) & (df_17.TP_GRAU_ACADEMICO == 1)])

if st.sidebar.checkbox('Visualizar Filtro 1: '):
    st.header('UF: SC / Universidade Estadual e Pública / Licenciatura ')
    st.write(df_dani)
    st.markdown("""
            **Fonte:** INEP
            """)
    st.write(f'A soma dos dados da coluna QT_MATRICULA_TOTAL desse dataframe filtrado é {sum(df_dani.QT_MATRICULA_TOTAL)}.')

if st.sidebar.checkbox('Visualizar  Filtro 2:'):
    st.header('UF: BA / Universidade Estadual e Pública / Licenciatura')
    st.write(df_dani_2)
    st.markdown("""
            **Fonte:** INEP
            """)
    st.write(f'A soma dos dados da coluna QT_MATRICULA_TOTAL desse dataframe filtrado é {sum(df_dani_2.QT_MATRICULA_TOTAL)}.')

if st.sidebar.checkbox('Visualizar Filtro 3: '):
    st.header('UF: MT / Universidade Estadual e Pública / Bacharelado')
    st.write(df_dani_3)
    st.markdown("""
            **Fonte:** INEP
            """)
    st.write(f'A soma dos dados da coluna QT_INGRESSOS_TOTAL desse dataframe filtrado é {sum(df_dani_3.QT_INGRESSO_TOTAL)}.')

