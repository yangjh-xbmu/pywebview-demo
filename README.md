# PyWebView 最小化演示项目

一个使用 PyWebView 构建的跨平台桌面应用演示项目，展示了如何使用 Python 后端和 HTML/CSS/JavaScript 前端创建现代桌面应用程序。

## 🚀 特性

- **跨平台支持**: 支持 Windows、macOS 和 Linux
- **Web 技术**: 使用熟悉的 HTML、CSS、JavaScript 构建用户界面
- **Python 后端**: 利用强大的 Python 生态系统
- **原生菜单栏**: 类似 Microsoft Word 的菜单系统，提供文件、编辑、工具和帮助菜单
- **轻量级**: 小巧快速，易于部署和分发
- **现代 UI**: 响应式设计，美观的用户界面
- **API 交互**: 前后端通信演示

## 📁 项目结构

```
pywebview-demo/
├── main.py              # 主应用程序文件（包含菜单系统）
├── static/              # 静态资源目录
│   └── index.html       # 前端界面
├── requirements.txt     # Python 依赖
├── setup.py            # 项目安装配置
├── Makefile            # 项目管理命令
├── MENU_GUIDE.md       # 菜单功能详细指南
└── README.md           # 项目说明文档
```

## 🛠️ 安装和运行

### 前置要求

- Python 3.8 或更高版本
- pip 包管理器

### 快速开始

1. **克隆或下载项目**

   ```bash
   # 如果是从 git 仓库克隆
   git clone <repository-url>
   cd pywebview-demo
   ```

2. **创建虚拟环境（推荐）**

   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **安装依赖**

   ```bash
   # 使用 pip
   pip install -r requirements.txt
   
   # 或使用 Makefile
   make install
   ```

4. **运行应用**

   ```bash
   # 直接运行
   python main.py
   
   # 或使用 Makefile
   make run
   ```

## 🎯 功能演示

应用程序包含以下功能演示：

1. **原生菜单栏**: 类似 Word 的菜单系统，包含文件、编辑、工具和帮助菜单
2. **系统信息获取**: 显示操作系统、Python 版本等信息
3. **计数器功能**: 演示前后端状态同步
4. **消息对话框**: 展示原生对话框调用
5. **目录获取**: 获取当前工作目录
6. **文件操作**: 通过菜单访问新建、打开、保存等文件操作
7. **响应式 UI**: 现代化的用户界面设计

## 🔧 开发

### 开发环境设置

```bash
# 安装开发依赖
make dev

# 代码格式化
make format

# 代码检查
make lint
```

### 项目结构说明

- **main.py**: 包含 PyWebView 应用的主要逻辑和 API 类
- **static/index.html**: 前端界面，包含 HTML、CSS 和 JavaScript
- **Api 类**: 提供前端可调用的后端方法

### 添加新功能

1. 在 `Api` 类中添加新方法
2. 在 HTML 中添加对应的 JavaScript 调用
3. 更新 UI 以展示新功能

## 📦 打包和分发

### 使用 PyInstaller 打包

```bash
# 打包为单个可执行文件
make package

# 或手动执行
pyinstaller --onefile --windowed \
    --add-data "static:static" \
    --name "PyWebView-Demo" \
    main.py
```

打包后的文件将在 `dist/` 目录中。

### 平台特定说明

#### Windows

- 推荐安装 `pythonnet` 以获得更好的性能
- 可能需要安装 Microsoft Visual C++ Redistributable

#### macOS

- 推荐安装 `pyobjc` 以获得原生体验
- 打包的应用可能需要代码签名

#### Linux

- 需要安装 GUI 框架（PyQt5/6 或 PySide2/6）
- 确保系统有必要的图形库

## 🎨 自定义

### 修改界面

编辑 `static/index.html` 文件来自定义：

- HTML 结构
- CSS 样式
- JavaScript 交互逻辑

### 添加后端功能

在 `main.py` 的 `Api` 类中添加新方法：

```python
def your_new_method(self, param):
    """你的新功能"""
    # 处理逻辑
    return result
```

然后在前端 JavaScript 中调用：

```javascript
const result = await pywebview.api.your_new_method(param);
```

## 🐛 故障排除

### 常见问题

1. **模块导入错误**
   - 确保已安装所有依赖：`pip install -r requirements.txt`
   - 检查 Python 版本是否符合要求

2. **GUI 框架问题（Linux）**
   - 安装适当的 GUI 框架：`pip install PyQt5` 或 `pip install PySide2`

3. **打包问题**
   - 确保 PyInstaller 版本兼容
   - 检查静态文件路径是否正确

4. **权限问题**
   - 在某些系统上可能需要管理员权限
   - 检查防火墙和安全软件设置

## 📚 相关资源

- [PyWebView 官方文档](https://pywebview.flowrl.com/)
- [PyWebView GitHub 仓库](https://github.com/r0x0r/pywebview)
- [PyInstaller 文档](https://pyinstaller.readthedocs.io/)

## 📄 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📞 支持

如果你在使用过程中遇到问题，可以：

- 查看 [FAQ 部分](#故障排除)
- 提交 [Issue](https://github.com/example/pywebview-demo/issues)
- 查阅 [PyWebView 官方文档](https://pywebview.flowrl.com/)

---

**享受使用 PyWebView 构建跨平台桌面应用的乐趣！** 🎉
