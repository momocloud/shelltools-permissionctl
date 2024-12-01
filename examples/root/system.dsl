version: "1.0"
permissions:
  - path: /etc/passwd
    mode: 0644
    owner: root
    group: root
    attributes: "+i"
  
  - path: /etc/shadow
    mode: 0600
    owner: root
    group: shadow
    attributes: "+i"
  
  - path: /etc/ssl/private
    mode: 0700
    owner: root
    group: root
  
  - path: /var/log/secure
    mode: 0600
    owner: root
    group: root
    attributes: "+a,+i"