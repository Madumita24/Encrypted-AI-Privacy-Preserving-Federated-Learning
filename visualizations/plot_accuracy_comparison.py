import matplotlib.pyplot as plt

# Federated accuracy from your run_all.py
federated_accuracy = [
    (1, 0.6770),
    (2, 0.6972),
    (3, 0.7738),
    (4, 0.8162),
    (5, 0.8336),
    (6, 0.8522),
    (7, 0.8576),
    (8, 0.8784),
    (9, 0.8964),
    (10, 0.9006),
]

# Federated loss from  logs after running the run_all.py
federated_loss = [
    (1, 0.6107),
    (2, 0.5381),
    (3, 0.4599),
    (4, 0.3980),
    (5, 0.3529),
    (6, 0.3139),
    (7, 0.2860),
    (8, 0.2609),
    (9, 0.2391),
    (10, 0.2275),
]

# Centralized final accuracy (set your actual value here)
centralized_accuracy = 0.93

# Extract data for plots
rounds = [r for r, _ in federated_accuracy]
acc_values = [a for _, a in federated_accuracy]
loss_values = [l for _, l in federated_loss]

# Plot Accuracy vs Rounds
plt.figure(figsize=(10, 5))
plt.plot(rounds, acc_values, marker='o', label="Federated Accuracy")
plt.axhline(y=centralized_accuracy, color='red', linestyle='--', label=f"Centralized Accuracy ({centralized_accuracy:.2f})")
plt.title("Federated vs Centralized Accuracy")
plt.xlabel("Round")
plt.ylabel("Accuracy")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("federated_vs_centralized_accuracy.png")
plt.show()

# Plot Loss vs Rounds
plt.figure(figsize=(10, 5))
plt.plot(rounds, loss_values, marker='o', color='orange', label="Federated Loss")
plt.title("Federated Loss per Round")
plt.xlabel("Round")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("federated_loss_plot.png")
plt.show()
