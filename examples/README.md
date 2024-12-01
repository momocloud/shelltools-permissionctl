# permissionctl 使用示例

本目录包含了 permissionctl 的各种使用示例，分为 root 用户和普通用户两类场景。

## Root 用户示例

root 用户可以管理系统级的权限和特殊属性，示例文件位于 `root/` 目录：

```bash
# 应用系统关键文件配置
sudo permissionctl apply system

# 应用Web服务器配置
sudo permissionctl apply web

# 应用数据库配置
sudo permissionctl apply database

# 应用所有配置
sudo permissionctl apply
```

## 普通用户示例

普通用户可以管理自己有权限的文件和目录，示例文件位于 `user/` 目录：

```bash
# 应用个人文件配置
permissionctl apply personal

# 应用项目配置
permissionctl apply project

# 应用共享目录配置
permissionctl apply shared

# 应用所有配置
permissionctl apply
```

## 注意事项

1. root用户可以管理系统级的权限和特殊属性
2. 普通用户只能管理自己有权限的文件和目录
3. 设置特殊属性（如+i）通常需要root权限
4. 用户只能在自己的DSL目录下创建和管理DSL文件 