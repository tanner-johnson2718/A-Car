cd mjpg-streamer
sudo mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -p 8090 -w /usr/local/share/mjpg-streamer/www" &
cd ..
python3 sensor_car.py &
python3 control_car.py &
