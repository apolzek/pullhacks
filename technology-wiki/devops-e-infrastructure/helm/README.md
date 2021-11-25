# Helm

## Resumão

- Comumente usado para empacotamento de aplicações kubernetes
- Surgiu em 2015, empresa criadora foi adquirida pela Microsoft
- Projeto graduado na CNCF
- Projeto baseado em Golang
- Versão Helm2 utilizada o Tiller(client/server)
- Versão Helm3 interage direto com o kube-api, não necessita do Tiller
- É um gerenciador de pacotes, semelhante ao APT e YUM
- Chart é o pacote do helm que possui vários arquivos, entre eles:
    - Chart.yaml: que é a versão e metadados do chart, carrega as próprias informações
    - Vvalues.yaml: valores para otimizar e personalizar as entregas
    - Templates: arquivos que vão receber os valus e combinados vão gerar os arquivos(yaml) kubernetes
    - Repositório: onde sobe e também consome charts (hub.helm)
    - Release: instância de um chart, quando faz a instalação de um microserviço(helm install cria um release)
    - Arquivos tpl são arquivos auxiliares
    - NOTES.txt pós instalação, helper depois da instalação

* É possível adicionar um repositório remoto do helm com o comando *helm repo add <name> <url>*
* {{ .Release.Name }} 

## Comandos

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/nginx
helm search repo nginx
helm install my-release bitnami/nginx
helm upgrade my-release bitnami/nginx --values values.yaml
helm show values bitnami/nginx # Ver os values default
helm history my-release bitnami/nginx
helm rollback my-release
helm uninstall my-release

# Install namespace k8s
helm install my-release bitnami/nginx --namespace <namespace>

helm show values elastic/apm-server
helm list

helm create helm-template

helm install <example> ./chart --dry-run --debug
```

## Referências

https://github.com/helm/helm

https://helm.sh/docs/

https://www.youtube.com/watch?v=LuBvYTqN1cw

https://www.youtube.com/watch?v=sItjxM3hYrE

https://www.youtube.com/watch?v=47PBtVmQKRU