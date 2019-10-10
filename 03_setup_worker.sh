#!/usr/bin/env bash

eval $(minikube docker-env)

docker build -t mnist-worker mnist_worker/
kubectl apply -f mnist_worker/worker.yaml

eval $(minikube docker-env -u)