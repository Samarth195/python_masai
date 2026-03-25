import numpy as np
import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

loss = [0.95, 0.88, 0.80, 0.72, 0.65, 0.58, 0.50, 0.43, 0.37, 0.30]

# line plot
plt.figure(figsize=(6, 4))
plt.plot(epochs, loss, marker='o')
plt.title('Loss vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()

# scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(epochs, loss)
plt.title('Epoch vs Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

# bar chart
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(6, 4))
plt.bar(models, accuracy)
plt.title('Model Accuracy')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.show()