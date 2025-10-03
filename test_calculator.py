#!/usr/bin/env python3
"""
测试计算器功能
"""

from calculator import calculate

def test_calculator():
    test_cases = [
        ("2 + 3", "结果：5"),
        ("10 - 4", "结果：6"),
        ("5 * 6", "结果：30"),
        ("15 / 3", "结果：5.0"),
        ("2.5 + 3.7", "结果：6.2"),
        ("10 / 0", "错误：除数不能为零"),
        ("2 + abc", "错误：只允许数字和运算符 (+, -, *, /)"),
        ("(2 + 3) * 4", "结果：20"),
        ("", "错误：表达式格式不正确"),
    ]

    print("测试计算器功能：")
    print("=" * 50)

    for expression, expected in test_cases:
        result = calculate(expression)
        status = "✓" if result == expected else "✗"
        print(f"{status} 测试：{expression}")
        print(f"  期望：{expected}")
        print(f"  实际：{result}")
        print()

if __name__ == "__main__":
    test_calculator()