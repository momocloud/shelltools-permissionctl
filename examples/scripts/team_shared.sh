#!/bin/bash

# Team shared directory configuration examples
# 团队共享目录配置示例

# Shared project directory setup
echo "=== Team Shared Directory Configuration ==="
permissionctl register /srv/shared/project shared --mode 0775 --group developers
permissionctl register /srv/shared/project/build shared --mode 0775 --group developers
permissionctl register /srv/shared/project/config shared --mode 0770 --group developers

# Apply shared directory configuration
permissionctl apply shared 