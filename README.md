# picamera-pusher

iOS app that shows photos in a feed in realtime from a [Raspberry Pi Python process](https://github.com/eh3rrera/picamera-pusher) using Pusher.

# Requirements

- A [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- A [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/)
- [ngrok](https://ngrok.com/)
- A [Pusher account](https://pusher.com/signup)

# Installation
1. Make sure you have all the development dependencies installed in your Raspberry Pi by executing `sudo apt-get install build-essential libssl-dev python-dev libffi-dev`.
2. [Install a web server](https://www.raspberrypi.org/documentation/remote-access/web-server/).
3. Create the directory `photos` under `/var/www/html/` and give it permissions (by changing the owner):
   - `sudo mkdir /var/www/html/photos`
   - `sudo chown -R pi:pi /var/www/html/photos`
4. Clone this repository and `cd` into it.
5. If you didn't have [virtualenv](https://virtualenv.pypa.io/en/stable/), install it with `sudo pip install virtualenv`.
6. Create virtual environment for the project with Python 3 `virtualenv -p python3 env`.
7. Activate `virtualenv` with `source env/bin/activate`.
8. Install requirements with `pip install -r requirements.txt`.
9. In another terminal, execute ngrok with `ngrok http 80` and copy the URL with HTTPS.
10. Modify the file `camera.py` to enter your Pusher credentials and ngrok URL. You can also change the time to take photos.
11. Execute `python camera.py`.
12. When your done, stop the program with `Ctrl-C` and deactivate your virutal environment with `deactivate`.

# License
MIT