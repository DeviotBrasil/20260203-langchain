"""
Aula 002 - Usando ChatPromptTemplate no LangChain
==================================================

Este script demonstra o uso de ChatPromptTemplate para criar prompts estruturados
com mensagens de sistema e usuário separadas.

Conceitos abordados:
- ChatPromptTemplate: Template de prompts para conversação
- Mensagens de sistema vs usuário
- Variáveis de template com placeholders {}
- Formatação de prompts com .format()

Vantagens do ChatPromptTemplate:
- Separa instruções de sistema do pedido do usuário
- Permite reutilização de templates
- Facilita a manutenção e testes
- Suporta validação de variáveis

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- langchain: Framework principal com templates de prompt
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def main():
    """
    Função principal que demonstra o uso de ChatPromptTemplate.
    
    Fluxo de execução:
    1. Carrega variáveis de ambiente
    2. Define parâmetros personalizáveis
    3. Cria um template de prompt com mensagens de sistema e usuário
    4. Formata o prompt com os valores das variáveis
    5. Invoca o modelo e exibe a resposta
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')
    
    # Parâmetros personalizáveis para o plano de atividades
    numero_dias = 7
    numero_criancas = 2
    atividade = "música"

    # Criação do ChatPromptTemplate com mensagens estruturadas
    # - "system": Define o comportamento/persona do assistente
    # - "user": Contém o pedido do usuário com variáveis entre {}
    # Isso permite maior controle sobre como o modelo responde
    modelo_prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente criativo que ajuda a criar planos de atividades para crianças."),
        ("user", "Crie um plano de atividades para {numero_dias} dias para {numero_criancas} crianças, focando em atividades relacionadas a {atividade}. Cada dia deve incluir uma atividade principal e uma breve descrição.")
    ])

    # Formata o template substituindo as variáveis pelos valores
    # O método .format() retorna uma string formatada
    prompt = modelo_prompt.format(
        numero_dias=numero_dias, 
        numero_criancas=numero_criancas, 
        atividade=atividade
    )

    # Exibe informações de debug para verificar o prompt gerado
    print("Gerando plano de atividades...")
    print("Prompt enviado para o modelo:")
    print(prompt)
    
    # Inicialização do modelo ChatOpenAI
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Invoca o modelo e exibe a resposta
    resposta = modelo.invoke(prompt)
    print("Plano de Atividades:")
    print(resposta)


if __name__ == "__main__":
    main()