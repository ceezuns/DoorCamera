from person import Person
from camera import Camera
import configuration
import threading
import web

camera = None

def main():
    # Initialize a camera
    camera = Camera()
    # Read from this camera.
    camera_thread = threading.Thread(target=camera.read)
    camera_thread.start()
    # Start Website
    web_thread = threading.Thread(target=web.app.run, args=("0.0.0.0", 8080))
    web_thread.start()

if __name__ == "__main__":
    main()