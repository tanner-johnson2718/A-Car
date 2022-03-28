cd mjpg-streamer
sudo rm -rf /usr/local/share/mjpg-streamer
sudo rm -rf /usr/local/bin/mjpg-streamer
sudo rm -rf /usr/local/lib/mjpg-streamer
make clean
make
sudo make install
cd ..