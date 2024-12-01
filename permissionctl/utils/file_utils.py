import os
import stat
import subprocess

def get_file_permissions(path):
    """获取文件的权限信息"""
    st = os.stat(path)
    return {
        'mode': stat.S_IMODE(st.st_mode),
        'uid': st.st_uid,
        'gid': st.st_gid
    }

def get_file_attributes(path):
    """获取文件的特殊属性"""
    try:
        result = subprocess.run(['lsattr', path], capture_output=True, text=True)
        if result.returncode == 0:
            # lsattr输出格式例如: "----i--------e-- /path/to/file"
            attrs = result.stdout.split()[0]
            return _parse_attributes(attrs)
    except Exception:
        pass
    return []

def set_file_attributes(path, attributes):
    """设置文件的特殊属性"""
    if not attributes:
        return
        
    attrs = attributes.split(',')
    for attr in attrs:
        if not attr.startswith('+') and not attr.startswith('-'):
            raise ValueError(f"Invalid attribute format: {attr}")
        
        # 对于每个属性执行chattr命令
        try:
            subprocess.run(['chattr', attr, path], check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to set file attributes: {str(e)}")

def _parse_attributes(attr_string):
    """解析lsattr输出的属性字符串"""
    attr_map = {
        'i': 'immutable',
        'a': 'append-only',
        's': 'secure-deletion',
        't': 'no-tail-merging',
        'T': 'top-of-directory-hierarchy',
        'c': 'compressed',
        'u': 'undeletable',
        'j': 'journal-data',
        'd': 'no-dump',
        'e': 'extent-format',
    }
    
    attrs = []
    for i, char in enumerate(attr_string):
        if char != '-':
            attr = attr_map.get(char)
            if attr:
                attrs.append(attr)
    return attrs

def validate_path(path):
    """验证路径是否合法且存在"""
    if not os.path.exists(path):
        raise ValueError(f"Path does not exist: {path}")
    return os.path.abspath(path) 