import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.keras.utils.set_random_seed(42)

quantity = np.array([[1], [2], [3], [4], [5]], dtype=np.float32)
price = np.array([[10], [20], [30], [40], [50]], dtype=np.float32)

model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer="sgd", loss="mean_squared_error")

history = model.fit(quantity, price, epochs=100, verbose=0)

prediction = model.predict(
    np.array([[7]], dtype=np.float32), verbose=0
)

print(f"Predicted price for 7 items: ₹{prediction[0][0]:.2f}")

plt.plot(history.history["loss"])
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("TensorFlow Training Loss")
plt.show()
