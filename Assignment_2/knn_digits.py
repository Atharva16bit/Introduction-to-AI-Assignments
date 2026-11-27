from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

digits = load_digits()
X, y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

print(f"Test accuracy: {accuracy * 100:.2f}%")

sample = X_test[0].reshape(1, -1)
result = model.predict(sample)

print("Actual digit:", y_test[0])
print("Predicted digit:", result[0])

plt.imshow(sample.reshape(8, 8), cmap="gray")
plt.title(f"Predicted digit: {result[0]}")
plt.axis("off")
plt.show()
