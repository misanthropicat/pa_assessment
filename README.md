## Purpose:
This project is an example of deployment of simple web application and necessary infrastructure with Helm.

## Used tech stack:
- FastAPI
- PostgreSQL
- Helm
- Docker

## Pre-requirements:
Having any of the following cluster:
- minikube on Linux host with `--driver=none` or Windows host with `--driver=hyperv` (both tested). Required addons: ingress, ingress-dns, metallb
- any other Kubernetes cluster + kubectl

## Installing:
1. Clone this repo
2. Run start.sh
3. Check: `kubectl get po`
Expected output is like the following:
```
NAME                               READY   STATUS    RESTARTS   AGE
pg-master                          1/1     Running   0          10m
pg-replica-64f7b8556c-t5w4g        1/1     Running   0          10m
webapp-b79dfdf5-zzzm8              1/1     Running   0          10m
```
4. Open browser: swagger is available on URL http://webapp.host.local/docs