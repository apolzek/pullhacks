# Elasticsearch

**Definição**:

- Motor de busca textual e fonética por relevância (PT-BR nativo)
- Construído em cima do Apache Lucene
- Busca por aproximação, ou seja, mesmo com caracteres errados ele consegue trazer resultados
- Plugins para fazer busca fonética. Ideal para nomes brasileiros (complexos: Rayanne)
- Apache Lucene: é uma biblioteca de software de mecanismo de pesquisa de código aberto, originalmente escrita em Java por Doug ~~Cutting~~. É suportado pela Apache Software Foundation e é lançado sob a Licença de Software Apache
- É um banco de dados NoSQL e orientado a Documento
- Distribuído (distribuído em vários nos). Big data, ou seja cada máquina faz sua busca em paralelo
- Escalável horizontalmente, ou seja, é possível adicionar mais nós(Máquinas)
- Open Source. O que é Open Source é sempre Open Source
- Ele possuí módulos pagos da Elastic(Empresa)
- Schema Free. Não é necessário mapear todos os tipos de dados, ele vai 'adivinhar'. Ou seja: é possível indexar sem mapear antes MAS é recomendado mapear
- Elasticsearch dispõem uma API REST
- Possui bibliotecas para várias linguagens oficiais consumirem a API (Javascript, Java, C#, Python)
- Pode-se usar o Kibana para exibir ou buscar os dados

# Arquitetura: Elastic Stack

![image_01_002.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9a8a6609-8a2d-4a80-ab12-0a8d8e4290c6/image_01_002.jpg)

![0*O6aGxGkIlazsHi-p.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dda48e81-0932-408c-826d-deda9a291050/0O6aGxGkIlazsHi-p.png)

# Configurações

- *elasticsearch.yml* e *jvm.options* são os principais arquivos de configuração
- *elasticsearch.yml*  configurações gerais do cluster de Elasticsearch
- *jvm.options* configurações de HEAP

# Componentes de um cluster

- **Nó**: é uma instância rodando Elasticsearch
- Deve haver apenas uma instância de Elasticsearch por servidor. OBS: Para desenvolvimento é possível colocar mais de uma instância em uma máquina, mas não é recomendado fazer isso em produção
- Recomendações para um Nó:
    - Metade da memória colocar para HEAP. Ex: Servidor com 16GM de memória, 8 para HEAP e 8 fica para SO
    - Não é recomendado passar de 32GB de HEAP, ou seja o Nó deve ter no máximo 64GB de memória
    - Configuração máxima e mínima de HEAP iguais. Xms == Xmx
    - Recomendado que seja Bare-metal e que o disco esteja na máquina. Pode ser VM mas é recomendado máquina física por questões de performance

- **Cluster**: um ou mais nós compartilhando o mesmo *[cluster.name](http://cluster.name).* Isso é configurado no arquivo *elasticsearch.yml*
- Dentro de um cluster o Nós podem possuir diferentes funções
    - Mater Node: responsável pelas configurações e alterações no cluster. [Analogia: semelhante a um Gerente de Projetos, ou seja faz a gestão]
    - Data Node: responsável pelas operações de dados. [Analogia: semelhante ao Técnico, mão na massa ]
    - Ingest Node: responsável pelo pré-processamento dos dados. Ingest pipelines, _reindex
    
- Recomendação ambientes **não críticos**
    - Desenvolvimento: 1 Node
    - elasticsearch.yml deve ter as três roles habilitadas

```jsx
cluster.name: devcluster
nome.master: true
node.data: true
node.ingest: true
```

- Recomendação ambientes  **críticos** (de produção)
    - 12 Nós sendo 3 Masters dedicados
        
        ```jsx
        cluster.name: production
        nome.master: true
        node.data: false
        node.ingest: false
        ```
        
    - 9 Data Nodes
        
        ```jsx
        cluster.name: production
        nome.master: false
        node.data: true
        node.ingest: true
        ```
        
- **Índice e Shard**:
    - Um índica aponta para um ou mais **Shards**
    - Índice não existe fisicamente, ele apenas aponta
    - o Shard é uma instância do Lucene. O Apache Lucene é gerenciado pelo Elasticsearch
    - Um índice pode ter mais de um Shard
    - Cada Shard é um motor de busca em si mesmo. Ex: Vendar possui 2 Shards com vários documentos. Quando se pergunta ao índice algum documento(query), o índice pergunta individualmente para cada Shard e ele une a informação no final
    - Os clients não acessar os Shards diretamente e sim os Índices
    - O dado está no Shard e não no Índice, ou seja, o índice é lógico
    - Shard0 e Replica0 nunca vão estar no mesmo Nó, para ter um backup dos dados
    - **Recomendação**: cada Shard deve possuir entre 40GB e 60GB de dados. Ou seja, o índice poderá armazenar até 120GB de dados. Caso aumente poderá ter perda de performance
    - Pode existir mais de um Shard primário em um mesmo Nó. Mas não pode ter o Shard e sua réplica no mesmo Nó
    - A indexação é sempre feito no Shard primeiro e depois é criado a Réplica
    - O Elasticsearch pode controlar o ID dos documentos adicionados
    - Se um nó cair o outro assume automaticamente
    
    ![Screenshot_20211018_201236.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e336ca0-79ea-4d1e-b122-4b56e5a9c6c4/Screenshot_20211018_201236.png)
    
- **Master Nodes**:
    - O Master Node é eleito através de uma votação entre os Master Nodes
    - Os outros Nodes com roles do tipo Master são os **Elegíveis**
    - Sempre irá ter apenas UM Master, os outros estarão no modo stand-by
    - O Master eleito escreve um 'relatório' com tudo que está acontecendo no cluster, inclusive mapeando todos os Documentos e Shards. O 'relatório' se chama **Cluster State**
    - O Cluster State é replicado em todos os outros Nós
- **Split-brain (troubleshooting)**:
    - Quando existe mais um Master eleito
    - Ele cria duas visões diferentes e tem mais de um Nó escrevendo um Cluster State
    - Ex: 3 Nodes: Node 1, Node 2 e Node  3. Pode acontecer do Node 1 perder a comunicação com o Node 2 e Node 3. Dai no caso o Node 1 pode se eleger e o Node 2 ou Node 3 decidirem eleger um novo Master também
    - Resolução: parâmetro ***minimum_master_nodes*** deve ser = Metade de Master Nodes + 1, ou seja. Nesse caso como tem três nodes, seria 2. 3/2 = 1,5 + 1 = 2,5 .. ignorando a virgual  seria 2. Ou seja: É necessário no mínimo 2 nós para ter uma 'Eleição'
    - A resolução acima funciona pois o Node 1 não vai ter quorum suficiente para se eleger
    - Da versão 7 para frente o Elasticsearch gerencia tudo isso. Então o problema de Split-brain pode acontecer da versão 7 para baixo
    
     **
    
- **Cluster Yellow**:
    - Pode acontecer por vário motivos, entre eles quando o Índice cria o Shard e a Réplica no mesmo nó. Ou seja se você tiver apenas 1 Node isso vai acontecer
    
- **Considerações Finais**
    - Não tentar fazer relacionamentos no Elasticsearch. O índice pode trazer vários dados que em um banco de Dados Relacional poderia estar dividido entre várias tabelas
    - Elasticsearch pode ser interessante para salvar Logs
    - Desnormalize os dados e crie Índices Fato
    - Ideal nosso Nó trabalhar com SSD(mais performance)
    
- **Outras imagens**
    
    ![1*0gUMUCd81Oxu-npn-NZcTw.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee1d7bdf-f971-4000-9d5e-b23c5a517683/10gUMUCd81Oxu-npn-NZcTw.png)
    

# Referências

[Elasticsearch - Definições, Arquitetura e Boas Práticas](https://www.youtube.com/watch?v=-fAq1B81nRI)

