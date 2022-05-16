import time
import numpy as np
import matplotlib.pyplot as plt

a = np.random.random((100, 100))
print(a)

k = 1e-1

plotTheFigure = False
if plotTheFigure:
    plt.figure(figsize=(10, 10))
for i in range(50):
    if plotTheFigure:
        plt.imshow(a, cmap='hot', interpolation='nearest')
    # Regle d'évolution de l'automate cellulaire
    a = a + k * (
                np.roll(a, 1, axis=0) + np.roll(a, -1, axis=0) + np.roll(a, 1, axis=1) + np.roll(a, -1, axis=1) - 4 * a)
    # plt.show()
    if plotTheFigure:
        plt.pause(0.2)

print(a)
