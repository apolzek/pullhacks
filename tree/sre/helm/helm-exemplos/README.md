helm create basic

1-basic


helm template .
elm template . --show-only templates/service.yaml
helm install nginx .
helm upgrade --install nginx .
helm upgrade --install nginx . --dry-run
helm upgrade --install nginx . --dry-run --debug
helm ls
helm lint . && echo $?
helm template . --show-only templates/tests/test-connection.yaml
kubectl get svc -l helm.sh/chart=basic-0.1.0
helm delete nginx

helm docs
helm-docs

https://github.com/databus23/helm-diff
helm diff revision myhelloworld 1 2
helm diff revision nginx 1 .

-------------------------------------------

2-dependencias

helm create subchart # deve estar dentro da pasta charts
helm upgrade --install dependencias .
#Chart size can not be larger than 1MB 