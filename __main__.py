from person import Person
from camera import Camera
import configuration

def main():
    # Initialize a camera
    camera = Camera()
    # Read from this camera.
    camera.read()

if __name__ == "__main__":
    main()