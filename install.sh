#!/bin/bash
if ! command -v helm &> /dev/null
then
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
        chmod 700 get_helm.sh
        ./get_helm.sh
fi
docker build -t olgamogish/postgres-fastapi-helm:latest .
docker push olgamogish/postgres-fastapi-helm:latest
kubectl apply -f https://raw.githubusercontent.com/reactive-tech/kubegres/v1.15/kubegres.yaml
kubectl apply -f pg-secret.yaml
kubectl apply -f postgres-kubegres.yaml
while [ $(kubectl get po | grep Running | wc -l) != 2 ]
do
        echo "Not all pods are running, wait 5 sec..."
        sleep 5
done
helm install webapp webapp