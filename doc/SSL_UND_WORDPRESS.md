### SSL einrichten


vi /etc/apache2/sites-available/betriebskostenabrechnung-einfach-gemacht.com.conf

<VirtualHost *:80>

DocumentRoot /var/www/html/
ServerName betriebskostenabrechnung-einfach-gemacht.com
ServerAlias www.betriebskostenabrechnung-einfach-gemacht.com

<Directory /var/www/html/>
Options FollowSymlinks
AllowOverride All
Require all granted
</Directory>

ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

vi /etc/apache2/sites-available/betriebskostenabrechnung-einfach-gemacht.de.conf

<VirtualHost *:80>

DocumentRoot /var/www/html/
ServerName betriebskostenabrechnung-einfach-gemacht.de
ServerAlias www.betriebskostenabrechnung-einfach-gemacht.de

<Directory /var/www/html/>
Options FollowSymlinks
AllowOverride All
Require all granted
</Directory>

ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

a2dissite 000-default
a2ensite betriebskostenabrechnung-einfach-gemacht.com.conf
a2ensite betriebskostenabrechnung-einfach-gemacht.de.conf
a2enmod rewrite
systemctl restart apache2.service

apt-get update
apt install software-properties-common
add-apt-repository universe
apt update

apt install certbot python3-certbot-apache
certbot --apache

systemctl status certbot.timer

a2enmod ssl



### Wordpress einrichten


apt-get install -y wordpress mysql-server
mysql -u root -p
create database wordpress;
create user wp;
set password for wp = 'geheim';
GRANT ALL PRIVILEGES ON *.* TO 'wp'@'%';

ln -s /usr/share/wordpress /var/www/html/wordpress
cp /usr/share/wordpress/wp-config-sample.php /etc/wordpress/config-default.php
vi /etc/wordpress/config-default.php

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');
/** MySQL database username */
define('DB_USER', 'wp');
/** MySQL database password */
define('DB_PASSWORD', 'geheim');
/** MySQL hostname */
define('DB_HOST', 'localhost');

chown -R www-data: /var/www/html/wordpress/

vi /etc/apache2/sites-available/wordpress.conf
<VirtualHost *:80>
    DocumentRoot /srv/www/wordpress
    <Directory /srv/www/wordpress>
        Options FollowSymLinks
        AllowOverride Limit Options FileInfo
        DirectoryIndex index.php
        Require all granted
    </Directory>
    <Directory /srv/www/wordpress/wp-content>
        Options FollowSymLinks
        Require all granted
    </Directory>
</VirtualHost>

sudo a2ensite wordpress
a2enmod rewrite
a2dissite 000-default
service apache2 reload

update wp_option set option_value='https://betriebskostenabrechnung-einfach-gemacht.de/wordpress' where option_name='siteurl';




