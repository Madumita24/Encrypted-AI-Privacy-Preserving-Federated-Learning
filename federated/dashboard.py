import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load metrics
with open("metrics.json", "r") as f:
    data = json.load(f)

accuracy = pd.DataFrame(data["accuracy"], columns=["Round", "Accuracy"])
loss = pd.DataFrame(data["loss"], columns=["Round", "Loss"])

st.title("Federated Learning Dashboard")

# Accuracy Plot
st.subheader("Federated Accuracy vs Rounds")
fig1, ax1 = plt.subplots()
ax1.plot(accuracy["Round"], accuracy["Accuracy"], marker='o', label="Federated Accuracy")
ax1.set_xlabel("Round")
ax1.set_ylabel("Accuracy")
ax1.set_ylim(0, 1)
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)

# Loss Plot
st.subheader("Federated Loss vs Rounds")
fig2, ax2 = plt.subplots()
ax2.plot(loss["Round"], loss["Loss"], marker='o', color='orange', label="Federated Loss")
ax2.set_xlabel("Round")
ax2.set_ylabel("Loss")
ax2.grid(True)
ax2.legend()
st.pyplot(fig2)

st.success("Dashboard Ready!")
