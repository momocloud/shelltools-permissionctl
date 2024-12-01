# permissionctl 使用示例脚本

本目录包含了各种 permissionctl 的使用场景示例脚本。

## 脚本说明

- `basic_usage.sh`: 基础使用示例，包括初始化和Web服务器配置
- `user_config.sh`: 普通用户配置示例，包括个人目录和项目目录权限设置
- `team_shared.sh`: 团队共享目录配置示例
- `system_security.sh`: 系统安全配置示例，包括关键系统文件和日志文件的权限设置
- `batch_operations.sh`: 批量操作示例，展示如何批量处理多个文件和目录

## 使用方法

1. 确保已安装 permissionctl
2. 给脚本添加执行权限：
   ```bash
   chmod +x *.sh
   ```
3. 根据需要执行相应的示例脚本

## 注意事项

1. 某些脚本需要 root 权限才能执行
2. 请根据实际环境修改脚本中的路径和用户名
3. 建议先查看脚本内容再执行
4. 这些脚本仅作为示例，请根据实际需求调整 