Artigo: https://www.digitalocean.com/community/tutorials/how-to-implement-distributed-tracing-with-jaeger-on-kubernetes

```
kind create cluster --config kind-example-config.yaml
```

```
kubectl create namespace observability # <1>
kubectl create -f https://github.com/jaegertracing/jaeger-operator/releases/download/v1.29.0/jaeger-operator.yaml -n observability # <2>

kubectl apply -f jaeger-simplest.yaml
```

```
https://gitlab.com/devlabops/pocs/container_registry

registry.gitlab.com/devlabops/pocs/do-visit-counter-frontend
registry.gitlab.com/devlabops/pocs/do-visit-counter-backend
```