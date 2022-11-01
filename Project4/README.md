# Project 4

## Documentation

1) Created `/etc/hosts`, where the private key was typed, followed by the shortcut name for the instance.
2) `ssh -i privkey.pem ubuntu@ServerOne` and `ssh -i privkey.pem ubuntu@ServerTwo`
3)
	- haproxy.cfg was modifed, with location being `/etc/haproxy/haproxy.cfg`
	- maxconn 1000 and 500 were added to Global and default sections. fronend was created with the public IP, with bind set to the private IP, and adding default-backend as web-servers. backend web-servers had a roundrobin balance, http option, and both servers along with their private Ip addresses
	- sudo systemctl reload haproxy
	- https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts
4)
	- index.html, `/var/www/html/html.index`
	- The original html text was tkane out and replaced with inividual sample text given.
	- index.html, `/var/www/html/html.index`, there is only one page of site content, so only one file was needed.
	- `sudo systemctl reload apache2`
	- Lecture, https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-:wq04
