#!/usr/bin/bash
helm del webapp
kubectl delete -f https://raw.githubusercontent.com/reactive-tech/kubegres/v1.15/kubegres.yaml