version: "1.0"
permissions:
  - path: /srv/shared/project
    mode: 0775
    group: developers
  
  - path: /srv/shared/project/build
    mode: 0775
    group: developers
  
  - path: /srv/shared/project/config
    mode: 0770
    group: developers 