import sys
import logging
from enum import Enum
from typing import Optional

class Color(Enum):
    """终端颜色代码"""
    HEADER = '\033[95m'
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class ColoredFormatter(logging.Formatter):
    """彩色日志格式化器"""
    
    def format(self, record):
        """格式化日志记录"""
        # 根据日志级别选择颜色
        if record.levelno >= logging.ERROR:
            color = Color.ERROR
        elif record.levelno >= logging.WARNING:
            color = Color.WARNING
        elif record.levelno == 25:  # SUCCESS level
            color = Color.SUCCESS
        else:
            color = Color.INFO

        # 添加路径信息（如果存在）
        msg = record.getMessage()
        if hasattr(record, 'path') and record.path:
            msg = f"{msg} [{record.path}]"
            
        return f"{color.value}{msg}{Color.RESET.value}"

class PermissionLogger:
    """权限管理日志器"""
    
    def __init__(self):
        # 添加SUCCESS日志级别
        logging.addLevelName(25, "SUCCESS")
        
        self.logger = logging.getLogger('permissionctl')
        self.logger.setLevel(logging.INFO)
        
        # 清除已存在的处理器
        self.logger.handlers = []
        
        # 添加标准输出处理器
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(ColoredFormatter())
        stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
        self.logger.addHandler(stdout_handler)
        
        # 添加标准错误处理器
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setFormatter(ColoredFormatter())
        stderr_handler.addFilter(lambda record: record.levelno > logging.WARNING)
        self.logger.addHandler(stderr_handler)
    
    def _log(self, msg: str, level: int, path: Optional[str] = None):
        """统一的日志处理"""
        extra = {'path': path} if path else None
        self.logger.log(level, msg, extra=extra)
    
    def info(self, msg: str, path: Optional[str] = None):
        """信息日志"""
        self._log(msg, logging.INFO, path)
    
    def success(self, msg: str, path: Optional[str] = None):
        """成功日志"""
        self._log(msg, 25, path)  # 25 is SUCCESS level
    
    def warning(self, msg: str, path: Optional[str] = None):
        """警告日志"""
        self._log(msg, logging.WARNING, path)
    
    def error(self, msg: str, path: Optional[str] = None):
        """错误日志"""
        self._log(msg, logging.ERROR, path)

# 创建全局日志器实例
logger = PermissionLogger() 