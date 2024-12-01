#!/bin/bash

# Basic usage examples for permissionctl
# 基础使用示例

# Root initialization
echo "=== Root User Operations ==="
# Initialize DSL directories for multiple users
for user in alice bob charlie; do
    sudo permissionctl init $user
done

# Web server configuration
echo "=== Web Server Configuration ==="
sudo permissionctl register /etc/nginx/nginx.conf web --mode 0644 --owner root --group root --attributes "+i"
sudo permissionctl register /var/www/html web --mode 0755 --owner www-data --group www-data
sudo permissionctl register /var/log/nginx web --mode 0755 --owner www-data --group adm --attributes "+a"
sudo permissionctl apply web

# List DSL files
echo "=== Listing DSL Files ==="
permissionctl list

# List again to see the new DSL
permissionctl list

# Apply configurations
echo "=== Applying Configurations ==="
permissionctl apply web

# Delete web configuration if needed
permissionctl delete web 
