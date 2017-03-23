from picamera import PiCamera
from time import sleep
from datetime import datetime
from pusher import Pusher

seconds_between_photos = 15
pusher_app_id = '<INSERT_YOUR_PUSHER_APP_ID_HERE>'
pusher_key = '<INSERT_YOUR_PUSHER_APP_KEY_HERE>'
pusher_secret = '<INSERT_YOUR_PUSHER_APP_SECRET_HERE>'
hostname =  '<INSERT_YOUR_NGROK_HTTPS_URL_HERE>'

camera = PiCamera()

pusher = Pusher(pusher_app_id, pusher_key, pusher_secret)

# If you need to rotate the camera
# camera.rotation = 180
camera.resolution = (640, 480)

while True:
    try:
        sleep(seconds_between_photos)
        date = datetime.now().strftime('%m-%d-%Y-%H:%M:%S')
        camera.annotate_text = date
        filename = '/photos/' + date + '.jpg'
        camera.capture('/var/www/html' + filename)
        url = hostname + filename
        pusher.trigger('photos', 'new_photo', {'url': url})
    except Exception as e:
        print ('Error:', e)
