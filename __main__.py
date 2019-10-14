from person import Person
from camera import Camera
import json

def main():
    # Initialize a camera
    camera = Camera(device_id, persons)
    # Read from this camera.
    camera.read()

if __name__ == "__main__":
    main()