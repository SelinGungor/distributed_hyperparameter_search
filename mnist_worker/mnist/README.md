# mnist-worker
Example repo for MNIST worker

## Hyperparameters

`batch_size`: Number of samples to train on per batch

`epochs`: Number of epochs (full iterations over dataset) to train for

`optimizer`: Which optimizer to use (`adam`, `sgd`, `adadelta`)

`activation_function`: Which activation function to use after every layer before the last (`sigmoid`, `tanh`, `relu`)

`dropout_rate`: Float between 0 and 0.5, determining how many random neurons to drop every batch

`number_conv_layers`: How many CNN layers to stack 

`number_channels_first_layer_cnn`: How many channels the first CNN layer should have

`cnn_channel_multiplier`: How many channels each sequential CNN layer should have based on it's predecessor

`number_flat_layers`: How many fully connected flattened layers to add

`number_neurons_first_flat_layer`: How many neurons the first flat layer should have

`flat_neuron_multiplier`: How many neurons each sequential flat layer should have based on it's predecessor
