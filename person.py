import face_recognition

class Person:

    def __init__(self, name):
        # The persons name, this is what will be sent in the Telegram message.
        self.name = name
        # Load the image file, and create a face encoding.
        self.image = face_recognition.load_image_file(self.name + ".png")
        self.face_encoding = face_recognition.face_encodings(self.name + ".png")[0]