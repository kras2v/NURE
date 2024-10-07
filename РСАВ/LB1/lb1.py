import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images_reshaped = train_images.reshape(train_images.shape[0], -1)
test_images_reshaped = test_images.reshape(test_images.shape[0], -1)

plt.figure(figsize=(9, 9))

for idx, (img, label) in enumerate(zip(train_images[:9], train_labels[:9])):
    subplot = plt.subplot(3, 3, idx + 1)
    subplot.imshow(img, cmap='gray')
    subplot.axis('off')
    subplot.set_title(f'Digit: {label}')

plt.suptitle('First 9 digits from MNIST Training Dataset')
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(train_labels, bins=np.arange(11) - 0.5, edgecolor='black')
plt.title('Digit Frequency in Training Set')
plt.xticks(np.arange(10))

plt.subplot(1, 2, 2)
plt.hist(test_labels, bins=np.arange(11) - 0.5, edgecolor='black')
plt.title('Digit Frequency in Testing Set')
plt.xticks(np.arange(10))

plt.show()

classifier = LogisticRegression(max_iter=100, n_jobs=6)
classifier.fit(train_images_reshaped, train_labels)

coefficients = classifier.coef_.copy()
max_scale = np.abs(coefficients).max()

plt.figure(figsize=(10, 5))
for i in range(10):
    coef_plot = plt.subplot(2, 5, i + 1)
    coef_plot.imshow(coefficients[i].reshape(28, 28), cmap='gray', vmin=-max_scale, vmax=max_scale, interpolation='bilinear')
    coef_plot.axis('off')
    coef_plot.set_title(f'Digit: {i}')

plt.suptitle('Coefficients per Digit')
predicted_labels = classifier.predict(test_images_reshaped)
accuracy = accuracy_score(test_labels, predicted_labels)
plt.suptitle(f'Accuracy of Logistic Regression: {accuracy:.4f}')
plt.show()
