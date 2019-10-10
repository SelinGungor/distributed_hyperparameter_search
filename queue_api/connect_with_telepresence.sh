#!/usr/bin/env bash

eval $(minikube docker-env)
docker build -t queue-create .
kubectl apply -f queue_api.yaml

eval $(minikube docker-env -u)

docker build . -t queue-create:telepresence

# Inject project in local cluster
telepresence \
  --swap-deployment queue-filler \
  --expose 5000:5000 --docker-run \
  -v /Users/selingungor/dataengineering/workqueue_example_rabbitmq/app:/app \
  queue-create:telepresence \
  -p 5000 python -u /app/main.py

eval $(minikube docker-env)
