import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from main import NeuralNetwork

# Gerando dados sintéticos
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# Separando em dados de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando um objeto NeuralNetwork
nn = NeuralNetwork(num_classes=2)

# Treinando o modelo
accuracy, f1, precision, recall = nn.train(X_train, y_train, X_test, y_test)
print(f"Accuracy: {accuracy}, F1-score: {f1}, Precision: {precision}, Recall: {recall}")

# Realizando previsões em novos dados
X_new = np.random.rand(5, 10)  # Gerando 5 exemplos com 10 features cada
y_pred = nn.predict(X_new)
print(f"Predictions: {y_pred}")
