"""
Aula 006 - Revisão: Cadeias Simples com LCEL
=============================================

Este script é uma revisão/consolidação dos conceitos de cadeias simples
com LCEL (LangChain Expression Language), similar à aula003.

Conceitos revisados:
- PromptTemplate: Template básico para prompts
- Operador pipe (|): Sintaxe LCEL para encadeamento
- StrOutputParser: Extração de texto da resposta
- Invocação de cadeias com dicionários

Caso de uso:
- Sugestão de cidades baseada em interesses do usuário
- Exemplo prático de aplicação de LLM para recomendações

Fluxo da cadeia:
    {interesse: "praias"} -> PromptTemplate -> ChatOpenAI -> StrOutputParser -> string

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- langchain-core: Output parsers
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def main():
    """
    Função principal que demonstra uma cadeia simples com LCEL.
    
    Esta aula serve como revisão e consolidação dos conceitos
    aprendidos nas aulas anteriores sobre cadeias básicas.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')

    # Criação do template de prompt simples
    # Define como a entrada do usuário será formatada para o modelo
    prompt_cidade = PromptTemplate(
        template="Sugira uma cidade dado o meu interesse por {interesse}.",
        input_variables=["interesse"],
    )
       
    # Inicialização do modelo ChatOpenAI
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Criação da cadeia usando LCEL
    # prompt_cidade: Formata a entrada
    # modelo: Processa e gera resposta
    # StrOutputParser: Extrai o texto da resposta
    cadeia = prompt_cidade | modelo | StrOutputParser()

    # Executa a cadeia com o interesse do usuário
    # Retorna uma string com a sugestão de cidade
    resposta = cadeia.invoke({"interesse": "praias"})
    print(resposta)


if __name__ == "__main__":
    main()