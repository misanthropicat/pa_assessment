## H2 Purpose:
This project is an example of deployment of simple web application and necessary infrastructure with Helm.

## H2 Used tech stack:
- FastAPI
- PostgreSQL
- Helm
- Docker
- Nginx

## H2 Pre-requirements:
Having any of the following cluster:
- minikube on Linux-based host with `--driver=none` (tested)
- any other Kubernetes cluster + kubectl

## H2 Installing:
1. Clone this repo
2. Run start.sh
3. Check: `kubectl get po`
Expected output is like the following:
```
NAME                               READY   STATUS    RESTARTS   AGE
nginx-deployment-86b659b7f-zb6w7   1/1     Running   0          10m
pg-master                          1/1     Running   0          10m
pg-replica-64f7b8556c-t5w4g        1/1     Running   0          10m
webapp-b79dfdf5-zzzm8              1/1     Running   0          10m
```

## H2 Usage:
1. Get Nginx URL `minikube service url`
```
|-------------|---------------|--------------|----------------------------|
|  NAMESPACE  |     NAME      | TARGET PORT  |            URL             |
|-------------|---------------|--------------|----------------------------|
| default     | kubernetes    | No node port |
| default     | nginx-service |           80 | http://10.244.128.12:30009 |
| default     | pg-master     | No node port |
| default     | pg-replica    | No node port |
| default     | webapp        | No node port |
| kube-system | kube-dns      | No node port |
|-------------|---------------|--------------|----------------------------|
```
2. Swagger is available on `<nginx-service>/docs`