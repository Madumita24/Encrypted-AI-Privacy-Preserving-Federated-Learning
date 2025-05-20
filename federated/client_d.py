
import flwr as fl
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os 

def load_client_data(csv_path):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=["user_id", "region", "is_suspicious"], errors="ignore")
    X = pd.get_dummies(X, columns=["device_type"], drop_first=True)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    y = df["is_suspicious"].values
    return X_scaled, y

def create_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

class FederatedClient(fl.client.NumPyClient):
    def __init__(self, model, train_data):
        self.model = model
        self.x_train, self.y_train = train_data

    def get_parameters(self, config):
        return self.model.get_weights()

    def fit(self, parameters, config):
        self.model.set_weights(parameters)
        self.model.fit(self.x_train, self.y_train, epochs=3, batch_size=32, verbose=0)
        return self.model.get_weights(), len(self.x_train), {}

    def evaluate(self, parameters, config):
        self.model.set_weights(parameters)
        loss, accuracy = self.model.evaluate(self.x_train, self.y_train, verbose=0)
        return loss, len(self.x_train), {"accuracy": accuracy}

def main():
    # csv_path = "data/Region_D.csv"  # Replace with your client file
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "Region_D.csv")
    x, y = load_client_data(csv_path)
    model = create_model(x.shape[1])
    client = FederatedClient(model, (x, y))
    fl.client.start_numpy_client(server_address="localhost:8080", client=client)

if __name__ == "__main__":
    main()
