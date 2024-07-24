import subprocess

def run_cpp_program(executable_path, args):
    try:
        # 调用可执行文件并传递参数
        result = subprocess.run([executable_path] + args, capture_output=True, text=True)

        # 获取标准输出和标准错误
        stdout = result.stdout
        stderr = result.stderr

        # 获取返回码
        returncode = result.returncode

        return stdout, stderr, returncode
    except Exception as e:
        return str(e), "", -1

# 可执行文件路径
executable_path = "./helloworld.exe"

# 要传递给可执行文件的参数
args = ["arg1", "arg2"]

# 调用可执行文件
stdout, stderr, returncode = run_cpp_program(executable_path, args)

# 输出结果
print("标准输出:", stdout)
print("标准错误:", stderr)
print("返回码:", returncode)
