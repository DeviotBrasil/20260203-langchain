"""
Aula 005 - Encadeamento de Múltiplas Cadeias (Chain Chaining)
==============================================================

Este script demonstra como encadear múltiplas cadeias, onde a saída de uma
cadeia alimenta a entrada da próxima, criando um fluxo de processamento complexo.

Conceitos abordados:
- Múltiplos modelos Pydantic para diferentes tipos de resposta
- Encadeamento sequencial de cadeias
- Passagem de dados entre cadeias
- Composição de cadeias complexas

Fluxo do pipeline:
    1. cadeia_1: interesse -> cidade (DestinoTuristico)
    2. cadeia_2: cidade -> restaurante (Restaurante)  
    3. cadeia_3: cidade -> atividade cultural (string)

Importante:
- A saída de cada cadeia deve ser compatível com a entrada da próxima
- O encadeamento usa os campos do dict retornado pela cadeia anterior

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


# Modelo para a primeira etapa: sugestão de destino turístico
class DestinoTuristico(BaseModel):
    """Modelo de dados para um destino turístico sugerido."""
    cidade: str = Field(..., description="Nome da cidade sugerida")
    motivo: str = Field(..., description="Motivo pelo qual a cidade é recomendada")


# Modelo para a segunda etapa: sugestão de restaurante
class Restaurante(BaseModel):
    """Modelo de dados para um restaurante sugerido."""
    cidade: str = Field(..., description="Nome da cidade sugerida")
    restaurante: str = Field(..., description="Nome do restaurante recomendado")    


def main():
    """
    Função principal que demonstra encadeamento de múltiplas cadeias.
    
    Fluxo de execução:
    1. Cadeia 1: Recebe interesse e sugere uma cidade (JSON)
    2. Cadeia 2: Recebe cidade e sugere um restaurante (JSON)
    3. Cadeia 3: Recebe cidade e sugere atividade cultural (string)
    
    As cadeias são conectadas sequencialmente, onde a saída de uma
    alimenta a entrada da próxima.
    """
    # Ativa modo debug para visualizar o fluxo interno
    set_debug(True)

    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')

    # Criação dos parsers para cada tipo de resposta estruturada
    parseador_destino = JsonOutputParser(pydantic_object=DestinoTuristico)
    parseador_restaurante = JsonOutputParser(pydantic_object=Restaurante)

    # Prompt 1: Sugestão de cidade baseada no interesse
    prompt_cidade = PromptTemplate(
        template="Sugira uma cidade dado o meu interesse por {interesse}.{formato_de_saida}",
        input_variables=["interesse"],
        partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()}
    )

    # Prompt 2: Sugestão de restaurante baseada na cidade
    # Nota: {cidade} será preenchida pela saída da cadeia anterior
    prompt_restaurante = PromptTemplate(
        template="Sugira um restaurante dado o meu interesse por {cidade}.{formato_de_saida}",
        partial_variables={"formato_de_saida": parseador_restaurante.get_format_instructions()}
    )

    # Prompt 3: Sugestão de atividade cultural baseada na cidade
    prompt_cultural = PromptTemplate(
        template="Sugira atividade cultural dada a minha sugestão de cidade {cidade} ",
    )
       
    # Inicialização do modelo (compartilhado entre as cadeias)
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    # Criação das cadeias individuais
    # Cadeia 1: interesse -> {cidade, motivo}
    cadeia_1 = prompt_cidade | modelo | parseador_destino
    
    # Cadeia 2: cidade -> {cidade, restaurante}
    cadeia_2 = prompt_restaurante | modelo | parseador_restaurante
    
    # Cadeia 3: cidade -> string com atividade cultural
    cadeia_3 = prompt_cultural | modelo | StrOutputParser()

    # Encadeamento das cadeias em sequência
    # A saída de cada cadeia é passada como entrada para a próxima
    cadeia = (cadeia_1 | cadeia_2 | cadeia_3)

    # Invoca a cadeia completa
    # Fluxo: {interesse: "praias"} -> cidade -> restaurante -> atividade cultural
    resposta = cadeia.invoke({"interesse": "praias"})
    print(resposta)


if __name__ == "__main__":
    main()