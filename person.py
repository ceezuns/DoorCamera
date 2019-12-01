import face_recognition

class Person:

    def __init__(self, name, telegram_uid):
        # The persons name, this is what will be sent in the Telegram message.
        self.name = name
        # Load the image file, and create a face encoding.
        self.image = face_recognition.load_image_file(self.name + ".jpg")
        self.face_encoding = face_recognition.face_encodings(self.image)[0]
        # This is the persons telegram unique id, it is what is used to send them a Telegram message.
        self.telegram_uid = telegram_uid
