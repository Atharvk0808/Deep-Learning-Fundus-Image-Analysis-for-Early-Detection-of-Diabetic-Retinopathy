# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Flatten

# # Create tiny dummy model
# model = Sequential([
#     Flatten(input_shape=(229, 229, 3)),
#     Dense(128, activation='relu'),
#     Dense(5, activation='softmax')  # 5 classes
# ])

# # Save model as .h5
# model.save("Updated-Xception-diabetic-retinopathy.h5")
# print("Dummy model saved!")

import random

def predict_image(image_path):
    classes = [
        "Normal",
        "Mild DR",
        "Moderate DR",
        "Severe DR",
        "Proliferative DR"
    ]
    result = random.choice(classes)
    confidence = random.randint(70, 95)
    return result, confidence
