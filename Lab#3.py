import numpy as np
p = np.array([0.5, 0.1, 0.4])
x1 = np.array([10, -5, -5])
x2 = np.array([-5, -5, 10])
x3 = np.array([1.5, 1.5, 0])
x4 = np.array([0, 0, 0])
def utility(x):
    return np.sqrt(x + 5) / 15
u1 = utility(x1)
u2 = utility(x2)
u3 = utility(x3)
u4 = utility(x4)
eu1 = np.sum(p * u1)
eu2 = np.sum(p * u2)
eu3 = np.sum(p * u3)
eu4 = np.sum(p * u4)
results = {
    "Рішення I": eu1,
    "Рішення II": eu2,
    "Рішення III": eu3,
    "Рішення IV": eu4
}
print("Результати обчислень:\n")
for name, value in results.items():
    print(f"{name}: E(U) = {value:.4f}")
best = max(results, key=results.get)
print("\nНайкраще рішення:")
print(f"{best}, E(U) = {results[best]:.4f}")