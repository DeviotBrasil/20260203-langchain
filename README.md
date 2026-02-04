# Gerador de Plano de Atividades para Crianças

Aplicação Python que utiliza LangChain e a API da OpenAI para gerar planos de atividades personalizados para crianças.

## 📋 Descrição

Este projeto utiliza o LangChain com o modelo GPT-3.5-turbo da OpenAI para criar planos de atividades educativas e divertidas para crianças. O usuário pode definir o número de dias, quantidade de crianças e o tema das atividades (ex: música, arte, esportes), e o sistema gera automaticamente um plano completo com atividades principais e descrições para cada dia.

## 🚀 Funcionalidades

- Geração automática de planos de atividades para crianças
- Personalização por número de dias e quantidade de crianças
- Foco em temas específicos (música, arte, esportes, etc.)
- Integração com LangChain e API da OpenAI
- Uso do modelo GPT-3.5-turbo
- Gerenciamento seguro de chaves de API via variáveis de ambiente

## 📦 Pré-requisitos

- Python 3.8 ou superior
- Chave de API da OpenAI ([obtenha aqui](https://platform.openai.com/api-keys))

## ⚙️ Configuração Inicial

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd 20260203-langchain
```

### 2. Criar ambiente virtual

#### Windows (CMD)

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS (Bash)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da API:

```env
OPENAI_API_KEY=sua-chave-api-aqui
```

⚠️ **Importante**: Nunca compartilhe ou commite seu arquivo `.env` com a chave da API!

## 🎯 Como Usar

Execute o script principal:

```bash
python main.py
```

O script irá:
1. Carregar a chave da API do arquivo `.env`
2. Inicializar o modelo GPT-3.5-turbo via LangChain
3. Gerar um plano de atividades personalizado com base nos parâmetros definidos
4. Exibir o plano completo no terminal

### Personalização

Edite o arquivo [main.py](main.py) para ajustar os parâmetros:

```python
numero_dias = 7        # Quantidade de dias do plano
numero_criancas = 2    # Número de crianças
atividade = "música"   # Tema das atividades (música, arte, esportes, etc.)
```

## 📚 Estrutura do Projeto

```
20260203-langchain/
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
├── .env.example        # Exemplo de configuração
├── .env                # Suas configurações (não versionar!)
└── README.md           # Esta documentação
```

## 📦 Dependências

- **langchain** - Framework para desenvolvimento com LLMs
- **langchain-openai** - Integração do LangChain com OpenAI
- **langgraph** - Extensão do LangChain para workflows
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **faiss-cpu** - Biblioteca para busca por similaridade
- **pypdf** - Manipulação de arquivos PDF

## 🔧 Comandos Úteis

### Atualizar dependências

```bash
python -m pip install -r requirements.txt --upgrade
```

### Listar dependências instaladas

```bash
pip freeze
```

## 📖 Exemplos de Saída

Ao executar o script com os parâmetros padrão, você receberá um plano de atividades como:

```
Plano de Atividades:
Dia 1: Explorando instrumentos musicais
- Atividade: Conhecer diferentes instrumentos musicais através de vídeos e sons
- Descrição: As crianças aprenderão sobre violão, piano, bateria...

Dia 2: Cantando juntos
- Atividade: Aprender uma música infantil simples
...
```

## 🔧 Ajustes no Modelo

### Ajustar parâmetros do LLM

No arquivo [main.py](main.py), você pode modificar:

```python
modelo = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # Modelo a ser usado
    temperature=0.7,             # Criatividade (0.0 - 2.0)
    max_tokens=500               # Tamanho máximo da resposta
)
```

## 🔗 Recursos

- [Documentação do LangChain](https://python.langchain.com/docs/)
- [Documentação Oficial da OpenAI](https://platform.openai.com/docs)
- [LangChain OpenAI Integration](https://python.langchain.com/docs/integrations/chat/openai)
- [Preços da API](https://openai.com/pricing)

## 📄 Licença

Este projeto é livre para uso educacional e de demonstração.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
