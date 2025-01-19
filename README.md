# Documentação: Algoritmo Genético para Otimização de Centros de Distribuição

## Visão Geral
Este documento explica a implementação de um algoritmo genético projetado para otimizar a localização de centros de distribuição com o objetivo de minimizar a distância total entre as cidades e esses centros. O código é executado com uma interface gráfica utilizando a biblioteca Pygame para visualização e Matplotlib para plotagem da evolução do algoritmo.

# Environments
#.env
#.venv
#env/
#venv/
#ENV/
#env.bak/
#venv.bak/

## Bibliotecas Utilizadas
- **Pygame**: Usada para criar a interface gráfica e gerenciar eventos de usuário, como fechar a janela ou interagir com a simulação.
- **Random**: Utilizada para a geração de números aleatórios, essencial para operações de mutação e crossover no algoritmo genético.
- **Math**: Fornece funções matemáticas necessárias, como a função de raiz quadrada usada no cálculo de distâncias euclidianas.
- **Matplotlib**: Usada para criar gráficos que mostram a evolução da função de fitness ao longo das gerações.
- **Collections (defaultdict)**: Facilita a manipulação de dicionários ao proporcionar valores padrão para chaves que ainda não existem.

## Configuração Inicial
As variáveis configuradas inicialmente incluem dimensões da tela para a simulação, número de cidades e centros de distribuição, o tamanho da população do algoritmo genético, o número de gerações a serem simuladas e a taxa de mutação.

## Funcionalidades do Código
### Geração de Indivíduos
Cada indivíduo na população representa um possível conjunto de localizações para os centros de distribuição. A inicialização e as mutações são feitas com base em coordenadas aleatórias dentro dos limites definidos pela tela.

### Cálculo de Fitness
O fitness de cada indivíduo é calculado como a negação da soma das distâncias das cidades aos seus centros de distribuição mais próximos. A abordagem visa minimizar a distância total, portanto, melhores soluções têm fitness mais alto (menos negativo).

### Seleção e Reprodução
Utiliza-se um método de seleção baseado no fitness para escolher quais indivíduos passarão seus genes para a próxima geração. Crossovers e mutações são aplicados para gerar diversidade genética.

### Visualização
As posições das cidades e dos centros são representadas na tela com diferentes cores. Linhas são desenhadas conectando cada cidade ao seu centro de distribuição designado.

### Evolução do Fitness
A evolução do fitness é plotada em um gráfico ao lado da visualização principal, mostrando como o melhor fitness evolui com cada geração, oferecendo insights sobre a performance do algoritmo.

## Encerramento do Programa
O loop principal do algoritmo continua até que o usuário feche a janela do Pygame ou interrompa o processo através de uma entrada de teclado específica.

Este documento fornece uma visão geral clara da estrutura e funcionamento do algoritmo genético para otimização de centros de distribuição, permitindo a qualquer usuário compreender e manipular o código com propriedade.
