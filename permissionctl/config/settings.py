# 全局配置
CONFIG = {
    'DSL_ROOT_DIR': '/etc/permissionctl',
    'DEFAULT_PERMISSIONS': {
        'file_mode': 0o644,
        'dir_mode': 0o755
    },
    'SUPPORTED_DSL_VERSIONS': ['1.0'],
}

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
} 