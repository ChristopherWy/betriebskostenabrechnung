### Subdomain

vi /etc/hosts

178.250.170.169 tool.betriebskostenabrechnung-einfach-gemacht.com

vi /etc/apache2/sites-available/tool.betriebskostenabrechnung-einfach-gemacht.com.conf

<VirtualHost *:80>

DocumentRoot /var/www/tool.betriebskostenabrechnung-einfach-gemacht.com

ServerName tool.betriebskostenabrechnung-einfach-gemacht.com

ServerAlias www.tool.betriebskostenabrechnung-einfach-gemacht.com

<Directory /var/www/tool.betriebskostenabrechnung-einfach-gemacht.com/>
Options FollowSymlinks
AllowOverride All
Require all granted
Options +ExecCGI
AddHandler cgi-script .cgi .pl .py
</Directory>

ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

mkdir -p /var/www/tool.betriebskostenabrechnung-einfach-gemacht.com

systemctl restart apache2.service

a2ensite tool.betriebskostenabrechnung-einfach-gemacht.com

systemctl reload apache2
 
 certbot --apache