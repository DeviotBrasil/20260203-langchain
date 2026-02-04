"""
Aula 001 - Introdução ao LangChain com OpenAI
=============================================

Este script demonstra o uso básico do LangChain para interagir com a API da OpenAI.
É o exemplo mais simples de como criar uma chamada ao modelo GPT-3.5-turbo.

Conceitos abordados:
- Configuração de variáveis de ambiente com python-dotenv
- Inicialização do modelo ChatOpenAI
- Criação de prompts simples com f-strings
- Invocação direta do modelo e obtenção de resposta

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


def main():
    """
    Função principal que demonstra o uso básico da API da OpenAI com LangChain.
    
    Fluxo de execução:
    1. Carrega variáveis de ambiente do arquivo .env
    2. Obtém a chave da API da OpenAI
    3. Define parâmetros do plano de atividades
    4. Cria um prompt usando f-string
    5. Inicializa o modelo ChatOpenAI
    6. Invoca o modelo e exibe a resposta
    """
    # Carrega as variáveis de ambiente do arquivo .env
    # O arquivo .env deve conter: OPENAI_API_KEY=sua-chave-aqui
    load_dotenv()
    
    # Obtém a chave da API da variável de ambiente
    # Isso evita expor a chave diretamente no código
    api_key = os.getenv('OPENAI_API_KEY')
    
    # Parâmetros para personalização do plano de atividades
    numero_dias = 7          # Quantidade de dias do plano
    numero_criancas = 2      # Número de crianças participantes
    atividade = "música"     # Tema principal das atividades

    # Criação do prompt usando f-string
    # Este é o método mais simples, mas não permite reutilização fácil
    prompt = (f"Crie um plano de atividades para {numero_dias} dias para {numero_criancas} crianças, "
              f"focando em atividades relacionadas a {atividade}. "
              "Cada dia deve incluir uma atividade principal e uma breve descrição.")
    
    # Inicialização do modelo ChatOpenAI
    # - model_name: Modelo a ser utilizado (gpt-3.5-turbo é mais econômico)
    # - temperature: Controla a criatividade (0=determinístico, 1=criativo)
    # - max_tokens: Limita o tamanho da resposta
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Invoca o modelo com o prompt e obtém a resposta
    # O método invoke() é a forma padrão de chamar o modelo no LangChain
    resposta = modelo.invoke(prompt)
    
    # Exibe o resultado
    print("Plano de Atividades:")
    print(resposta)


if __name__ == "__main__":
    main()