import os
import pwd
import grp
from .dsl_parser import DSLParser
from permissionctl.utils.logger import logger

class PermissionManager:
    def __init__(self):
        self.parser = DSLParser()
        self.base_path = "/etc/permissionctl/dsl"
        self.current_user = pwd.getpwuid(os.getuid()).pw_name
    
    def init_user_dsl_dir(self, username):
        """初始化用户的DSL目录
        
        Args:
            username: 要初始化的用户名
        """
        try:
            # 验证用户是否存在
            try:
                pwd.getpwnam(username)
            except KeyError:
                raise ValueError(f"User does not exist: {username}")
            
            # 创建用户DSL目录
            user_dir = os.path.join(self.base_path, username)
            
            if os.path.exists(user_dir):
                logger.warning(f"User directory already exists", user_dir)
                return
                
            # 创建目录结构
            os.makedirs(user_dir, mode=0o700)
            logger.info(f"Created user directory", user_dir)
            
            # 修改目录所有权
            uid = self._get_uid(username)
            gid = self._get_gid(username)
            os.chown(user_dir, uid, gid)
            logger.info(f"Set directory owner: {username}", user_dir)
            
            logger.success(f"Successfully initialized user DSL directory", user_dir)
            
        except Exception as e:
            logger.error(f"Failed to initialize user directory: {str(e)}")
            raise
    
    def register_permission(self, file_path, dsl_name, mode=None, owner=None, group=None, attributes=None):
        """注册文件权限到指定的DSL文件"""
        try:
            # 验证用户只能访问自己的DSL文件
            user_dir = os.path.join(self.base_path, self.current_user)
            dsl_file = os.path.join(user_dir, f"{dsl_name}.dsl")
            
            if not os.path.exists(user_dir):
                logger.error(f"User directory does not exist: {user_dir}")
                raise ValueError(f"User directory does not exist: {user_dir}")
                
            # 读取现有的DSL文件内容或创建新的
            permissions = {}
            if os.path.exists(dsl_file):
                permissions = self.parser.parse_dsl_file(dsl_file)
            else:
                permissions = {'version': '1.0', 'permissions': []}
                
            # 更新或添加新的权限规则
            # 处理路径中的波浪号展开
            expanded_path = os.path.expanduser(file_path)
            # 确保路径是绝对路径且规范化
            abs_path = os.path.abspath(expanded_path)
            
            new_rule = {
                'path': abs_path
            }
            if mode:
                new_rule['mode'] = mode
            if owner:
                new_rule['owner'] = owner
            if group:
                new_rule['group'] = group
            if attributes:
                new_rule['attributes'] = attributes
                
            # 检查是否已存在该路径的规则
            rules = permissions.get('permissions', [])
            for i, rule in enumerate(rules):
                if rule['path'] == new_rule['path']:
                    rules[i].update(new_rule)
                    break
            else:
                rules.append(new_rule)
                
            permissions['permissions'] = rules
            
            # 保存更新后的DSL文件
            self.parser.save_dsl_file(dsl_file, permissions)
            logger.success(f"Successfully registered permission", file_path)
            
        except Exception as e:
            logger.error(f"Failed to register permission: {str(e)}", file_path)
            raise
    
    def apply_permissions(self, dsl_name=None):
        """应用DSL文件中定义的权限"""
        user_dir = os.path.join(self.base_path, self.current_user)
        
        if dsl_name:
            # 应用指定的DSL文件
            dsl_file = os.path.join(user_dir, f"{dsl_name}.dsl")
            if not os.path.exists(dsl_file):
                raise ValueError(f"DSL file does not exist: {dsl_name}")
            self._apply_dsl_file(dsl_file)
        else:
            # 应用所有DSL文件
            for filename in os.listdir(user_dir):
                if filename.endswith('.dsl'):
                    self._apply_dsl_file(os.path.join(user_dir, filename))
    
    def _apply_dsl_file(self, dsl_file):
        """应用单个DSL文件的权限规则"""
        permissions = self.parser.parse_dsl_file(dsl_file)
        self._apply_permission_rules(permissions)
    
    def _apply_permission_rules(self, rules):
        """应用权限规则"""
        for rule in rules.get('permissions', []):
            path = rule.get('path')
            if not path or not os.path.exists(path):
                logger.warning(f"Skipping non-existent path", path)
                continue
                
            try:
                if 'mode' in rule:
                    os.chmod(path, int(str(rule['mode']), 8))
                    logger.info(f"Set permission mode: {rule['mode']}", path)
                    
                if 'owner' in rule or 'group' in rule:
                    uid = self._get_uid(rule.get('owner')) if 'owner' in rule else -1
                    gid = self._get_gid(rule.get('group')) if 'group' in rule else -1
                    os.chown(path, uid, gid)
                    logger.info(f"Set owner/group: {rule.get('owner', '-')}/{rule.get('group', '-')}", path)
                    
                if 'attributes' in rule:
                    from permissionctl.utils.file_utils import set_file_attributes
                    set_file_attributes(path, rule['attributes'])
                    logger.info(f"Set special attributes: {rule['attributes']}", path)
                    
            except Exception as e:
                logger.error(f"Failed to apply permission: {str(e)}", path)
    
    def _get_uid(self, username):
        """获取用户ID"""
        return pwd.getpwnam(username).pw_uid if username else -1
    
    def _get_gid(self, username):
        """获取用户组ID"""
        return pwd.getpwnam(username).pw_gid if username else -1
    
    def delete_dsl(self, dsl_name):
        """删除指定的DSL文件
        
        Args:
            dsl_name: DSL文件名（不含.dsl后缀）
        """
        try:
            # 验证用户只能访问自己的DSL文件
            user_dir = os.path.join(self.base_path, self.current_user)
            dsl_file = os.path.join(user_dir, f"{dsl_name}.dsl")
            
            if not os.path.exists(user_dir):
                logger.error(f"User directory does not exist: {user_dir}")
                raise ValueError(f"User directory does not exist: {user_dir}")
            
            if not os.path.exists(dsl_file):
                logger.error(f"DSL file does not exist: {dsl_name}")
                raise ValueError(f"DSL file does not exist: {dsl_name}")
            
            # 删除DSL文件
            os.remove(dsl_file)
            logger.info(f"Deleted DSL file", dsl_file)
            
        except Exception as e:
            logger.error(f"Failed to delete DSL file: {str(e)}", dsl_name)
            raise
    
    def list_dsls(self):
        """列出当前用户的所有DSL文件
        
        Returns:
            list: 包含DSL文件信息的列表，每个元素是一个字典，包含name和rules_count
        """
        try:
            user_dir = os.path.join(self.base_path, self.current_user)
            
            if not os.path.exists(user_dir):
                logger.error(f"User directory does not exist: {user_dir}")
                raise ValueError(f"User directory does not exist: {user_dir}")
            
            dsls = []
            for filename in os.listdir(user_dir):
                if filename.endswith('.dsl'):
                    dsl_path = os.path.join(user_dir, filename)
                    try:
                        # 读取DSL文件内容以获取规则数量
                        permissions = self.parser.parse_dsl_file(dsl_path)
                        rules_count = len(permissions.get('permissions', []))
                        
                        dsls.append({
                            'name': filename[:-4],  # 移除.dsl后缀
                            'rules_count': rules_count
                        })
                    except Exception as e:
                        logger.warning(f"Failed to parse DSL file: {filename}", str(e))
                        continue
                        
            return sorted(dsls, key=lambda x: x['name'])
            
        except Exception as e:
            logger.error(f"Failed to list DSL files: {str(e)}")
            raise
    