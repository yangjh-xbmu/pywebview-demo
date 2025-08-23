# PyWebView 菜单功能指南

## 概述

这个PyWebView演示应用现在包含了类似Microsoft Word的菜单栏功能。菜单栏提供了一个熟悉的用户界面，让用户可以通过传统的菜单方式访问应用功能。

## 菜单结构

### 📁 文件菜单
- **新建**: 创建新文件（显示确认对话框）
- **打开...**: 打开文件对话框选择文件
- **保存...**: 保存文件对话框
- **退出**: 关闭应用程序

### ✏️ 编辑菜单
- **撤销**: 撤销上一个操作
- **重做**: 重做上一个操作
- **复制**: 复制选中内容
- **粘贴**: 粘贴剪贴板内容

### 🔧 工具菜单
- **系统信息**: 显示系统详细信息
- **计数器**: 增加计数器值
- **当前目录**: 显示当前工作目录

### ❓ 帮助菜单
- **关于**: 显示应用程序信息

## 技术实现

### 菜单创建

菜单使用PyWebView的内置菜单API创建：

```python
from webview.menu import Menu, MenuAction, MenuSeparator

# 创建菜单项
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
```

### 菜单事件处理

每个菜单项都关联一个Python函数，当用户点击菜单项时会调用相应的函数：

```python
def new_file_action():
    """新建文件菜单动作"""
    active_window = webview.active_window()
    if active_window and active_window.js_api:
        active_window.js_api.new_file()
```

### 菜单集成

菜单通过`webview.start()`函数的`menu`参数集成到应用中：

```python
app_menu = create_menu()
webview.start(
    menu=app_menu,
    debug=True,
    http_server=True
)
```

## 使用方法

1. **启动应用**:
   ```bash
   source venv/bin/activate
   python main.py
   ```

2. **使用菜单**:
   - 在应用窗口顶部可以看到菜单栏
   - 点击任何菜单项来访问相应功能
   - 菜单功能与页面上的按钮功能相同

3. **测试功能**:
   - 尝试"文件 > 打开"来选择文件
   - 使用"工具 > 系统信息"查看系统详情
   - 点击"帮助 > 关于"查看应用信息

## 自定义菜单

要添加新的菜单项或修改现有菜单：

1. 在`main.py`中定义新的动作函数
2. 在`create_menu()`函数中添加新的`MenuAction`
3. 重新启动应用以查看更改

## 平台兼容性

- ✅ **macOS**: 完全支持，菜单显示在系统菜单栏中
- ✅ **Windows**: 支持，菜单显示在窗口顶部
- ✅ **Linux**: 支持，菜单显示在窗口顶部

## 注意事项

- 菜单在应用启动时创建，运行时无法动态修改
- 某些菜单项（如编辑菜单）目前仅显示演示对话框
- 文件操作菜单项会打开系统文件对话框
- 菜单快捷键支持取决于操作系统

## 扩展建议

- 添加菜单快捷键（Ctrl+N, Ctrl+O等）
- 实现真实的文件操作功能
- 添加最近文件列表
- 实现编辑菜单的实际功能
- 添加视图菜单控制界面显示选项