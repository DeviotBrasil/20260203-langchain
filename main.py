import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def main():
    """
    Função principal que demonstra o uso da API da OpenAI.
    """
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém a chave da API
    api_key = os.getenv('OPENAI_API_KEY')
    
    numero_dias = 7
    numero_criancas = 2
    atividade = "música"

    prompt = (f"Crie um plano de atividades para {numero_dias} dias para {numero_criancas} crianças, "
              f"focando em atividades relacionadas a {atividade}. "
              "Cada dia deve incluir uma atividade principal e uma breve descrição.")
    
    modelo = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=api_key,
        temperature=0.7,
        max_tokens=500
    )

    resposta = modelo.invoke(prompt)
    print("Plano de Atividades:")
    print(resposta)

if __name__ == "__main__":
    main()