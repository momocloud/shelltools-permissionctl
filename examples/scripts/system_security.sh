#!/bin/bash

# System security configuration examples
# 系统安全配置示例

# Critical system files
echo "=== System Security Configuration ==="
sudo permissionctl register /etc/passwd secure --mode 0644 --owner root --group root --attributes "+i"
sudo permissionctl register /etc/shadow secure --mode 0600 --owner root --group shadow --attributes "+i"
sudo permissionctl register /etc/sudoers secure --mode 0440 --owner root --group root --attributes "+i"

# Secure log files
sudo permissionctl register /var/log/auth.log logs --mode 0640 --owner syslog --group adm --attributes "+a"
sudo permissionctl register /var/log/secure logs --mode 0600 --owner root --group root --attributes "+a,+i"

# Apply security configurations
sudo permissionctl apply secure
sudo permissionctl apply logs 