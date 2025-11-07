"""
Simple Neural Network Implementation from Scratch

This example demonstrates a basic neural network implementation
for binary classification using NumPy.
"""

import numpy as np
import matplotlib.pyplot as plt


class SimpleNeuralNetwork:
    """A simple 2-layer neural network for binary classification."""
    
    def __init__(self, input_size, hidden_size, output_size):
        """
        Initialize the neural network with random weights.
        
        Args:
            input_size: Number of input features
            hidden_size: Number of neurons in hidden layer
            output_size: Number of output neurons
        """
        # Initialize weights with small random values
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
    
    def sigmoid(self, x):
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        """Derivative of sigmoid function."""
        return x * (1 - x)
    
    def forward(self, X):
        """
        Forward propagation through the network.
        
        Args:
            X: Input data
            
        Returns:
            tuple: Hidden layer output and final output
        """
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a1, self.a2
    
    def backward(self, X, y, output, learning_rate):
        """
        Backward propagation to update weights.
        
        Args:
            X: Input data
            y: True labels
            output: Network output
            learning_rate: Learning rate for gradient descent
        """
        m = X.shape[0]
        
        # Calculate gradients
        dz2 = output - y
        dW2 = np.dot(self.a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        
        dz1 = np.dot(dz2, self.W2.T) * self.sigmoid_derivative(self.a1)
        dW1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        
        # Update weights
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
    
    def train(self, X, y, epochs, learning_rate):
        """
        Train the neural network.
        
        Args:
            X: Training data
            y: Training labels
            epochs: Number of training iterations
            learning_rate: Learning rate
            
        Returns:
            list: Loss history
        """
        loss_history = []
        
        for epoch in range(epochs):
            # Forward propagation
            _, output = self.forward(X)
            
            # Calculate loss (binary cross-entropy)
            loss = -np.mean(y * np.log(output + 1e-8) + 
                           (1 - y) * np.log(1 - output + 1e-8))
            loss_history.append(loss)
            
            # Backward propagation
            self.backward(X, y, output, learning_rate)
            
            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")
        
        return loss_history
    
    def predict(self, X):
        """
        Make predictions.
        
        Args:
            X: Input data
            
        Returns:
            numpy.ndarray: Predictions (0 or 1)
        """
        _, output = self.forward(X)
        return (output > 0.5).astype(int)


def main():
    """Main function to demonstrate the neural network."""
    # Generate sample data (XOR problem)
    np.random.seed(42)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])  # XOR outputs
    
    # Create and train the network
    nn = SimpleNeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    print("Training Neural Network on XOR problem...")
    loss_history = nn.train(X, y, epochs=1000, learning_rate=0.5)
    
    # Make predictions
    predictions = nn.predict(X)
    print("\nPredictions:")
    for i, (input_val, pred, true) in enumerate(zip(X, predictions, y)):
        print(f"Input: {input_val}, Predicted: {pred[0]}, True: {true[0]}")
    
    # Plot loss
    plt.figure(figsize=(10, 6))
    plt.plot(loss_history)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Time')
    plt.grid(True)
    plt.savefig('training_loss.png')
    print("\nLoss plot saved as 'training_loss.png'")


if __name__ == "__main__":
    main()
