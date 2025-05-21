Gerenciamento de Rede com Árvores Binárias
Este projeto implementa uma árvore binária de busca em Python para gerenciar uma rede de computadores, organizando endereços IP de forma hierárquica. Ele demonstra conceitos de teoria dos grafos (árvores como grafos direcionados sem ciclos) e recursividade, com saídas gráficas (ASCII) para visualizar a estrutura da árvore. O código é simples, didático e ideal para ensino e apresentações sobre estruturas de dados.
Contexto

Cenário: Uma empresa organiza seus computadores por endereços IP (representados como números inteiros para simplificação, ex.: 100).
Estrutura: A árvore binária de busca organiza IPs, com valores menores à esquerda e maiores à direita.
Funcionalidades:
Inserir um computador (IP).
Buscar um computador por IP.
Listar todos os IPs em ordem crescente.
Exibir a árvore graficamente (usando ASCII art) após cada operação.



Requisitos

Python 3.x
Sem dependências externas (o código usa apenas funcionalidades nativas do Python).

Como Executar

Clone o repositório:git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>


Execute o script Python:python arvore_binaria_rede.py


A saída mostrará:
Inserção de IPs (100, 50, 150, 25, 75) com a árvore exibida após cada inserção.
Busca por IPs (ex.: 75 e 99) com a árvore e resultados.
Listagem de todos os IPs em ordem, seguida da árvore completa.



Estrutura do Código

Computador (classe): Representa um nó da árvore, com ip, esquerdo e direito.
exibir_arvore_grafica: Função recursiva que imprime a árvore em formato ASCII.
inserir_computador: Insere um IP recursivamente e exibe a árvore.
buscar_computador: Busca um IP recursivamente e exibe a árvore.
listar_computadores: Lista IPs em ordem (esquerda, raiz, direita) e exibe a árvore.
main: Testa o código com IPs de exemplo (100, 50, 150, 25, 75).

Exemplo de Saída
Inserindo IP 100...
Árvore após inserir IP 100:
IP: 100

Inserindo IP 50...
Árvore após inserir IP 50:
IP: 100
    ├── IP: 50

[...]

Buscando IPs...
Computador encontrado: IP 75
Árvore com IP encontrado:
IP: 100
    ├── IP: 50
    │    ├── IP: 25
    │    └── IP: 75
    └── IP: 150

Listando todos os computadores...
Computador com IP: 25
Computador com IP: 50
Computador com IP: 75
Computador com IP: 100
Computador com IP: 150
Árvore completa:
IP: 100
    ├── IP: 50
    │    ├── IP: 25
    │    └── IP: 75
    └── IP: 150

Por que Árvores Binárias?

Teoria dos Grafos: A árvore é um grafo direcionado sem ciclos, com vértices (computadores) e arestas (conexões entre nós).
Recursividade: Todas as funções (inserção, busca, listagem, exibição gráfica) usam recursividade para processar subárvores.
Aplicação: Organiza IPs de forma eficiente (busca em O(log n) em média), útil em gerenciamento de redes.
Didático: Saídas ASCII mostram visualmente a estrutura da árvore, facilitando o ensino.

Para Apresentações

Slides: Inclua capturas da saída ASCII para mostrar a evolução da árvore.
Demonstração: Execute o código ao vivo para mostrar inserções e buscas.
Visual: Desenhe a árvore final (IP 100, 50, 150, 25, 75) em um slide para explicar a hierarquia.

Contribuições
Sinta-se à vontade para sugerir melhorias, como:

Destacar nós encontrados na saída ASCII.
Adicionar mais funcionalidades (ex.: remover IPs).
Adaptar para outras linguagens.

Licença
MIT License – sinta-se livre para usar, modificar e compartilhar o código.
