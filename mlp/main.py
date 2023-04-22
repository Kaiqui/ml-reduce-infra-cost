import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

class NeuralNetwork:
    def __init__(self, num_classes, hidden_layers=(256, 128), learning_rate=0.001):
        self.num_classes = num_classes
        self.hidden_layers = hidden_layers
        self.learning_rate = learning_rate
        self.model = self._build_model()

    def _build_model(self):
        model = MLPClassifier(hidden_layer_sizes=self.hidden_layers, learning_rate_init=self.learning_rate, max_iter=10)
        return model

    def train(self, X_train, y_train, X_val, y_val):
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_val)
        accuracy = accuracy_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred, average='weighted')
        precision = precision_score(y_val, y_pred, average='weighted')
        recall = recall_score(y_val, y_pred, average='weighted')
        return accuracy, f1, precision, recall

    def predict(self, X_new):
        return self.model.predict(X_new)
