## Purpose:
This project is an example of deployment of simple web application and necessary infrastructure with Helm.

## Used tech stack:
- FastAPI
- Kubegres
- Helm
- Docker

## Pre-requirements:
Having any of the following cluster:
- minikube on Linux host with `--driver=none` or Windows host with `--driver=hyperv` (both tested). Required addons: ingress, ingress-dns, metallb
- any other Kubernetes cluster + kubectl

## Installation:
1. Clone this repo
2. Run install.sh
3. Check deployment
Expected output is like the following:
```
C:\>kubectl get po
NAME                      READY   STATUS    RESTARTS   AGE
webapp-55679cc648-6x7tg   1/1     Running   0          22s
webapp-pg-1-0             1/1     Running   0          42s
webapp-pg-2-0             1/1     Running   0          31s

C:\>kubectl get svc
NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
kubernetes          ClusterIP   10.96.0.1        <none>        443/TCP    17h
webapp              ClusterIP   10.102.147.153   <none>        8080/TCP   30s
webapp-pg           ClusterIP   None             <none>        5432/TCP   39s
webapp-pg-replica   ClusterIP   None             <none>        5432/TCP   28s

C:\>kubectl get ing
NAME             CLASS   HOSTS               ADDRESS        PORTS   AGE
ingress-webapp   nginx   webapp.host.local   172.27.95.23   80      39s

C:\>kubectl get deploy
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
webapp   1/1     1            1           52s
```
4. Open browser: swagger is available on URL http://webapp.host.local/docs

## Unistallation:
Run uninstall.sh