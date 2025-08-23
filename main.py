#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyWebView 最小化演示项目
一个简单的桌面应用，使用 PyWebView 显示 HTML 内容
"""

from pathlib import Path
import sys

import webview
from webview.menu import Menu, MenuAction, MenuSeparator


class Api:
    """
    后端 API 类，提供前端可调用的方法
    """

    def __init__(self):
        self.counter = 0

    def get_system_info(self):
        """获取系统信息"""
        import platform
        return {
            'platform': platform.system(),
            'version': platform.version(),
            'architecture': platform.architecture()[0],
            'python_version': platform.python_version(),
            'machine': platform.machine()
        }

    def increment_counter(self):
        """计数器递增"""
        self.counter += 1
        return self.counter

    def get_counter(self):
        """获取当前计数"""
        return self.counter

    def show_message(self, message):
        """显示消息对话框"""
        webview.windows[0].create_confirmation_dialog('消息', message)
        return f'已显示消息: {message}'

    def get_current_directory(self):
        """获取当前工作目录"""
        return str(Path.cwd())

    def new_file(self):
        """新建文件"""
        webview.windows[0].create_confirmation_dialog('新建', '创建新文件功能')
        return '新建文件'

    def open_file(self):
        """打开文件"""
        result = webview.windows[0].create_file_dialog(
            webview.OPEN_DIALOG, allow_multiple=False
        )
        if result:
            return f'选择的文件: {result[0]}'
        return '未选择文件'

    def save_file(self):
        """保存文件"""
        result = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        if result:
            return f'保存到: {result}'
        return '取消保存'

    def about_app(self):
        """关于应用"""
        webview.windows[0].create_confirmation_dialog(
            '关于 PyWebView Demo', 
            'PyWebView 最小化演示应用\n版本: 1.0.0\n基于 PyWebView 构建'
        )
        return '显示关于信息'

    def exit_app(self):
        """退出应用"""
        webview.windows[0].destroy()
        return '退出应用'


def get_html_path():
    """获取 HTML 文件路径"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的可执行文件
        base_path = sys._MEIPASS
    else:
        # 开发环境
        base_path = Path(__file__).parent

    return Path(base_path) / 'static' / 'index.html'


# 菜单动作函数
def new_file_action():
    """新建文件菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.new_file()


def open_file_action():
    """打开文件菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.open_file()


def save_file_action():
    """保存文件菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.save_file()


def exit_app_action():
    """退出应用菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.exit_app()


def undo_action():
    """撤销菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.create_confirmation_dialog('编辑', '撤销功能')


def redo_action():
    """重做菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.create_confirmation_dialog('编辑', '重做功能')


def copy_action():
    """复制菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.create_confirmation_dialog('编辑', '复制功能')


def paste_action():
    """粘贴菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.create_confirmation_dialog('编辑', '粘贴功能')


def system_info_action():
    """系统信息菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.evaluate_js('getSystemInfo()')


def counter_action():
    """计数器菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.evaluate_js('incrementCounter()')


def current_dir_action():
    """当前目录菜单动作"""
    active_window = webview.active_window()
    if active_window:
        active_window.evaluate_js('getCurrentDirectory()')


def about_action():
    """关于菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.about_app()


def create_menu():
    """创建应用菜单"""
    # 创建文件菜单
    file_menu = Menu(
        '文件',
        [
            MenuAction('新建', new_file_action),
            MenuAction('打开...', open_file_action),
            MenuSeparator(),
            MenuAction('保存...', save_file_action),
            MenuSeparator(),
            MenuAction('退出', exit_app_action)
        ]
    )
    
    # 创建编辑菜单
    edit_menu = Menu(
        '编辑',
        [
            MenuAction('撤销', undo_action),
            MenuAction('重做', redo_action),
            MenuSeparator(),
            MenuAction('复制', copy_action),
            MenuAction('粘贴', paste_action)
        ]
    )
    
    # 创建工具菜单
    tools_menu = Menu(
        '工具',
        [
            MenuAction('系统信息', system_info_action),
            MenuAction('计数器', counter_action),
            MenuAction('当前目录', current_dir_action)
        ]
    )
    
    # 创建帮助菜单
    help_menu = Menu(
        '帮助',
        [
            MenuAction('关于', about_action)
        ]
    )
    
    return [file_menu, edit_menu, tools_menu, help_menu]


def main():
    """主函数"""
    # 创建 API 实例
    api = Api()

    # 获取 HTML 文件路径
    html_path = get_html_path()

    # 检查 HTML 文件是否存在
    if not html_path.exists():
        print(f"错误: 找不到 HTML 文件: {html_path}")
        # 如果找不到文件，使用内联 HTML
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>PyWebView Demo</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>PyWebView 演示</h1>
            <p>HTML 文件未找到，使用内联内容。</p>
            <button onclick="pywebview.api.show_message(
                'Hello from PyWebView!')">测试消息</button>
        </body>
        </html>
        """
        url = html_content
    else:
        url = str(html_path)

    # 创建菜单
    app_menu = create_menu()
    
    # 创建窗口
    webview.create_window(
        title='PyWebView 最小化演示',
        url=url,
        js_api=api,
        width=800,
        height=600,
        min_size=(400, 300),
        resizable=True,
        shadow=True,
        on_top=False,
        maximized=False,
        minimized=False
    )

    # 启动应用，传入菜单
    webview.start(
        menu=app_menu,
        debug=True,  # 开发模式下启用调试
        http_server=True  # 启用内置 HTTP 服务器
    )


if __name__ == '__main__':
    main()
