#!/bin/bash
if ! command -v helm &> /dev/null
then
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
        chmod 700 get_helm.sh
        ./get_helm.sh
fi
docker build -t localhost:5000/webapp:latest .
helm install postgres postgres
helm install webapp webapp