import streamlit as st
from Library import estoque

st.title("Estoque de produto")

nomeProduto = st.text_input("Digite o nome do produto: ")
quantidadeProduto = st.number_input(f"Selecione a quantidade de {nomeProduto}", format="%g",step=1,min_value=1, value="min")
precoProduto = st.number_input("Qual preço do produto: ",)

if 'prod_cadastrados' not in st.session_state:
    st.session_state.prod_cadastrados = []
if 'preco_cadastrados' not in st.session_state:
    st.session_state.preco_cadastrados=[]
if 'quant_cadastradas' not in st.session_state:
    st.session_state.quant_cadastradas=[]

if st.button("Processar"):

    valorTotal = estoque(nomeProduto, quantidadeProduto, precoProduto)

    st.write(f"Produto: {nomeProduto}")
    st.write(f"Quantidade: {quantidadeProduto}")
    st.write(f"Preço unitário: {precoProduto:.2f}\n")
    st.write(f"Total: {valorTotal[1]:.2f}")

    st.session_state.prod_cadastrados.append(valorTotal[0])
    st.session_state.preco_cadastrados.append(valorTotal[1])
    st.session_state.quant_cadastradas.append(valorTotal[2])

for produtoAtual , precoAtual, quantAtual in zip(st.session_state.prod_cadastrados,st.session_state.preco_cadastrados,st.session_state.quant_cadastradas):
        st.write(f"Qt: {quantAtual} | Produto: {produtoAtual} - Preço total: {precoAtual:.2f}")


if st.button("Resetar lista"):
    if 'prod_cadastrados' in st.session_state:
            del st.session_state['prod_cadastrados']
            del st.session_state['preco_cadastrados']
            del st.session_state['quant_cadastradas']
            st.rerun()









