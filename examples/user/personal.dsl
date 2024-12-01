version: "1.0"
permissions:
  - path: ~/important_docs
    mode: 0700
    owner: user1
  
  - path: ~/.ssh
    mode: 0700
    owner: user1
  
  - path: ~/.ssh/config
    mode: 0600
    owner: user1
    attributes: "+i"
  
  - path: ~/.gnupg
    mode: 0700
    owner: user1
    attributes: "+i" 