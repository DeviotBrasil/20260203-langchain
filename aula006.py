"""
Aula 006 - Memória de Conversação com RunnableWithMessageHistory
================================================================

Este script demonstra como adicionar memória de conversação a uma cadeia LCEL
usando RunnableWithMessageHistory, permitindo que o modelo mantenha contexto
entre múltiplas interações.

Conceitos abordados:
- ChatPromptTemplate com placeholder para histórico
- InMemoryChatMessageHistory: Armazenamento de mensagens em memória
- RunnableWithMessageHistory: Wrapper que adiciona memória a cadeias
- Gerenciamento de sessões para múltiplas conversas
- Operador pipe (|): Sintaxe LCEL para encadeamento

Caso de uso:
- Chatbot de recomendação de cidades turísticas
- Conversa multi-turno com contexto preservado

Fluxo da cadeia:
    {query, historico} -> ChatPromptTemplate -> ChatOpenAI -> StrOutputParser -> string
                              ↑
                    RunnableWithMessageHistory (gerencia histórico por sessão)

Dependências:
- langchain-openai: Integração do LangChain com OpenAI
- langchain-core: Output parsers, histórico de mensagens
- python-dotenv: Gerenciamento de variáveis de ambiente
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.globals import set_debug


def main():
    """
    Função principal que demonstra memória de conversação com LCEL.
    
    Utiliza RunnableWithMessageHistory para manter o contexto
    entre múltiplas perguntas, permitindo conversas multi-turno.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')

    # Inicialização do modelo (compartilhado entre as cadeias)
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    prompt_sugestao = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um assistente especializado em recomendar cidades turísticas com base nos interesses do usuário."),
            ("placeholder", "{historico}"),
            ("human", "{query}"),
        ]
    )

    cadeia = prompt_sugestao | modelo | StrOutputParser()

    memoria = {}
    sessao_id = "aula006_sessao1"

    def historico_por_sessao(sessao_id: str) -> InMemoryChatMessageHistory:
        if sessao_id not in memoria:
            memoria[sessao_id] = InMemoryChatMessageHistory()

        return memoria[sessao_id]  

    lista_pergunta = [
        "Quero visitar cidades com muitas praias. Quais você recomenda?",
        "Qual a melhor epoca do ano para visitar essas cidades?",
    ]

    cadeia_com_memoria = RunnableWithMessageHistory(
        runnable=cadeia,
        get_session_history=historico_por_sessao,
        input_messages_key="query",
        history_messages_key="historico",
    )

    for pergunta in lista_pergunta:
        resposta = cadeia_com_memoria.invoke(
            {
                "query": pergunta
            },
            config={"session_id": sessao_id}
        )

        print("Usuario: ", pergunta)
        print("Assistente: ", resposta, "\n")

if __name__ == "__main__":
    main()