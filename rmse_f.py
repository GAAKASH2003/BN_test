import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the result.out file into a DataFrame

file_path = '01.train/results.f.out'  # Update this to the correct path if needed
columns = ['data_fx', 'data_fy', 'data_fz', 'pred_fx', 'pred_fy', 'pred_fz']
df = pd.read_csv(file_path, delim_whitespace=True, comment='#', header=None, names=columns)

# Calculate RMSE for fx, fy, and fz
rmse_fx = np.sqrt(np.mean((df['data_fx'] - df['pred_fx'])**2))
rmse_fy = np.sqrt(np.mean((df['data_fy'] - df['pred_fy'])**2))
rmse_fz = np.sqrt(np.mean((df['data_fz'] - df['pred_fz'])**2))

# Function to plot RMSE
def plot_rmse(actual, predicted, rmse, label, filename):
    plt.figure(figsize=(6, 6))
    plt.scatter(actual, predicted, color='red', alpha=0.6, label='Data')
    plt.plot([actual.min(), actual.max()], [actual.min(), actual.max()], 'k-', lw=2)
    plt.title(f'{label} (RMSE = {rmse:.4f} eV/Å)', fontsize=14)
    plt.xlabel('DFT Force (eV/Å)', fontsize=12)
    plt.ylabel('NNP Force (eV/Å)', fontsize=12)
    plt.grid(alpha=0.3)
    plt.savefig(filename)
    plt.show()

# Generate plots
plot_rmse(df['data_fx'], df['pred_fx'], rmse_fx, '$f_x$', 'fx_rmse_plot.png')
plot_rmse(df['data_fy'], df['pred_fy'], rmse_fy, '$f_y$', 'fy_rmse_plot.png')
plot_rmse(df['data_fz'], df['pred_fz'], rmse_fz, '$f_z$', 'fz_rmse_plot.png')
