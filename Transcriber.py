from keras.models import Sequential
from keras.layers import Convolution2D  # for 2d images
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
from keras_preprocessing.image import ImageDataGenerator
from keras.utils import plot_model

rgb = 2

cnn = Sequential()

# step 1: convolution
# slide feature detectors ("filters") along image
# results feature maps that form convolutional layer
cnn.add(Convolution2D(32, 3, 3, input_shape=(192, 108, 3), activation='relu'))  # 32, 3x3 filters

# step 2: pooling
cnn.add(MaxPool2D(pool_size=(2, 2)))

# step 3: flatten
# this vector will be the input of a future ann
cnn.add(Flatten())

# step 4: full connection
cnn.add(Dense(output_dim=128, activation='relu'))  # add hidden layers
cnn.add(Dense(output_dim=3, activation='sigmoid'))  # sigmoid for binary output

# compile cnn
cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# image augmentation - prevent overfitting
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_set = train_datagen.flow_from_directory(
    'train',
    target_size=(192, 108),
    batch_size=32)

test_set = test_datagen.flow_from_directory(
    'test',
    target_size=(192, 108),
    batch_size=32)

cnn.fit_generator(
    train_set,
    steps_per_epoch=8,  # we have 8k images in our training set
    epochs=1000,
    validation_data=test_set,
    validation_steps=2)

cnn.save('transcriber.h5')

# visualize training set results
# plot_model(cnn, to_file='model.png')
# plt.scatter(cnn.metrics[0][:, 50], cnn.metrics[0][:, 50], color='red')
# # plt.plot(X_train, regressor.predict(X_train), color='blue')
# plt.plot(cnn.metrics[0]. cnn.metrics[1], color = 'red')
# plt.title('Loss vs Accuracy')
# plt.xlabel(cnn.metrics_names[0])
# plt.ylabel(cnn.metrics_names[1])
# plt.show()
