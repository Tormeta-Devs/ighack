clear
sleep 2
echo -e "Installing"
sleep 1
pkg update -y
pkg upgrade -y
apt update -y
apt upgrade -y
pkg install python -y
apt install python
pkg install python2 -y
pkg install wget -y
pkg install lolcat -y
pip install lolcat
apt install lolcat -y
pip install install --upgrade pip
pip install requests --upgrade
pip install requests[socks]
pip install stem
pip install instagram-py
pkg install tor -y
cd 
wget -O ~/instapy-config.json "https://git.io/v5DGy"
cd /data/data/com.termux/files/usr/etc/tor
rm -rf torrc
cd $HOME/ighack
cp -r torrc /data/data/com.termux/files/usr/etc/tor
cd
echo "   "
clear
echo "Ante de usar el programa revise que en otra terminal este ejecutandose tor"
echo "   "
echo "Para ejecutar 'tor' inserta la misma palabra y entra e esta terminal nuevamente"

sleep 3
clear
