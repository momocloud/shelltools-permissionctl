version: "1.0"
permissions:
  - path: /path/to/file1
    mode: 0644
    owner: user1
    group: group1
    attributes: "+i"
  
  - path: /path/to/directory
    mode: 0755
    owner: user1
    group: group1
    attributes: "+t"
    recursive: true 