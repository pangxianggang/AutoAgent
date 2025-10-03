# 简单计算器项目

这个项目包含两个版本的计算器程序：

## 文件说明

- `calculator.py` - 命令行版本的计算器
- `gui_calculator.py` - 图形界面版本的计算器
- `test_calculator.py` - 测试脚本

## 功能特性

- ✅ 支持基本算术运算：加法 (+)、减法 (-)、乘法 (*)、除法 (/)
- ✅ 支持小数点运算
- ✅ 支持括号运算
- ✅ 错误处理：除零错误、无效字符、格式错误
- ✅ 安全防护：只允许数字和基本运算符

## 使用方法

### 命令行版本 (calculator.py)

```bash
python3 calculator.py
```

然后输入数学表达式，例如：
- `2 + 3` (加法)
- `10 - 4` (减法)
- `5 * 6` (乘法)
- `15 / 3` (除法)
- `(2 + 3) * 4` (括号运算)

输入 `quit` 或 `exit` 退出程序。

### 图形界面版本 (gui_calculator.py)

**注意：需要安装tkinter模块**

```bash
# Ubuntu/Debian系统安装tkinter
sudo apt-get install python3-tk

# 其他系统可能需要安装相应的tkinter包
python3 gui_calculator.py
```

点击按钮输入表达式，点击 `=` 计算结果，点击 `C` 清空。

如果tkinter不可用，可以使用命令行版本。

## 测试

运行测试脚本验证功能：

```bash
python3 test_calculator.py
```

## 注意事项

- 只支持基本的算术运算，不支持高级数学函数
- 输入中不能包含字母或其他特殊字符
- 除数不能为零

享受计算的乐趣！ 🧮