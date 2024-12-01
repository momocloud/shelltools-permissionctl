import yaml
import os

class DSLParser:
    def parse_dsl_file(self, dsl_path):
        """解析DSL文件"""
        try:
            with open(dsl_path, 'r') as f:
                permissions = yaml.safe_load(f)
            return self._validate_and_process(permissions)
        except Exception as e:
            raise Exception(f"DSL parsing error: {str(e)}")
    
    def save_dsl_file(self, dsl_path, permissions):
        """保存DSL文件"""
        try:
            # 保存文件内容
            with open(dsl_path, 'w') as f:
                yaml.dump(permissions, f, default_flow_style=False)
                
            # 设置DSL文件权限为600
            os.chmod(dsl_path, 0o600)
                
        except Exception as e:
            raise Exception(f"Failed to save DSL file: {str(e)}")
    
    def _validate_and_process(self, permissions):
        """验证并处理解析后的权限配置"""
        if not isinstance(permissions, dict):
            raise ValueError("Invalid DSL format")
        if 'version' not in permissions:
            permissions['version'] = '1.0'
        if 'permissions' not in permissions:
            permissions['permissions'] = []
        return permissions 