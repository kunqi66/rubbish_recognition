import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from time import *
layers = tf.keras.layers




# 加载数据
def data_load(data_dir, img_height, img_width, batch_size):
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        label_mode='categorical',
        validation_split=0.1,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        label_mode='categorical',
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)
    class_names = train_ds.class_names
    return train_ds, val_ds, class_names


def model_load(IMG_SHAPE=(224, 224, 3), class_num=6):
    model = tf.keras.models.Sequential([
        tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=IMG_SHAPE),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(class_num, activation='softmax')
    ])
    model.summary()
    # 模型训练
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # loss函数修改过
    return model


# 展示训练过程的曲线
def show_loss_acc(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()), 1])
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.savefig('results_cnn.png', dpi=100)


def train(epochs):
    begin_time = time()
    train_ds, val_ds, class_names = data_load(".\\data\\trash_jpg", 224, 224, 16)
    print(class_names)
    model = model_load(class_num=len(class_names))
    history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)
    model.save("models/cnn_epoch30.h5")
    end_time = time()
    run_time = end_time - begin_time
    print('该循环程序运行时间：', run_time, "s")
    show_loss_acc(history)



if __name__ == '__main__':
    train(epochs=30)
