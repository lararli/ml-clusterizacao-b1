# Clusterização de Dados Socioeconômicos de Países

Este projeto realiza análise de clusterização não supervisionada em dados socioeconômicos e de saúde de 167 países, utilizando dados do Kaggle. O objetivo é identificar padrões e agrupar nações com características semelhantes.

## Descrição do Projeto

O trabalho analisa indicadores como:
- Mortalidade infantil (child_mort)
- Expectativa de vida (life_expec)
- Renda per capita (income)
- PIB per capita (gdpp)
- Investimento em saúde (health)
- Taxa de fertilidade (total_fer)
- Inflação (inflation)
- Exportações e importações (exports, imports)

## Estrutura do Repositório

```
clusterizacao_b1/
├── main.ipynb           # Notebook principal com toda a análise
├── load.py              # Script para carregar dados do Kaggle
├── requirements.txt     # Dependências do projeto
└── reports/             # Diretório para relatórios gerados
```

## Algoritmos Implementados

O projeto compara quatro algoritmos de clusterização:

1. **K-Means**: Algoritmo baseado em centróides que agrupa países por distâncias médias
2. **Clusterização Hierárquica (Ward)**: Agrupa países por similaridade progressiva, visualizado através de dendrograma
3. **K-Medoids (implementação customizada)**: Usa medoides (pontos reais) ao invés de centróides, mais robusto a outliers
4. **DBSCAN**: Algoritmo baseado em densidade que identifica automaticamente ruído e outliers

## Principais Resultados

### Perfis de Clusters Identificados

- **Países Desenvolvidos**: Alto PIB per capita, baixa mortalidade infantil, alta expectativa de vida (ex: Austrália, Suíça, Noruega)
- **Países em Desenvolvimento**: Indicadores intermediários, condições moderadas (ex: Albânia, Argélia)
- **Países em Situação Vulnerável**: Alta mortalidade infantil, baixa expectativa de vida, baixa renda (ex: Afeganistão, Angola, Haiti)

### Comparação de Algoritmos

O projeto analisa as diferenças entre os algoritmos:
- K-Means forma separações mais nítidas baseadas em perfis extremos
- Hierárquico revela estruturas de similaridade gradual
- K-Medoids oferece maior robustez a outliers usando pontos reais
- DBSCAN identifica outliers automaticamente sem forçá-los em clusters

## Instalação e Uso

### Pré-requisitos

- Python 3.x
- pip

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd clusterizacao_b1
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando o Projeto

1. Abra o Jupyter Notebook:
```bash
jupyter notebook main.ipynb
```

2. Execute as células sequencialmente para reproduzir a análise completa

## Dependências Principais

- pandas: Manipulação de dados
- numpy: Operações numéricas
- scikit-learn: Algoritmos de clusterização
- matplotlib & seaborn: Visualizações
- scipy: Clusterização hierárquica
- kagglehub: Download de dados do Kaggle

## Fonte dos Dados

Os dados são obtidos do Kaggle:
- Dataset: `rohan0301/unsupervised-learning-on-country-data`
- Arquivo: `Country-data.csv`
- Contém 167 países e 9 variáveis socioeconômicas

## Estrutura do Notebook

1. **Parte 1**: Introdução e contexto
2. **Parte 2**: Exploração e análise de dados
   - Análise de correlações
   - Visualizações (pairplot, heatmap, boxplots)
   - Padronização com StandardScaler
3. **Parte 3**: Clusterização
   - K-Means (k=3)
   - Clusterização Hierárquica com dendrograma
   - Comparação entre métodos
4. **Parte 4**: Algoritmos avançados
   - Implementação customizada de K-Medoids
   - DBSCAN para identificação de outliers
   - Análise de robustez a outliers

## Visualizações

O projeto inclui:
- Boxplots de variáveis antes e depois da padronização
- Pairplot de relações entre variáveis
- Matriz de correlação com heatmap
- Dendrograma da clusterização hierárquica
- Tabelas comparativas de médias dos clusters

## Autoria

Projeto desenvolvido como trabalho acadêmico de pós-graduação.
