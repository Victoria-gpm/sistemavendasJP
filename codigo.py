import pandas as pd
import streamlit as st
import plotly.express as px



# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

# Passo a passo
# Titulo - Sistema de vendas
st.write("# Sistema de vendas")

# Seção - Cadastrar vendas
st.write("## Cadastrar Vendas")
st.sidebar.write("## Cadastrar venda")

    # Campo de data
data = st.sidebar.date_input("Data")
    # Campo vendedor - ana, bruno e carla
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
    # Campo produto - notebook, fone e celualar
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
    # Campo de quantidade
quantidade = st.sidebar.number_input("Quantidade", step=1)
    # Campo de valor
valor = st.sidebar.number_input("Valor")
    # Botão de cadastrar vendas
botao_cadastrar = st.sidebar.button("Cadastrar venda")

# logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada com sucesso!")

# Ao clicar no botão -> adicionar a venda na tabela


# Seção - Vendas cadastradas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)


    # Tabela com as vendas
# Seção - Dashboard
st.write("## Dashboard")
# Card do faturamento total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")
          
# Grafico de barra/coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)
# Grafico de pizza -> venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.45)
st.plotly_chart(grafico2)




