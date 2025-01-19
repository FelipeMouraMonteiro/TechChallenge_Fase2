# Algoritmo Genético - Centros de Distribuição

Este projeto implementa um algoritmo genético para otimizar a distribuição de centros em uma configuração simulada de cidades. Ele utiliza Pygame para renderização gráfica e Matplotlib para visualizar a evolução do fitness ao longo das gerações.

## Pré-requisitos

Antes de começar, você precisará instalar Python em seu sistema. Este projeto foi desenvolvido usando Python 3.8 ou superior. Você também precisará de algumas bibliotecas Python, incluindo Pygame para a interface gráfica e Matplotlib para a visualização de dados.

### Instalação do Python

1. **Windows:** Você pode baixar o instalador do Python em [python.org](https://www.python.org/downloads/).
2. **macOS:** Recomenda-se usar o Homebrew para instalar Python com `brew install python`.
3. **Linux:** Python geralmente já está instalado, ou você pode instalá-lo via gerenciador de pacotes com `sudo apt install python3`.

### Configuração do Ambiente Virtual

É recomendável usar um ambiente virtual para gerenciar as dependências. Para criar e ativar um ambiente virtual, use:

```bash
python -m venv venv
source venv/bin/activate  # No Unix ou macOS
venv\Scripts\activate  # No Windows
```

### Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências necessárias com:

 ```bash
pip install pygame matplotlib 
```

A biblioteca `matplotlib.backends.backend_agg` e o módulo `pylab` são partes do Matplotlib e não requerem instalação separada. O módulo `random` é padrão do Python e já está disponível com a instalação do Python.

## Executando o Projeto

Para executar o projeto, clone este repositório, navegue até o diretório clonado, e execute o script principal:
 
<URL-do-repositorio>
<nome-do-repositorio>
python Centro_Distribuicao.py 

`Centro_Distribuicao.py` deve ser o nome do arquivo que contém o código principal.

## Estrutura do Código

- **Centro_Distribuicao.py:** Contém a lógica principal do algoritmo genético e a interface gráfica com Pygame.
- **servicos.py:** Deve conter as definições da classe `Servicos`, responsável por operações como geração de cidades, cálculo de fitness, crossover e mutação.

## Contribuições

Contribuições são bem-vindas! Para contribuir, por favor faça um fork do repositório, crie uma branch para suas modificações, e submeta um pull request.
