import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

# Load the CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Preprocess the data
x_train = x_train / 255.0
x_test = x_test / 255.0
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Define the model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('Test accuracy:', test_acc)


# new_images = str('cat.jpg')
# predictions = model.predict(new_images)

from PIL import Image
import numpy as np

# Load the image
image = Image.open('cat.jpg')

# Resize the image to match the input shape expected by the model
image = image.resize((32, 32))

# Convert the image to a numpy array
image_array = np.array(image)

# Normalize the pixel values to the range [0, 1]
image_array = image_array / 255.0

# Add a batch dimension to the numpy array
image_array = np.expand_dims(image_array, axis=0)

# Make a prediction using the trained model
predictions = model.predict(image_array)

# Print the predicted class
predicted_class = np.argmax(predictions)
print('Predicted class:', predicted_class)
