# Elasticsearch

**Resumo sobre Elasticsearch**:

- Motor de busca textual e fonética por relevância (PT-BR nativo)
- Construído em cima do **Apache Lucene**
- Busca por aproximação, ou seja, mesmo com caracteres errados ele consegue trazer resultados
- Plugins para fazer busca fonética. Ideal para nomes brasileiros (complexos: Rayanne)
- Apache Lucene: é uma biblioteca de software de mecanismo de pesquisa de código aberto, originalmente escrita em Java por Doug Cutting. É suportado pela Apache Software Foundation e é lançado sob a Licença de Software Apache
- É um banco de dados NoSQL e Orientado a Documento
- Distribuído (distribuído em vários nos). Big data, ou seja cada máquina faz sua busca em paralelo
- Escalável horizontalmente, ou seja, é possível adicionar mais nós(Máquinas)
- Open Source. O que é Open Source é sempre Open Source
- Ele possuí módulos pagos da Elastic(Empresa)
- Schema Free. Não é necessário mapear todos os tipos de dados, ele vai 'adivinhar'. Ou seja: é possível indexar sem mapear antes MAS é recomendado mapear
- Elasticsearch dispõem uma API REST
- Possui bibliotecas para várias linguagens oficiais consumirem a API (Javascript, Java, C#, Python)
- Pode-se usar o Kibana para exibir ou buscar os dados

## Arquitetura: Elastic Stack

![image1](https://github.com/apolzek/pullhacks/blob/main/technology-wiki/databases/elasticsearch/.images/1.jpg)

## Configurações

Os principais arquivos de configuração são: *elasticsearch.yml* e *jvm.options* 

- *elasticsearch.yml*  configurações gerais do cluster de Elasticsearch
- *jvm.options* configurações de HEAP

## Componentes Elasticsearch

### Nó

- **Nó**: é uma instância rodando Elasticsearch
- Deve haver apenas uma instância de Elasticsearch por servidor. **OBS**: Para desenvolvimento é possível colocar mais de uma instância em uma máquina, mas não é recomendado fazer isso em produção
- Recomendações para um Nó:
    - Metade da memória colocar para HEAP. Ex: Servidor com 16GM de memória, 8 para HEAP e 8 fica para SO
    - Não é recomendado passar de 32GB de HEAP, ou seja o Nó deve ter no máximo 64GB de memória
    - Configuração máxima e mínima de HEAP iguais. Xms == Xmx
    - Recomendado que seja Bare-metal e que o disco esteja na máquina. Pode ser VM mas é recomendado máquina física por questões de performance

### Cluster

- **Cluster**: um ou mais nós compartilhando o mesmo *cluster.name.* Isso é configurado no arquivo *elasticsearch.yml*
- Dentro de um cluster o Nós podem possuir diferentes funções
    - **Mater Node**: responsável pelas configurações e alterações no cluster. [Analogia: semelhante a um Gerente de Projetos, ou seja faz a gestão]
    - **Data Node**: responsável pelas operações de dados. [Analogia: semelhante ao Técnico, mão na massa ]
    - **Ingest Node**: responsável pelo pré-processamento dos dados. Ingest pipelines, _reindex
    
- Recomendação ambientes **não críticos**
    - Desenvolvimento: 1 Node
    - elasticsearch.yml deve ter as três roles habilitadas

        ```
        cluster.name: devcluster
        nome.master: true
        node.data: true
        node.ingest: true
        ```

- Recomendação ambientes  **críticos** (produção)
    - 12 Nós sendo 3 Masters dedicados

        ```
        cluster.name: production
        nome.master: true
        node.data: false
        node.ingest: false
        ```
        ```
        cluster.name: production
        nome.master: false
        node.data: true
        node.ingest: true
        ```

![image2](https://github.com/apolzek/pullhacks/blob/main/technology-wiki/databases/elasticsearch/.images/6.png)

## Considerações

- Um índice aponta para um ou mais **Shards**
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
    
![image3](https://github.com/apolzek/pullhacks/blob/main/technology-wiki/databases/elasticsearch/.images/5.png)

### Master Nodes

- O Master Node é eleito através de uma votação entre os Master Nodes
- Os outros Nodes com roles do tipo Master são os **Elegíveis**
- Sempre irá ter apenas UM Master, os outros estarão no modo stand-by
- O Master eleito escreve um 'relatório' com tudo que está acontecendo no cluster, inclusive mapeando todos os Documentos e Shards. O 'relatório' se chama **Cluster State**
- O Cluster State é replicado em todos os outros Nós

### Split-brain (troubleshooting)

- Quando existe mais um Master eleito
- Ele cria duas visões diferentes e tem mais de um Nó escrevendo um Cluster State
- Ex: 3 Nodes: Node 1, Node 2 e Node  3. Pode acontecer do Node 1 perder a comunicação com o Node 2 e Node 3. Dai no caso o Node 1 pode se eleger e o Node 2 ou Node 3 decidirem eleger um novo Master também
- Resolução: parâmetro ***minimum_master_nodes*** deve ser = Metade de Master Nodes + 1, ou seja. Nesse caso como tem três nodes, seria 2. 3/2 = 1,5 + 1 = 2,5 .. ignorando a virgual  seria 2. Ou seja: É necessário no mínimo 2 nós para ter uma 'Eleição'
- A resolução acima funciona pois o Node 1 não vai ter quorum suficiente para se eleger
- Da versão 7 para frente o Elasticsearch gerencia tudo isso. Então o problema de Split-brain pode acontecer da versão 7 para baixo

### Cluster Yellow

- Pode acontecer por vário motivos, entre eles quando o Índice cria o Shard e a Réplica no mesmo nó. Ou seja se você tiver apenas 1 Node isso vai acontecer
    
## Considerações Finais

- Não tentar fazer relacionamentos no Elasticsearch. O índice pode trazer vários dados que em um banco de Dados Relacional poderia estar dividido entre várias tabelas
- Elasticsearch pode ser interessante para salvar Logs
- Desnormalize os dados e crie Índices Fato
- Ideal nosso Nó trabalhar com SSD(mais performance)


![image4](https://github.com/apolzek/pullhacks/blob/main/technology-wiki/databases/elasticsearch/.images/4.png)


## Hands-on

![https://media.giphy.com/media/4KEChFKWvCYOQBbngD/giphy.gif](https://media.giphy.com/media/4KEChFKWvCYOQBbngD/giphy.gif)

Subir Elasticsearch usando **Docker**

```bash
# Docker
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.1
```

Subir Elasticsearch usando **docker-compose**

```
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.3.1
    container_name: elasticsearch
    environment:
      - node.name=ws-es-node
      - discovery.type=single-node
      - cluster.name=ws-es-data-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms1024m -Xmx1024m"
      # - xpack.security.enabled='false'
      # - xpack.monitoring.enabled='false'
      # - xpack.watcher.enabled='false'
      # - xpack.ml.enabled='false'
      # - http.cors.enabled='true'
      # - http.cors.allow-origin="*"
      # - http.cors.allow-methods=OPTIONS, HEAD, GET, POST, PUT, DELETE
      # - http.cors.allow-headers=X-Requested-With,X-Auth-Token,Content-Type, Content-Length
      - logger.level=debug
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - vibhuviesdata:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
      - 9300:9300
    networks:
      - esnet

  elasticsearch_exporter:
      image: quay.io/prometheuscommunity/elasticsearch-exporter:latest
      command:
      - '--es.uri=http://elasticsearch:9200'
      restart: always
      ports:
      - "9114:9114"

  kibana:
    image: docker.elastic.co/kibana/kibana:7.3.1
    container_name: kibana
    environment:
      SERVER_NAME: 127.0.0.1
      ELASTICSEARCH_HOSTS: http://elasticsearch:9200
      # XPACK_GRAPH_ENABLED: false
      # XPACK_ML_ENABLED: false
      # XPACK_REPORTING_ENABLED: false
      # XPACK_SECURITY_ENABLED: false
      # XPACK_WATCHER_ENABLED: false
    ports:
      - "5601:5601"
    networks:
      - esnet
    depends_on:
      - elasticsearch
    restart: "unless-stopped"
    
volumes:
  vibhuviesdata:
    driver: local

networks:
  esnet:
```

Chamadas a API REST do Elasticsearch

```bash
# Health cluster
curl -X GET 'localhost:9200/_cluster/health?pretty'

# Resumo do cluster(versão, nome ..)
curl http://localhost:9200/

# State do cluster(output grande)
curl -XGET "http://localhost:9200/_cluster/state?pretty"

# Listar nodes e recursos dos nodes
curl -X GET "localhost:9200/_cat/nodes?v=true&pretty"

# Listar indices
curl 'localhost:9200/_cat/indices?v'

# Create an Index in Elasticsearch with custom shards and replicas
curl -XPUT -H "Content-Type: application/json" http://localhost:9200/indice?pretty -d '{
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 1
    }
  }
}'

# Deletar indices
curl -v -XDELETE "localhost:9200/indice?pretty"

# Buscando indice
curl -XGET http://localhost:9200/indice?pretty

# Buscando indice que nao existe
curl -XGET http://localhost:9200/force404?pretty

# Create index in Elasticsearch with mapping
curl -v -XPUT "localhost:9200/indicemap?include_type_name=false" -H 'Content-Type: application/json' -d '
{
  "settings" : {
    "number_of_shards" : 3,
    "number_of_replicas" : 1
  },
  "mappings": {
    "properties": {
      "field_1": { "type" : "text" },
        "field_2": { "type" : "integer" },
        "field_3": { "type" : "boolean" },
      "created": {
        "type" : "date",
        "format" : "epoch_second"
      }
    }
  }
}'


# Criar um indice com documento

# make a PUT request to index, or update, document #42
curl -XPUT "localhost:9200/indicedoc/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "field_1": "Hello 1111111111",
  "field_2": 7771,
  "field_3": false,
  "created": "1556191252"
}'

curl -XPUT "localhost:9200/indicedoc/_doc/2?pretty" -H 'Content-Type: application/json' -d'
{
  "field_1": "Hello 2222222222",
  "field_2": 666,
  "field_3": true,
  "created": "1256191252"
}'

# Index an Elasticsearch document with an autogenerated, dynamically-created ID
curl -XPOST "localhost:9200/indiceauto/_doc?pretty" -H 'Content-Type: application/json' -d'
{
  "field_1": "I wonder what my ID will be?!?!?!",
  "field_2": 5678,
  "field_3": true,
  "created": "1556193846"
}'

curl -XPOST "localhost:9200/indiceauto/_doc?pretty" -H 'Content-Type: application/json' -d'
{
  "field_1": "Ho hacking ?!?!?!",
  "field_2": 6666,
  "field_3": true,
  "created": "1456193846"
}'

# Using the _bulk API to index documents to Elasticsearch:  You can use the _bulk option at the end of the header and include a JSON object with the "_id" declared for each document in a nested "index" field:2
curl -v -XPOST "http://localhost:9200/some_index/_doc/_bulk?pretty" -H 'Content-Type: application/json' -d '
  { "index": { "_id" : 1234 }}
  { "field_1": "SOME TEXT, YO!!!", "field_2": 34, "field_3": true, "created" : "1556195768" }
  { "index": { "_id" : 4321 }}
  { "field_1": "MORE TEXT, YO!!!", "field_2": 575, "field_3": false, "created" : "1556195768" }
  { "index": { "_id" : 3456 }}
  { "field_1": "LAST TEXT, YO!!!", "field_2": 123890, "field_3": true, "created" : "1556195773" }
'
```

O formato geral da consulta `_stats` é:

```bash
/_stats
/_stats/{metric}
/_stats/{metric}/{indexMetric}
/{index}/_stats
/{index}/_stats/{metric}


# Where the metrics are:

indices, docs, store, indexing, search, get, merge,
refresh, flush, warmer, filter_cache, id_cache,
percolate, segments, fielddata, completion
```

Rest UI

```
# Criar um indice
PUT example_index
{
    "settings": {
		"index": {
			"number_of_shards": 3,
			"number_of_replicas": 2
		}
	}
}


# Criar documento no index
PUT example_index/_doc/1
{
"model": "Porshe",
"year": 1972,
"engine": "2.0-liter four-cylinder Macan",
"horsepower": "252hp",
"genres": ["Sporty", "Classic"]
}
```

## Subir Elasticsearch via Helm

```bash
# k3d cluster create elasticdemo --agents 3
helm repo add elastic https://helm.elastic.co
helm install elastic elastic/elasticsearch --set volumeClaimTemplate.resources.requests.storage=10Gi
kubectl get pods --namespace=default -l app=elasticsearch-master -w
```



# Referências

[Elasticsearch - Definições, Arquitetura e Boas Práticas](https://www.youtube.com/watch?v=-fAq1B81nRI)

[https://logz.io/blog/elasticsearch-cluster-tutorial/](https://logz.io/blog/elasticsearch-cluster-tutorial/)

[https://addons.mozilla.org/en-US/firefox/addon/elasticvue/](https://addons.mozilla.org/en-US/firefox/addon/elasticvue/)

[https://github.com/prometheus-community/elasticsearch_exporter](https://github.com/prometheus-community/elasticsearch_exporter)

https://phoenixnap.com/kb/elasticsearch-kubernetes