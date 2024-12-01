from setuptools import setup, find_packages
import os

# 获取当前目录
here = os.path.abspath(os.path.dirname(__file__))

# 读取README
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="permissionctl",
    version="0.1.0",
    packages=find_packages(include=['permissionctl', 'permissionctl.*']),
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=5.1"
    ],
    entry_points={
        'console_scripts': [
            'permissionctl=permissionctl.cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="基于DSL的声明式权限管理工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
) 