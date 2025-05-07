# 📦 Gerenciamento de Estoque Simples com Streamlit

Uma aplicação Streamlit para gerenciar o estoque de produtos de forma interativa.

## 🚀 O que é Streamlit?

Streamlit é uma biblioteca Python de código aberto que simplifica a criação e o compartilhamento de aplicativos web personalizados para diversas finalidades, incluindo a criação de interfaces de usuário para scripts Python sem a necessidade de conhecimento em desenvolvimento web.

## 🛠️ Tecnologias e Conceitos Utilizados

Este projeto foi construído utilizando as seguintes tecnologias e conceitos do Streamlit:

### ⌨️ Entrada de Dados com `st.text_input` e `st.number_input`

Utilizamos `st.text_input` para permitir que o usuário digite o nome do produto e `st.number_input` para coletar a quantidade e o preço do produto de forma numérica e controlada.

### 💾 Gerenciamento de Estado com `st.session_state`

O `st.session_state` é crucial para persistir informações entre as interações do usuário. Neste projeto, ele gerencia as listas de:

* Produtos cadastrados (`prod_cadastrados`).
* Preços totais calculados para cada produto (`preco_cadastrados`).
* Quantidades de cada produto cadastrado (`quant_cadastradas`).

### 🖱️ Interação com `st.button`

Os botões (`st.button`) são utilizados para acionar ações específicas:

* **Processar:** Calcula o preço total do produto e armazena as informações.
* **Resetar lista:** Limpa todos os produtos cadastrados, reiniciando o estado da aplicação.

### 🖋️ Exibição com `st.write`

A função `st.write` é empregada para exibir informações importantes na interface, como:

* Os detalhes do produto recém-processado (nome, quantidade, preço unitário e total).
* A lista de todos os produtos cadastrados com suas respectivas quantidades e preços totais.

### 🔄 Atualização da Interface com `st.rerun`

A função `st.rerun()` é utilizada no botão de "Resetar lista" para forçar a atualização imediata da interface após a limpeza dos dados, garantindo que a lista de produtos seja removida da tela.

### 🔗 Importação de Módulo com `from Library import estoque`

O projeto demonstra como importar funções de outros arquivos Python (`Library.py` neste caso), utilizando a instrução `from Library import estoque` para acessar a lógica de cálculo do estoque.

## 🧪 Teste o Gerenciador de Estoque Online!

Você pode experimentar esta aplicação de gerenciamento de estoque diretamente no Streamlit Community Cloud:

[https://estoquegustavobritto.streamlit.app](https://estoquegustavobritto.streamlit.app)

## ⏭️ Próximos Passos (Melhorias Futuras)

Este projeto pode ser expandido com as seguintes funcionalidades:

* Permitir a edição ou exclusão de itens da lista de estoque.
* Adicionar funcionalidades de filtragem e ordenação da lista de produtos.
* Implementar uma interface mais visual para a exibição dos dados, como tabelas.
* Persistir os dados em um armazenamento mais robusto (banco de dados, arquivos).
* Adicionar validações de entrada para garantir a integridade dos dados.
* Implementar funcionalidades de busca de produtos.

## 🎯 Objetivo

O principal objetivo deste repositório é ilustrar o uso da biblioteca Streamlit para criar uma aplicação interativa de gerenciamento de dados, demonstrando conceitos como entrada de dados, gerenciamento de estado e interação com o usuário, além da importação de módulos externos.
