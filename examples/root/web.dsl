version: "1.0"
permissions:
  - path: /etc/nginx/nginx.conf
    mode: 0644
    owner: root
    group: root
    attributes: "+i"
  
  - path: /var/www/html
    mode: 0755
    owner: www-data
    group: www-data
  
  - path: /var/log/nginx
    mode: 0755
    owner: www-data
    group: adm
    attributes: "+a" 