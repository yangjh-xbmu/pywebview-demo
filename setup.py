#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyWebView 最小化演示项目安装配置
"""

from setuptools import setup, find_packages

# 读取 README 文件
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取 requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh 
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="pywebview-demo",
    version="1.0.0",
    author="PyWebView Demo",
    author_email="demo@example.com",
    description="PyWebView 最小化演示项目",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/pywebview-demo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Desktop Environment",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "": ["static/*.html", "static/*.css", "static/*.js"],
    },
    entry_points={
        "console_scripts": [
            "pywebview-demo=main:main",
        ],
    },
)