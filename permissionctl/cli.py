import click
from permissionctl.core.permission_manager import PermissionManager
from permissionctl.utils.logger import logger
import sys
import os

@click.group()
def main():
    """permissionctl - 基于DSL的权限管理工具"""
    pass

@main.command()
@click.argument('username')
def init(username):
    """初始化用户的DSL目录（需要root权限）"""
    if os.geteuid() != 0:
        logger.error("Root privileges required")
        sys.exit(1)
        
    try:
        manager = PermissionManager()
        manager.init_user_dsl_dir(username)
    except Exception as e:
        logger.error(str(e))
        sys.exit(1)

@main.command()
@click.argument('file_path')
@click.argument('dsl_name')
@click.option('--mode', '-m', help='文件权限模式，例如: 0644')
@click.option('--owner', '-o', help='文件所有者')
@click.option('--group', '-g', help='文件所属组')
@click.option('--attributes', '-a', help='特殊权限属性，例如: +i,+t')
def register(file_path, dsl_name, mode=None, owner=None, group=None, attributes=None):
    """将文件权限注册到指定的DSL文件中"""
    try:
        manager = PermissionManager()
        manager.register_permission(file_path, dsl_name, mode, owner, group, attributes)
    except Exception as e:
        logger.error(str(e))
        sys.exit(1)

@main.command()
@click.argument('dsl_name', required=False)
def apply(dsl_name=None):
    """应用DSL文件中定义的权限配置。
    如果不指定dsl_name，则应用用户所有的DSL配置"""
    try:
        manager = PermissionManager()
        manager.apply_permissions(dsl_name)
        msg = f"Successfully applied permission configurations for {dsl_name}" if dsl_name else "Successfully applied all DSL permission configurations"
        click.echo(msg)
    except Exception as e:
        click.echo(f"Failed to apply permissions: {str(e)}", err=True)

@main.command()
@click.argument('dsl_name')
def delete(dsl_name):
    """删除指定的DSL文件"""
    try:
        manager = PermissionManager()
        manager.delete_dsl(dsl_name)
        logger.success(f"Successfully deleted DSL file", dsl_name)
    except Exception as e:
        logger.error(str(e))
        sys.exit(1)

@main.command()
def list():
    """列出当前用户的所有DSL文件"""
    try:
        manager = PermissionManager()
        dsls = manager.list_dsls()
        if not dsls:
            logger.info("No DSL files found")
            return
            
        logger.info("Available DSL files:")
        for dsl in dsls:
            name = dsl['name']
            count = dsl['rules_count']
            logger.info(f"  {name} ({count} rules)")
    except Exception as e:
        logger.error(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main() 