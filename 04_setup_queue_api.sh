#!/usr/bin/env bash

eval $(minikube docker-env)
docker build -t queue-create queue_api/

kubectl apply -f queue_api/queue_api.yaml
kubectl apply -f queue_api/queue_service.yaml

eval $(minikube docker-env -u)
