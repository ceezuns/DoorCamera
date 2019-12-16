from flask import Flask, Response, url_for
import imutils, configuration, cv2, datetime
from imutils.video import WebcamVideoStream

app = Flask(__name__)
video_stream = WebcamVideoStream(src=configuration.camera["device_id"]).start()

def get():
	while True:
		frame = cv2.GaussianBlur(cv2.cvtColor(imutils.resize(video_stream.read(), width=400), cv2.COLOR_BGR2RGB), (7, 7), 0)
		timestamp = datetime.datetime.now()
		cv2.putText(frame, timestamp.strftime(
			"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		(flag, encodedImage) = cv2.imencode(".jpg", frame)
		if not flag:
			continue
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/")
def index():
	return '<img src=\"' + url_for('video_feed') + '\">'

@app.route('/video_feed')
def video_feed():
	return Response(get(), mimetype='multipart/x-mixed-replace; boundary=frame')
