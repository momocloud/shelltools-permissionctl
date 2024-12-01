version: "1.0"
permissions:
  - path: /var/lib/mysql
    mode: 0750
    owner: mysql
    group: mysql
  
  - path: /etc/mysql/my.cnf
    mode: 0644
    owner: root
    group: root
    attributes: "+i"
  
  - path: /var/log/mysql
    mode: 0755
    owner: mysql
    group: adm
    attributes: "+a" 