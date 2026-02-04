"""
Aula 003 - Introdução às Cadeias (Chains) com LCEL
===================================================

Este script demonstra o uso de cadeias (chains) usando LCEL (LangChain Expression Language).
LCEL é a forma moderna e recomendada de criar pipelines no LangChain.

Conceitos abordados:
- PromptTemplate: Template simples para prompts
- Operador pipe (|): Conecta componentes em uma cadeia
- StrOutputParser: Extrai texto puro da resposta do modelo
- LCEL (LangChain Expression Language): Sintaxe declarativa para cadeias

Vantagens do LCEL:
- Sintaxe limpa e legível com operador |
- Composição fácil de componentes
- Suporte nativo a streaming e execução assíncrona
- Melhor performance e debugging

Fluxo da cadeia:
    prompt_cidade -> modelo -> StrOutputParser -> resposta (string)

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- langchain-core: Componentes principais como output parsers
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main():
    """
    Função principal que demonstra o uso de cadeias com LCEL.
    
    Fluxo de execução:
    1. Carrega variáveis de ambiente
    2. Cria um PromptTemplate para sugestão de cidades
    3. Inicializa o modelo ChatOpenAI
    4. Cria uma cadeia usando o operador pipe (|)
    5. Invoca a cadeia e exibe o resultado como string
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')

    # Criação do PromptTemplate
    # - template: String com placeholders {variavel}
    # - input_variables: Lista de variáveis esperadas (validação)
    prompt_cidade = PromptTemplate(
        template="Sugira uma cidade dado o meu interesse por {interesse}.",
        input_variables=["interesse"],
    )
       
    # Inicialização do modelo
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Criação da cadeia usando LCEL (operador pipe)
    # Fluxo: prompt -> modelo -> parser
    # - PromptTemplate formata a entrada
    # - ChatOpenAI processa e gera resposta
    # - StrOutputParser extrai apenas o texto da resposta
    cadeia = prompt_cidade | modelo | StrOutputParser()

    # Invoca a cadeia passando um dicionário com as variáveis
    # O resultado é uma string limpa graças ao StrOutputParser
    resposta = cadeia.invoke({"interesse": "praias"})
    print(resposta)


if __name__ == "__main__":
    main()