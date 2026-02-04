"""
Aula 004 - Saída Estruturada com JsonOutputParser e Pydantic
=============================================================

Este script demonstra como obter respostas estruturadas em JSON do modelo,
usando JsonOutputParser com validação via Pydantic.

Conceitos abordados:
- JsonOutputParser: Parser que converte a saída do modelo em JSON
- Pydantic BaseModel: Define o schema/estrutura esperada da resposta
- Field: Descreve campos e suas validações
- partial_variables: Variáveis pré-preenchidas no template
- set_debug: Ativa modo debug do LangChain para ver detalhes internos

Vantagens da saída estruturada:
- Respostas em formato JSON consistente
- Validação automática com Pydantic
- Fácil integração com outras partes do sistema
- Tratamento de erros mais robusto

Fluxo da cadeia:
    prompt_cidade -> modelo -> JsonOutputParser -> dict Python

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- langchain-core: Output parsers
- pydantic: Validação e serialização de dados
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from langchain.globals import set_debug


# Definição do modelo Pydantic para a estrutura de resposta
# O modelo define o schema JSON esperado e fornece validação automática
class DestinoTuristico(BaseModel):
    """Modelo de dados para um destino turístico sugerido."""
    cidade: str = Field(..., description="Nome da cidade sugerida")
    motivo: str = Field(..., description="Motivo pelo qual a cidade é recomendada")


def main():
    """
    Função principal que demonstra saída estruturada com JsonOutputParser.
    
    Fluxo de execução:
    1. Ativa o modo debug do LangChain
    2. Carrega variáveis de ambiente
    3. Cria um JsonOutputParser com o modelo Pydantic
    4. Cria um prompt que inclui instruções de formato
    5. Executa a cadeia e obtém um dicionário Python
    """
    # Ativa o modo debug para visualizar detalhes internos do LangChain
    # Útil para entender o fluxo e depurar problemas
    set_debug(True)

    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')

    # Cria o parser JSON baseado no modelo Pydantic
    # O parser irá validar e converter a resposta do modelo
    parseador = JsonOutputParser(pydantic_object=DestinoTuristico)

    # Cria o template de prompt com instruções de formato
    # - partial_variables: Injeta automaticamente as instruções de formato JSON
    # - get_format_instructions(): Gera instruções para o modelo retornar JSON válido
    prompt_cidade = PromptTemplate(
        template="Sugira uma cidade dado o meu interesse por {interesse}.{formato_de_saida}",
        input_variables=["interesse"],
        partial_variables={"formato_de_saida": parseador.get_format_instructions()}
    )
       
    # Inicialização do modelo
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Criação da cadeia com LCEL
    # O parseador no final converte a resposta em dicionário Python
    cadeia = prompt_cidade | modelo | parseador

    # Invoca a cadeia - o resultado é um dicionário, não uma string
    # Exemplo de resposta: {"cidade": "Florianópolis", "motivo": "Belas praias..."}
    resposta = cadeia.invoke({"interesse": "praias"})
    print(resposta)


if __name__ == "__main__":
    main()