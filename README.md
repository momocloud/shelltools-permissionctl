# permissionctl 项目

本项目使用 cursor协助生成。

## 项目结构

```
permissionctl/                 
├── setup.py
├── README.md
├── requirements.txt
├── install.sh                  # 安装shell脚本
├── MANIFEST.in                 # 打包配置文件
├── permissionctl/ 
│   ├── __init__.py
│   ├── cli.py                 # 命令行接口
│   ├── core/                  # 核心功能模块
│   │   ├── dsl_parser.py     # DSL解析器
│   │   └── permission_manager.py  # 权限管理器
│   ├── utils/
│   │   ├── logger.py         # 日志管理
│   │   └── file_utils.py 
│   └── config/
│       └── settings.py 
└── examples/                  # 示例目录
    ├── README.md             # 示例说明文档
    └── scripts/              # 示例脚本
        ├── README.md         # 脚本说明文档
        ├── basic_usage.sh    # 基础使用示例
        ├── user_config.sh    # 用户配置示例
        ├── team_shared.sh    # 团队共享示例
        ├── system_security.sh # 系统安全示例
        └── batch_operations.sh # 批量操作示例

安装后的系统目录结构：
/etc/permissionctl/           # 配置根目录
└── dsl/                      # DSL文件目录
    ├── root/                 # root用户的DSL目录 (700)
    │   └── system.dsl        # DSL文件 (600)
    └── user1/                # 普通用户的DSL目录 (700)
        └── personal.dsl      # DSL文件 (600)
```

## 文件说明

### 核心模块
- `cli.py`: 命令行接口实现，处理用户命令
- `dsl_parser.py`: DSL文件解析器，处理DSL文件的读写和验证
- `permission_manager.py`: 权限管理器，实现权限的注册和应用
- `logger.py`: 日志管理，提供统一的日志输出
- `file_utils.py`: 文件操作工具，处理文件属性和权限

### 配置文件
- `settings.py`: 全局配置，包含基础路径和默认设置
- `install.sh`: 安装脚本，创建必要的目录结构
- `MANIFEST.in`: 确保所有必要文件被打包

### 示例文件
- `basic_usage.sh`: 基础使用示例，包括初始化和基本操作
- `user_config.sh`: 用户配置示例，展示普通用户的使用方式
- `team_shared.sh`: 团队共享示例，展示共享目录的权限管理
- `system_security.sh`: 系统安全示例，展示关键系统文件的权限配置
- `batch_operations.sh`: 批量操作示例，展示如何批量处理权限

## 简介

通过 DSL 和 python3 脚本实现声明式的权限管理。项目通过在`/etc/permissionctl/`目录下创建用户的子目录在子目录下创建权限文件DSL来定义权限，然后 python3 解析 DSL 文件实现权限管理。

## 原理

permissionctl 通过提供接口，用户调用接口将文件的权限注册到对应的dsl文件中。permissionctl 同时提供接口，根据 dsl 文件刷新注册的所有文件的权限，从而实现统一的文件管理。

## 使用示例

详细的使用示例请参考 [examples](./examples) 目录。

### Root用户示例

```bash
# 为root和user1用户创建DSL目录
sudo permissionctl init root
sudo permissionctl init user1

# 设置系统关键文件为不可变
sudo permissionctl register /etc/passwd system --mode 0644 --attributes "+i"

# 设置Web服务器目录权限
sudo permissionctl register /var/www/html web --mode 0755 --owner www-data

# 应用配置
sudo permissionctl apply system
sudo permissionctl apply web

# 列出所有DSL文件
permissionctl list

# 删除DSL文件
permissionctl delete web
```

### 普通用户示例

```bash
# 用户为user1

# 设置个人文件权限（生成/etc/permissionctl/dsl/user1/personal.dsl文件）
permissionctl register ~/important_docs personal --mode 0700

# 设置共享目录权限（生成/etc/permissionctl/dsl/user1/shared.dsl文件）
permissionctl register /srv/shared/project shared --mode 0775 --group developers

# 应用配置
permissionctl apply personal
permissionctl apply shared

# 列出所有DSL文件
permissionctl list

# 删除DSL文件
permissionctl delete shared
```
