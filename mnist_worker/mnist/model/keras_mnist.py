from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

import numpy as np


def add_conv_layer(model: Sequential, number_channels: int, activation: str, dropout_rate: float, input_shape=None):
    if input_shape is None:
        model.add(Conv2D(filters=number_channels, kernel_size=(3,3), activation=activation))
    else:
        model.add(Conv2D(filters=number_channels, kernel_size=(3,3), activation=activation, input_shape=input_shape))
    model.add(Dropout(rate=dropout_rate))
    model.add(MaxPooling2D())


def add_conv_layers(model: Sequential, input_shape, hyperparameters: dict):
    dropout_rate = hyperparameters['dropout_rate']
    activation_function = hyperparameters['activation_function']
    number_conv_layers = hyperparameters['number_conv_layers']
    number_channels_first_layer_cnn = hyperparameters['number_channels_first_layer_cnn']
    cnn_channel_multiplier = hyperparameters['cnn_channel_multiplier']

    add_conv_layer(model, number_channels=number_channels_first_layer_cnn, activation=activation_function, dropout_rate=dropout_rate, input_shape=input_shape)
    for layer_index in range(1, number_conv_layers):
        add_conv_layer(model=model,
                       number_channels=int(round(number_channels_first_layer_cnn * np.power(cnn_channel_multiplier, layer_index))),
                       activation=activation_function,
                       dropout_rate=dropout_rate)


def add_fully_connected_layer(model: Sequential, number_neurons: int, activation: str, dropout_rate: float):
    model.add(Dense(number_neurons, activation=activation))
    model.add(Dropout(rate=dropout_rate))


def add_fully_connected_layers(model: Sequential, hyperparameters: dict):
    dropout_rate = hyperparameters['dropout_rate']
    activation_function = hyperparameters['activation_function']
    number_flat_layers = hyperparameters['number_flat_layers']
    number_neurons_first_flat_layer = hyperparameters['number_neurons_first_flat_layer']
    flat_neuron_multiplier = hyperparameters['flat_neuron_multiplier']
    model.add(Flatten())
    add_fully_connected_layer(model=model,
                              number_neurons=number_neurons_first_flat_layer,
                              activation=activation_function,
                              dropout_rate=dropout_rate)
    for layer_index in range(1, number_flat_layers):
        add_fully_connected_layer(model=model,
                                  number_neurons=int(round(number_neurons_first_flat_layer * np.power(flat_neuron_multiplier, layer_index))),
                                  activation=activation_function,
                                  dropout_rate=dropout_rate)


def initialize_model(input_shape, hyperparameters: dict):
    model = Sequential()
    add_conv_layers(model=model, input_shape=input_shape, hyperparameters=hyperparameters)
    add_fully_connected_layers(model=model, hyperparameters=hyperparameters)
    model.add(Dense(10, activation='softmax'))
    model.compile(optimizer=hyperparameters['optimizer'],
                  loss='categorical_crossentropy',
                  metrics=['acc'])
    return model


def evaluate_model(x_train, y_train, x_test, y_test, input_shape, hyperparameters: dict):
    batch_size = hyperparameters['batch_size']
    epochs = hyperparameters['epochs']
    model = initialize_model(input_shape=input_shape, hyperparameters=hyperparameters)
    history = model.fit(x_train, y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        validation_data=(x_test, y_test),
                        verbose=2)
    results = {key[4:]: history.history[key][-1] for key in history.history.keys() if key[:4] == 'val_'}
    return results
