import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

torch.manual_seed(42)

time = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
distance = torch.tensor([[10.0], [20.0], [30.0], [40.0], [50.0]])

model = nn.Linear(1, 1)

loss_function = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

loss_values = []

for epoch in range(100):
    prediction = model(time)
    loss = loss_function(prediction, distance)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    loss_values.append(loss.item())

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

with torch.no_grad():
    result = model(torch.tensor([[7.0]]))

print(f"\nPredicted distance in 7 hours: {result.item():.2f} km")

plt.plot(range(1, 101), loss_values)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("PyTorch Training Loss")
plt.show()
