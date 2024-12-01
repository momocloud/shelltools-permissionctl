#!/bin/bash

# 检查是否为root用户
if [ "$EUID" -ne 0 ]; then 
    echo "请使用root权限运行此脚本"
    exit 1
fi

# 清理旧的安装（如果存在）
pip3 uninstall -y permissionctl 2>/dev/null || true

# 构建并安装Python包
pip3 install --no-cache-dir .

# 创建配置目录
mkdir -p /etc/permissionctl/dsl
chmod 755 /etc/permissionctl
chmod 755 /etc/permissionctl/dsl

# 确保命令对所有用户可用
chmod 755 /usr/bin/permissionctl 2>/dev/null || true

echo "permissionctl 安装完成！"
echo "现在您可以使用 'sudo permissionctl init <username>' 来初始化用户的DSL目录" 