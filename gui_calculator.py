#!/usr/bin/env python3
"""
GUI计算器程序
使用tkinter创建图形界面
"""

import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("简单计算器")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # 创建显示区域
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        display_frame = ttk.Frame(root, padding="10")
        display_frame.pack(fill="x")

        self.display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 20),
            justify="right",
            state="readonly"
        )
        self.display.pack(fill="x", pady=(0, 10))

        # 创建按钮布局
        button_frame = ttk.Frame(root, padding="10")
        button_frame.pack(fill="both", expand=True)

        # 定义按钮布局
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '(', ')', '']
        ]

        # 创建按钮
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text:  # 跳过空按钮
                    btn = ttk.Button(
                        button_frame,
                        text=btn_text,
                        command=lambda t=btn_text: self.button_click(t)
                    )

                    # 设置按钮样式
                    if btn_text == '=':
                        btn.config(style="Accent.TButton")
                    elif btn_text in ['+', '-', '*', '/']:
                        btn.config(style="Operator.TButton")

                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        # 配置网格权重
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # 4列
            button_frame.grid_columnconfigure(j, weight=1)

        # 创建样式
        style = ttk.Style()
        style.configure("Operator.TButton", font=("Arial", 12, "bold"))
        style.configure("Accent.TButton", font=("Arial", 12, "bold"))

        # 当前输入
        self.current_input = ""
        self.last_result = "0"

    def button_click(self, value):
        if value == '=':
            self.calculate()
        elif value == 'C':
            self.clear()
        else:
            self.append_to_input(value)

    def append_to_input(self, value):
        if self.display_var.get() == "0" or self.display_var.get() == self.last_result:
            self.current_input = value
        else:
            self.current_input += value

        self.display_var.set(self.current_input)

    def calculate(self):
        expression = self.current_input

        try:
            # 只允许数字和基本运算符
            allowed_chars = set('0123456789+-*/.()')
            if not all(c in allowed_chars for c in expression):
                messagebox.showerror("错误", "只允许数字和运算符 (+, -, *, /)")
                return

            # 计算结果
            result = eval(expression)

            # 检查除零错误
            if isinstance(result, float) and result == float('inf'):
                messagebox.showerror("错误", "除数不能为零")
                return

            self.display_var.set(str(result))
            self.last_result = str(result)
            self.current_input = str(result)

        except ZeroDivisionError:
            messagebox.showerror("错误", "除数不能为零")
        except SyntaxError:
            messagebox.showerror("错误", "表达式格式不正确")
        except Exception as e:
            messagebox.showerror("错误", f"计算错误：{str(e)}")

    def clear(self):
        self.current_input = ""
        self.display_var.set("0")
        self.last_result = "0"

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()