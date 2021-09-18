### Tool Installieren

cd /etc/apache2/mods-enabled

ln -s ../mods-available/cgi.load

a2enmod cgi

apt install -y git-all

apt install software-properties-common

add-apt-repository ppa:deadsnakes/ppa

apt install python3.9

python3.9 --version

chmod 755 auf alle files

cd /var/www/tool.betriebskostenabrechnung-einfach-gemacht.com

git clone https://github.com/ChristopherWy/betriebskostenabrechnung.git

cd ..

cp -r betriebskostenabrechnung/* /var/www/tool.betriebskostenabrechnung-einfach-gemacht.com/

chmod 755 index.cgi