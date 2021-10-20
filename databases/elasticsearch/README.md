```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.1

```

```
curl -X GET "localhost:9200/_cat/nodes?v=true&pretty"
```