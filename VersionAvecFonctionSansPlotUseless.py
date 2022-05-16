import time
import numpy as np
import matplotlib.pyplot as plt


def cellularAutomatonTemperature(a, nbIterations=100, k=1e-1):
    copya = a.copy()
    historic = []
    for i in range(nbIterations):
        # Regle d'évolution de l'automate cellulaire
        copya = copya + k * (np.roll(copya, 1, axis=0) + np.roll(copya, -1, axis=0) + np.roll(copya, 1, axis=1) + np.roll(copya,-1,axis=1) - 4 * copya)
        historic.append(copya)
    return copya, historic


np.random.seed(42)
abefore = np.random.random((100, 100))
aafter, historic = cellularAutomatonTemperature(abefore, nbIterations=100, k=1e-1)

plt.figure("diff",figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.title("Before")
plt.imshow(abefore, cmap='hot', interpolation='nearest')
plt.subplot(1, 2, 2)
plt.title("After")
plt.imshow(aafter, cmap='hot', interpolation='nearest')
plt.show()


print(abefore)
print(aafter)
