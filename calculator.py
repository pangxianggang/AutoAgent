#!/usr/bin/env python3
"""
简单计算器程序
支持基本的算术运算：加法、减法、乘法、除法
"""

import sys

def calculate(expression):
    """
    安全的计算器函数，使用eval进行计算
    只允许基本的算术运算
    """
    try:
        # 只允许数字和基本运算符
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            return "错误：只允许数字和运算符 (+, -, *, /)"

        # 计算结果
        result = eval(expression)

        # 检查除零错误
        if isinstance(result, float) and result == float('inf'):
            return "错误：除数不能为零"

        return f"结果：{result}"

    except ZeroDivisionError:
        return "错误：除数不能为零"
    except SyntaxError:
        return "错误：表达式格式不正确"
    except Exception as e:
        return f"错误：{str(e)}"

def main():
    print("欢迎使用简单计算器！")
    print("支持运算：+, -, *, /")
    print("输入 'quit' 或 'exit' 退出")
    print("=" * 40)

    while True:
        try:
            expression = input("请输入计算表达式：").strip()

            if expression.lower() in ['quit', 'exit', 'q']:
                print("感谢使用，再见！")
                break

            if not expression:
                continue

            result = calculate(expression)
            print(result)

        except KeyboardInterrupt:
            print("\n感谢使用，再见！")
            break
        except EOFError:
            print("\n感谢使用，再见！")
            break

if __name__ == "__main__":
    main()