# 🍎 Sistema de Gestão de Inventário: Varejão Gen

Este projeto simula o controle de estoque de um hortifruti utilizando **Python**. O foco principal foi criar um sistema interativo que permite ao usuário gerenciar uma lista de produtos de forma dinâmica através do console.

---

### 💡 O Desafio
O objetivo foi construir uma interface simples de linha de comando (CLI) que aplicasse os conceitos de **CRUD** (Create, Read, Update, Delete). O sistema permite que dados sejam armazenados em memória, manipulados e visualizados enquanto o programa estiver em execução.

---

### 🔍 O que eu aprendi e apliquei

#### 1. Manipulação Dinâmica de Listas
Entendi que listas em Python são estruturas poderosas para armazenar coleções de dados que mudam de tamanho durante o uso:
* **`append()`**: Utilizado para anexar novos produtos ao final da lista de forma organizada.
* **`pop()`**: Fundamental para a funcionalidade de exclusão, removendo itens baseando-se no índice informado pelo usuário.

#### 2. Lógica de Repetição e Fluxo (Loops & Condicionais)
Para garantir que o sistema fosse contínuo e não fechasse após uma única ação, implementei:
* **Estrutura `while`**: Cria um loop que mantém o menu ativo até que o usuário decida explicitamente "Sair" (`break`).
* **Validação de Entrada**: Uso de blocos `if/elif/else` para tratar as escolhas do usuário e garantir que apenas opções válidas sejam processadas.

#### 3. UX (User Experience) no Terminal
Busquei tornar o sistema amigável para pessoas que não são da área técnica:
* **`enumerate()`**: No momento da exclusão, o sistema numera os produtos na tela começando pelo "1". Isso traduz a "lógica de programação" (que começa no 0) para a "lógica humana", facilitando a escolha do usuário.
* **Feedback de Ação**: O sistema sempre confirma quando uma fruta foi adicionada ou removida com sucesso, evitando incertezas.

---

### 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Lógica de Programação Estruturada**
* **Conceitos de Memória Volátil**

---

### 🚀 Como funciona o sistema
1. Ao iniciar, o sistema exibe um **Varejão Digital**.
2. **Opção 01**: Adiciona uma nova fruta à lista.
3. **Opção 02**: Lista os produtos numerados e permite excluir um deles pela posição.
4. **Opção 03**: Exibe todos os itens salvos no momento.
5. **Opção 04**: Finaliza o sistema com uma mensagem de despedida.

---

### 🧠 Reflexão Técnica
"Este projeto foi essencial para consolidar minha base em algoritmos. Gerenciar o fluxo de um programa através de menus interativos é o primeiro passo para entender como softwares maiores e bancos de dados operam no mundo real."

---
Desenvolvido por Hirlandia 🚀
