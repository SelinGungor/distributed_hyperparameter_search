#!/usr/bin/env bash

cd postgres_object/ && { curl -fsSL https://github.com/kubedb/installer/raw/v0.13.0-rc.0/deploy/kubedb.sh | bash; cd -; }

kubectl get pods -n kube-system | grep kubedb-operator

kubectl get storageclasses

kubectl create secret generic postgres-secret \
--from-literal=POSTGRES_USER=admin \
--from-literal=POSTGRES_PASSWORD=admin

kubectl apply -f postgres_object/postgres_kubedb.yaml
kubectl apply -f postgres_object/postgres_pgadmin.yaml