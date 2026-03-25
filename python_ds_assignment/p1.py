import numpy as np
np.random.seed(42)
data = np.random.rand(100, 3)
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
normalized_data =(data - mean) / std

train = normalized_data[:80]
test = normalized_data[80:]

train[0,0] = 100
print("Original data shape:",data.shape)
print("Mean Shape:", mean.shape)
print("training data shape :", train.shape)
print("test data shape :", test.shape)
print("Note: Modifying the slice affected the original array, because it is a view of the original array.")