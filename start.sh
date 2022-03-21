#!/bin/bash
if ! command -v helm &> /dev/null
then
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
        chmod 700 get_helm.sh
        ./get_helm.sh
fi
docker build -t olgamogish/postgres-fastapi-helm:latest .
docker push olgamogish/postgres-fastapi-helm:latest
helm install postgres postgres
helm install webapp webapp
kubectl patch configmap tcp-services -n ingress-nginx --patch "{\"data\":{\"8080\":\"default/webapp:8080\"}}"
kubectl patch deployment ingress-nginx-controller --patch "$(cat ingress-nginx-controller-patch.yaml)" -n ingress-nginx