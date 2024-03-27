import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Reading the dataset
df = pd.read_csv('dataset.csv')
df.info()
df.describe()

# Dropping the 'time [s]' column as it doesn't seem relevant for classification
df = df.drop(columns=['time [s]'])

# Splitting dataset
X = df.drop('evm', axis=1) # Assuming 'evm' is the target variable
y = df['evm']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Defining the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear')) # Assuming a regression problem; change activation for classification.

# Compiling the model
model.compile(optimizer='adam', loss='mse') # Use 'categorical_crossentropy' for multi-class classification

# Training the model
model.fit(X_train_scaled, y_train, epochs=100, batch_size=10, validation_split=0.2)

test_loss = model.evaluate(X_test_scaled, y_test)

print(f'Test Loss: {test_loss}')