# Kubernetes

```
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanentemente ao seu shell.
```

```
alias k=kubectl
complete -F __start_kubectl k
```


```
List cotainers in Pod Kubernetes(2 args)
kubectl get pods do-visit-counter-frontend-85594cf655-65bwc -n [namespace] -o jsonpath='{.spec.containers[*].name}*'
```