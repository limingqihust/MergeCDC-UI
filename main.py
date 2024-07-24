import tkinter as tk
from tkinter import ttk



def TeraSort():
    try:
        total_node_num = entry_total_node_num.get()
        file_distribution = text_file_distribution.get("1.0", tk.END).strip()
        rack_config = text_rack_config.get("1.0", tk.END).strip()
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, f"total node num: {total_node_num}\n")
        output_text.insert(tk.END, f"file distribution: {file_distribution}\n")
        output_text.insert(tk.END, f"rack config: {rack_config}\n")
    except ValueError:
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, "Please enter valid numbers\n")


def CodedTeraSort():
    try:
        total_node_num = entry_total_node_num.get()
        file_distribution = text_file_distribution.get("1.0", tk.END).strip()
        rack_config = text_rack_config.get("1.0", tk.END).strip()
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, f"total node num: {total_node_num}\n")
        output_text.insert(tk.END, f"file distribution: {file_distribution}\n")
        output_text.insert(tk.END, f"rack config: {rack_config}\n")
    except ValueError:
        output_text.delete("1.0", tk.END)  # 清除之前的内容
        output_text.insert(tk.END, "Please enter valid numbers\n")

def OpenFileDistributionSubWindow():
    # 创建一个新的顶级窗口（子窗口）
    input_window = tk.Toplevel(root)
    input_window.title("Input Subwindow")
    
    # 子窗口中的标签和多行文本框
    sub_label = ttk.Label(input_window, text="Enter your input:")
    sub_label.pack(padx=10, pady=10)
    
    sub_text = tk.Text(input_window, width=40, height=10)
    sub_text.pack(padx=10, pady=10)
    
    # 子窗口中的确认按钮
    def confirm_input():
        # 获取子窗口中的输入内容
        input_text = sub_text.get("1.0", tk.END).strip()
        # 将输入内容设置到主窗口的输入框中
        text_file_distribution.delete("1.0", tk.END)
        text_file_distribution.insert("1.0", input_text)
        # 关闭子窗口
        input_window.destroy()
    
    confirm_button = ttk.Button(input_window, text="Confirm", command=confirm_input)
    confirm_button.pack(padx=10, pady=10)

def OpenRackConfigSubWindow():
    # 创建一个新的顶级窗口（子窗口）
    input_window = tk.Toplevel(root)
    input_window.title("Input Subwindow")
    
    # 子窗口中的标签和多行文本框
    sub_label = ttk.Label(input_window, text="Enter your input:")
    sub_label.pack(padx=10, pady=10)
    
    sub_text = tk.Text(input_window, width=40, height=10)
    sub_text.pack(padx=10, pady=10)
    
    # 子窗口中的确认按钮
    def confirm_input():
        # 获取子窗口中的输入内容
        input_text = sub_text.get("1.0", tk.END).strip()
        # 将输入内容设置到主窗口的输入框中
        text_rack_config.delete("1.0", tk.END)
        text_rack_config.insert("1.0", input_text)
        # 关闭子窗口
        input_window.destroy()
    
    confirm_button = ttk.Button(input_window, text="Confirm", command=confirm_input)
    confirm_button.pack(padx=10, pady=10)

root = tk.Tk()
root.title("MergeCDC")

# input node total num
label_total_node_num = ttk.Label(root, text="total node num:")
label_total_node_num.grid(column=0, row=2, padx=10, pady=5)

entry_total_node_num = ttk.Entry(root)
entry_total_node_num.grid(column=1, row=2, padx=10, pady=5)

# input file distribution
label_file_distribution = ttk.Label(root, text="file distribution:")
label_file_distribution.grid(column=0, row=3, padx=10, pady=5)

text_file_distribution = tk.Text(root, width = 20, height = 2)
text_file_distribution.grid(column=1, row=3, padx=10, pady=5)
text_file_distribution.bind("<Button-1>", lambda event: OpenFileDistributionSubWindow())

# input rack config
label_rack_config = ttk.Label(root, text="rack config:")
label_rack_config.grid(column=0, row=4, padx=10, pady=5)

text_rack_config = tk.Text(root, width = 20, height = 2)
text_rack_config.grid(column=1, row=4, padx=10, pady=5)
text_rack_config.bind("<Button-1>", lambda event: OpenRackConfigSubWindow())


# exec terasort
terasort_button = ttk.Button(root, text = "TeraSort", command = TeraSort)
terasort_button.grid(column=0, row=5, padx=5, pady=5)

# exec codedterasort
codedterasort_button = ttk.Button(root, text = "CodedTeraSort", command = CodedTeraSort)
codedterasort_button.grid(column=1, row=5, padx=5, pady=5)


# 创建输出框
output_text = tk.Text(root, height=5, width=30)
output_text.grid(column=0, row=6, columnspan=2, pady=5, padx=10)

# 运行主循环
root.mainloop()

