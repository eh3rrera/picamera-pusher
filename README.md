# picamera-pusher

Python script that takes pictures at a certain interval with the Raspberry Pi camera, then save them to a web server and publish the URL to a Pusher channel so an iOS app can show them in a realtime photo feed.

You can follow the [tutorial](https://pusher.com/tutorials/photo-feed-swift-raspberrypi/) to build this application or jump straight to the code.

## Getting Started

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

### Prerequisites

- A [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
- A [Raspberry Pi Camera Module](https://www.raspberrypi.org/products/camera-module-v2/)
- [ngrok](https://ngrok.com/)
- A [Pusher account](https://pusher.com/signup)

## Built With

* [Pusher](https://pusher.com/) - APIs to enable devs building realtime features
* [Python](https://www.python.org/) - A programming language that lets you work quickly
and integrate systems more effectively.

## Acknowledgments

* Thanks to [Pusher](https://pusher.com/) for sponsoring this tutorial.

## License
MIT
