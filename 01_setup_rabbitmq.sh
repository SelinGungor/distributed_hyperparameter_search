#!/usr/bin/env bash

eval $(minikube docker-env)
docker build -t rabbitmq-with-management rabbitmq/

kubectl apply -f rabbitmq/rabbitmq-deployment.yaml
kubectl apply -f rabbitmq/rabbitmq-service.yaml
kubectl apply -f rabbitmq/rabbitmq-service-ui.yaml

SERVICE=rabbitmq-service

# Uncomment this part for local development
#sleep 3
#kubectl port-forward svc/rabbitmq-service-ui 15672:15672