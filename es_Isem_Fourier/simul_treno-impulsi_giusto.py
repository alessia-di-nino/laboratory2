import matplotlib.pyplot as plt
import numpy as np

# Create a figure with 8 subplots arranged in 2 rows and 4 columns
fig, axs = plt.subplots(2, 4, figsize=(16, 8))

delta = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
n = 10000
xs = np.linspace(-2, 2, 1000)

for i, ax in enumerate(axs.flatten()):
    x = xs

    y = delta[i] + sum(
        (2 / (k * np.pi)) * np.sin(k * np.pi * delta[i]) * np.cos(2 * np.pi * k * x) for k in range(1, n, 1)
    )
    y1 = delta[i] + sum(
        ((2 / (k * np.pi)) * np.cos((k * 2 * np.pi * 1000 * x) + np.arctan(-((k * 1000) / 10))) * np.sin(
            (k * np.pi * delta[i])
        )) * (1 / np.sqrt(1 + ((k * 1000) / 10) ** 2)) for k in range(1, n, 1)
    )

    ax.plot(x, y, label='Treno di impulsi')
    ax.plot(x, y1, label='Ripple')
    ax.set_title(f'$\delta$ = {delta[i]}')
    ax.legend()

# Common X label below the entire figure
fig.text(0.5, 0.02, 'Tempo [T]', ha='center', va='center', fontsize=14)

# Common Y label to the left of the entire figure
fig.text(0.02, 0.5, 'Segnale simulato', ha='center', va='center', rotation='vertical', fontsize=14)

plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])  # Adjust the rectangle to make room for labels



# Create a figure with 8 subplots arranged in 2 rows and 4 columns - ripple only
fig, axs = plt.subplots(2, 4, figsize=(16, 8))

delta = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
n = 10000
xs = np.linspace(-2, 2, 1000)

for i, ax in enumerate(axs.flatten()):
    x = xs


    y1 = delta[i] + sum(
        ((2 / (k * np.pi)) * np.cos((k * 2 * np.pi * 1000 * x) + np.arctan(-((k * 1000) / 10))) * np.sin(
            (k * np.pi * delta[i])
        )) * (1 / np.sqrt(1 + ((k * 1000) / 10) ** 2)) for k in range(1, n, 1)
    )

    y1 -= np.mean(y1)

    ax.plot(x, y1, color = "orange")
    ax.set_title(f'$\delta$ = {delta[i]}')

# Common X label below the entire figure
fig.text(0.5, 0.02, 'Tempo [T]', ha='center', va='center', fontsize=14)

# Common Y label to the left of the entire figure
fig.text(0.02, 0.5, 'Segnale simulato', ha='center', va='center', rotation='vertical', fontsize=14)

plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])  # Adjust the rectangle to make room for labels
plt.show()
