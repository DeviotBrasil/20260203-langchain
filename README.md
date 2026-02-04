# Curso de LangChain - Aulas Práticas

Repositório com exemplos práticos de uso do LangChain com a API da OpenAI, cobrindo desde conceitos básicos até cadeias complexas.

## 📋 Descrição

Este projeto contém uma série de aulas práticas que demonstram o uso progressivo do framework LangChain para construir aplicações com modelos de linguagem (LLMs). Cada aula introduz novos conceitos e técnicas.

## 📚 Conteúdo das Aulas

### [aula001.py](aula001.py) - Introdução ao LangChain com OpenAI
- Configuração básica do ambiente
- Uso do `ChatOpenAI` para chamadas diretas ao modelo
- Criação de prompts simples com f-strings
- Invocação do modelo e obtenção de respostas

### [aula002.py](aula002.py) - Usando ChatPromptTemplate
- `ChatPromptTemplate` para prompts estruturados
- Separação de mensagens de sistema e usuário
- Variáveis de template com placeholders `{}`
- Formatação de prompts com `.format()`

### [aula003.py](aula003.py) - Introdução às Cadeias com LCEL
- `PromptTemplate` para templates simples
- Operador pipe (`|`) para encadeamento - LCEL
- `StrOutputParser` para extrair texto puro
- Sintaxe declarativa do LangChain Expression Language

### [aula004.py](aula004.py) - Saída Estruturada com JSON
- `JsonOutputParser` para respostas em JSON
- Validação com modelos Pydantic (`BaseModel`, `Field`)
- `partial_variables` para instruções de formato
- Modo debug com `set_debug(True)`

### [aula005.py](aula005.py) - Encadeamento de Múltiplas Cadeias
- Múltiplos modelos Pydantic para diferentes respostas
- Encadeamento sequencial de cadeias
- Passagem de dados entre cadeias
- Composição de pipelines complexos

### [aula006.py](aula006.py) - Revisão: Cadeias Simples
- Consolidação dos conceitos de cadeias com LCEL
- Exemplo prático de recomendação de cidades
- Revisão do fluxo `prompt -> modelo -> parser`

## 🚀 Tecnologias Utilizadas

- **LangChain**: Framework para desenvolvimento com LLMs
- **LangChain OpenAI**: Integração com modelos da OpenAI
- **LangGraph**: Orquestração de agentes (para aulas futuras)
- **Pydantic**: Validação de dados e schemas
- **FAISS**: Busca vetorial (para aulas futuras)
- **python-dotenv**: Gerenciamento de variáveis de ambiente

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

```env
OPENAI_API_KEY=sua-chave-api-aqui
```

⚠️ **Importante**: Nunca compartilhe ou commite seu arquivo `.env` com a chave da API!

## 🎯 Como Usar

Execute qualquer script de aula:

```bash
# Aula 1 - Básico
python aula001.py

# Aula 2 - ChatPromptTemplate
python aula002.py

# Aula 3 - Cadeias LCEL
python aula003.py

# Aula 4 - Saída JSON
python aula004.py

# Aula 5 - Múltiplas Cadeias
python aula005.py

# Aula 6 - Revisão
python aula006.py
```

## 📂 Estrutura do Projeto

```
20260203-langchain/
├── aula001.py           # Introdução ao LangChain
├── aula002.py           # ChatPromptTemplate
├── aula003.py           # Cadeias com LCEL
├── aula004.py           # Saída estruturada JSON
├── aula005.py           # Múltiplas cadeias
├── aula006.py           # Revisão de cadeias
├── requirements.txt     # Dependências do projeto
├── README.md            # Este arquivo
└── .env                 # Variáveis de ambiente (não versionado)
```

## 📖 Conceitos Principais

| Conceito | Descrição |
|----------|------------|
| **LCEL** | LangChain Expression Language - sintaxe com operador `\|` |
| **Chain** | Sequência de componentes conectados |
| **PromptTemplate** | Template para formatação de prompts |
| **OutputParser** | Processa e estrutura a saída do modelo |
| **Pydantic** | Validação de schemas para saídas JSON |

## 🔧 Parâmetros do Modelo

Em todos os scripts, você pode ajustar os parâmetros do modelo:

```python
modelo = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # Modelo a ser usado
    temperature=0.7,             # Criatividade (0.0 - 2.0)
    max_tokens=500               # Tamanho máximo da resposta
)
```

## 🔗 Recursos

- [Documentação do LangChain](https://python.langchain.com/docs/)
- [LCEL - LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/)
- [Documentação Oficial da OpenAI](https://platform.openai.com/docs)
- [Pydantic](https://docs.pydantic.dev/)

## 📄 Licença

Este projeto é livre para uso educacional e de demonstração.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
