https://github.com/scaamanho/k3d-cluster


```
k3d cluster create my-multinode-cluster --servers 1 --agents 3 --port 9080:80@loadbalancer --port 9443:443@loadbalancer --api-port 6443 --k3s-server-arg '--no-deploy=traefik'
```