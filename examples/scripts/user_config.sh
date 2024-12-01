#!/bin/bash

# User configuration examples
# 普通用户配置示例

# Personal directory permissions
echo "=== Personal Directory Configuration ==="
permissionctl register ~/.ssh personal --mode 0700
permissionctl register ~/.ssh/config personal --mode 0600 --attributes "+i"
permissionctl register ~/.gnupg personal --mode 0700 --attributes "+i"

# Project directory permissions
echo "=== Project Directory Configuration ==="
permissionctl register ~/projects/webapp project --mode 0755
permissionctl register ~/projects/webapp/config project --mode 0700
permissionctl register ~/projects/webapp/logs project --mode 0755 --attributes "+a"

# Apply all configurations
permissionctl apply 