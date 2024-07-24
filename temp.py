import tkinter as tk
from tkinter import ttk

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, f"Number 1: {num1}\n")
        output_text.insert(tk.END, f"Number 2: {num2}\n")
        output_text.insert(tk.END, f"Sum: {result}\n")
    except ValueError:
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, "Please enter valid numbers\n")

# 创建主窗口
root = tk.Tk()
root.title("Sum Calculator")

# 创建输入框和标签
label1 = ttk.Label(root, text="Number 1:")
label1.grid(column=0, row=0, padx=10, pady=5)

entry1 = ttk.Entry(root)
entry1.grid(column=1, row=0, padx=10, pady=5)

label2 = ttk.Label(root, text="Number 2:")
label2.grid(column=0, row=1, padx=10, pady=5)

entry2 = ttk.Entry(root)
entry2.grid(column=1, row=1, padx=10, pady=5)

# 创建计算按钮
calculate_button = ttk.Button(root, text="Calculate", command=calculate_sum)
calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

# 创建输出框
output_text = tk.Text(root, height=5, width=30)
output_text.grid(column=0, row=3, columnspan=2, pady=5, padx=10)

# 运行主循环
root.mainloop()
