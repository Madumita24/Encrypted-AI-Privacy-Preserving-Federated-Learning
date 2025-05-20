# Encrypted-AI-Privacy-Preserving-Federated-Learning
This project simulates a real-world federated learning setup for detecting suspicious user behavior using synthetic regional login/session data — all while preserving data privacy by avoiding centralized data collection.

## 🚀 Project Overview

- **Goal:** Detect abnormal login behavior without sharing raw data
- **Approach:** Use federated learning (with Flower) to train a shared model across distributed synthetic clients (regions)
- **Tech:** Python, TensorFlow, Flower, Pandas, Matplotlib

## 🧠 Features

- Federated learning simulation with 5 clients (Region_A to Region_E)
- No raw data leaves local clients
- Centralized vs. federated accuracy comparison
- Visualization of accuracy per round
- Full automation script to launch server + clients

## 🧪 Architecture

```plaintext
               +----------------------+
               |      Server (FL)     |
               +----------+-----------+
                          |
         +----------------+----------------+
         |                |                |
    Region_A         Region_B         Region_C
    client.py        client.py        client.py
       .                 .                .
    Region_D         Region_E         (more...)
