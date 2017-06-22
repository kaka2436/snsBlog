sudo apt-get install git git-core
git config --global user.name "kaka2436"
git config --global user.email "kaka2436@163.com"
ssh-keygen -t rsa -C "kaka2436@163.com"
sudo apt-get install python-setuptools python-dev build-essential
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip
sudo apt-get install openssl libssl-dev
sudo apt-get install libpcre3 libpcre3-dev
sudo apt-get install zlib1g-dev
sudo apt-get install build-essential
sudo apt-get install libtool
cd /usr/local/src
sudo wget http://nginx.org/download/nginx-1.4.2.tar.gz
sudo tar -zxvf nginx-1.4.2.tar.gz
sudo cd nginx-1.4.2
sudo ./configure --prefix=/usr/local/nginx
sudo make
sudo make install
sudo /usr/local/nginx/sbin/nginx

