version: "1.0"
permissions:
  - path: ~/projects/webapp
    mode: 0755
    owner: user1
  
  - path: ~/projects/webapp/config
    mode: 0700
    owner: user1
  
  - path: ~/projects/webapp/logs
    mode: 0755
    owner: user1
    attributes: "+a" 