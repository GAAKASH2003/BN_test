import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

filename = '01.train/results.e.out'  

expected = []
predicted = []

with open(filename, 'r') as file:
    i = 0
    for line in file:
        if i == 0:  
            i += 1
            continue
        values = line.split()
        expected.append(float(values[0]))  
        predicted.append(float(values[1])) 

expected = np.array(expected)
predicted = np.array(predicted)

rmse = np.sqrt(np.mean((predicted - expected) ** 2))*1000
r2 = r2_score(expected, predicted)
print(f'RMSE = {rmse:.4f} meV/atom')
print(f'R² = {r2:.4f}')

plt.figure(figsize=(8, 6))
plt.scatter(expected, predicted, color='red', s=10)
plt.plot(expected, expected, color='black', linestyle='-')
plt.title('(a) Energy', fontsize=14, fontweight='bold')
plt.xlabel('DFT energy (eV/atom)', fontsize=12)
plt.ylabel('NNP energy (eV/atom)', fontsize=12)
plt.annotate(f'RMSE = {rmse:.2f} meV/atom\nR² = {r2:.4f}', xy=(0.05, 0.9), xycoords='axes fraction',
             fontsize=12, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()