#!/usr/bin/env bash


sh 01_setup_rabbitmq.sh

sh 02_setup_kubedb_postgres.sh

sh 03_setup_worker.sh

sh 04_setup_queue_api.sh


#port forward
# kubectl port-forward queue-filler-d5766d677-mrlfd 5000


#post payload

#{
#    "batch_size": 16,
#    "epochs": 1,
#    "optimizer": "adam",
#    "activation_function": "relu",
#    "dropout_rate": 0.2,
#    "number_conv_layers": 3,
#    "number_channels_first_layer_cnn": 16,
#    "cnn_channel_multiplier": 1.3,
#    "number_flat_layers": 2,
#    "number_neurons_first_flat_layer": 64,
#    "flat_neuron_multiplier": 0.5
#}

#psql -d resultsdb -U admin
# \dt