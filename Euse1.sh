o '----开始 yum 升级---'
yum -y  update

#安装 wget
yum -y install wget
yum -y install vim*
yum -y install unzip

echo '----安装python selenium---'
yum -y install python3
yum -y install epel-release
yum -y install python-pip


pip3 install --upgrade pip
pip3 install selenium


echo '-----安装 谷歌浏览器---'
touch /etc/yum.repos.d/google-chrome.repo
echo '[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub' > /etc/yum.repos.d/google-chrome.repo

yum -y install google-chrome-stable 
mkdir -p /app/local
cd /app/local & wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum -y localinstall google-chrome-stable_current_x86_64.rpm

echo '----下载 chrome 驱动---'
google-chrome --version
cd /app/local
echo "Enter the your name: "  
read -p "chrome 驱动链接:" LIU
wget $LIU
echo '----添加 x 权限-----'
unzip chromedriver_linux64.zip
sudo chmod a+x /app/local/chromedriver

echo '-------添加软连接----'
ln -s /app/local/chromedriver  /usr/bin/chromedriver
cd /app/local & wget https://cdn.jsdelivr.net/gh/hngyedu/EUserv_extend/euserv_test_linux.py

echo '执行测试'
python3 euserv_test_linux.py
