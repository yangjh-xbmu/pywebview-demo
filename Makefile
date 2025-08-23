# PyWebView 最小化演示项目 Makefile

.PHONY: help install dev run clean build package test lint format

# 默认目标
help:
	@echo "PyWebView 最小化演示项目"
	@echo "可用命令:"
	@echo "  install    - 安装项目依赖"
	@echo "  dev        - 安装开发依赖"
	@echo "  run        - 运行应用"
	@echo "  clean      - 清理构建文件"
	@echo "  build      - 构建项目"
	@echo "  package    - 打包为可执行文件"
	@echo "  test       - 运行测试"
	@echo "  lint       - 代码检查"
	@echo "  format     - 代码格式化"

# 安装依赖
install:
	@echo "安装项目依赖..."
	pip install -r requirements.txt

# 安装开发依赖
dev: install
	@echo "安装开发依赖..."
	pip install flake8 black pyinstaller

# 运行应用
run:
	@echo "启动 PyWebView 应用..."
	python main.py

# 清理构建文件
clean:
	@echo "清理构建文件..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

# 构建项目
build: clean
	@echo "构建项目..."
	python setup.py build

# 打包为可执行文件
package: clean
	@echo "打包为可执行文件..."
	pyinstaller --onefile --windowed \
		--add-data "static:static" \
		--name "PyWebView-Demo" \
		main.py

# 运行测试
test:
	@echo "运行测试..."
	@echo "暂无测试用例"

# 代码检查
lint:
	@echo "代码检查..."
	flake8 main.py setup.py --max-line-length=88

# 代码格式化
format:
	@echo "代码格式化..."
	black main.py setup.py --line-length=88