```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev
$ wget https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.4.1/tensorflow-1.4.1-cp35-none-linux_armv7l.whl
$ sudo pip3 install tensorflow-1.4.1-cp35-none-linux_armv7l.whl
# 機械学習ライブラリのインストール
$ sudo apt-get install python3-pandas
$ sudo apt-get install python3-sklearn

# モデル可視化ツール インストール
$ sudo apt install python3-pydot graphviz

# matplotlib インストール
$ sudo pip3 install numpy psutil python-dateutil pytz tornado pyparsing six
$ sudo pip3 --no-cache-dir install matplotlib

# kerasとh5py インストール
$ sudo apt-get install python3-h5py
$ sudo pip3 install keras

# スワップ領域を拡大
$ sudo nano /etc/dphys-swapfile
# CONF_SWAPSIZE=100（約100 MB）となっている初期設定をCONF_SWAPSIZE=2048（2 GB）に変更
$ sudo /etc/init.d/dphys-swapfile restart

# OpenCV 3.1をインストール
$ sudo apt-get purge wolfram-engine
$ sudo apt-get purge libreoffice*
$ sudo apt-get clean
$ sudo apt-get autoremove
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install build-essential cmake pkg-config
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libgtk2.0-dev libgtk-3-dev
$ sudo apt-get install libcanberra-gtk*
$ sudo apt-get install libatlas-base-dev gfortran
$ cd ~
$ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.1.zip
$ unzip opencv.zip
$ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.1.zip
$ unzip opencv_contrib.zip
$ cd ~/opencv-3.3.1/
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.1/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..
$ make -j4
$ sudo make install
$ sudo ldconfig
```
