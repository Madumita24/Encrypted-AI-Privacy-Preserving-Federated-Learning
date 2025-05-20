import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import tensorflow as tf

# Path to regional CSVs
data_dir = "data"
regions = ["Region_A.csv", "Region_B.csv", "Region_C.csv", "Region_D.csv", "Region_E.csv"]
all_files = [os.path.join(data_dir, f) for f in regions]

# Load and combine all region data
df = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)

# Drop non-feature columns
X = df.drop(columns=["user_id", "region", "is_suspicious"], errors='ignore')
y = df["is_suspicious"]

# One-hot encode 'device_type'
X = pd.get_dummies(X, columns=["device_type"], drop_first=True)

# Normalize numeric features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Build the Neural Network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=20, batch_size=32)

# Predict and evaluate
y_pred = model.predict(X_test).flatten()
y_pred_classes = (y_pred > 0.5).astype(int)
roc_score = roc_auc_score(y_test, y_pred)

# Print classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred_classes))
print("ROC-AUC Score:", roc_score)

# Plot Confusion Matrix
cm = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix (Centralized)')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.savefig("centralized_confusion_matrix.png")
plt.show()

# Plot training history
plt.figure(figsize=(10, 4))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.title('Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.tight_layout()
plt.savefig("centralized_training_accuracy.png")
plt.show()
