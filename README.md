## AMQP architecture ( Advanced Message Queue Protocol)
publisher --> exchange --> queue --> consumer 
                       
## Local development  

### Start minikube
 ```
 minikube stop 
 minikube delete
 minikube start --cpus 4 --memory 8192
```

### Start minikube dashboard
 ```
 minikube dashboard 
```
 
### Create all the resources  
```
sh setup_project.sh
``` 

### Get pod name of queue-filler and port forward
```
kubectl get pods
kubectl port-forward queue-filler-d5766d677-72gt8 5000
```

### Go to localhost:5000

### Example Hyperparameters to post

```
{
    "batch_size": 16,
    "epochs": 1,
    "optimizer": "adam",
    "activation_function": "relu",
    "dropout_rate": 0.2,
    "number_conv_layers": 3,
    "number_channels_first_layer_cnn": 16,
    "cnn_channel_multiplier": 1.3,
    "number_flat_layers": 2,
    "number_neurons_first_flat_layer": 64,
    "flat_neuron_multiplier": 0.5
}
```

### Check the status of the message on the queue 
Go to RabbitMQ admin panel:
```
kubectl get pods
kubectl port-worward rabbitmq-deployment-77555f7d87-9bkg9 15672
```


### Get database pod name and ssh into the pod
```
kubectl get pods
kubectl exec -it postgresdb-0 bash
```

### Check if the data is saved to the database:
```
psql -d resultsdb -U admin
\dt
select * from result;
```