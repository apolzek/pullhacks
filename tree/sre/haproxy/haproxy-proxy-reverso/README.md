# haproxy-proxy-reverso

## Versões

```
OS: Linux Mint 20.2
Docker: 20.10.10
docker-compose: 1.29.2
HAProxy(imagem): haproxy:2.3
nginx(imagem): latest
```

## Passo a passo

```
docker-compose up -d

# output:
Creating haproxy-proxy-reverso_nginx-blue_1     ... done
Creating haproxy-proxy-reverso_nginx-pink_1     ... done
Creating haproxy-proxy-reverso_nginx-internal_1 ... done
Creating haproxy-proxy-reverso_haproxy_1        ... done
Creating haproxy-proxy-reverso_nginx-red_1      ... done
```

```
docker-compose ps
```

Acesse no navegador:

```
http://localhost
http://localhost/pink
http://localhost:1234/stats
```

Artigo: https://apolzek.github.io/2021-10-13-haproxy-como-proxy-reverso/