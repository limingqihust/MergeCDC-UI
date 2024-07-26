import subprocess

def Exec(type):
    try:
        if type == "TeraSort":
            args = ["mpirun", "-np", "31", "--oversubscribe", "./MergeCDC/TeraSort"]
            result = subprocess.run(args, capture_output = True, text = True)
            stdout = result.stdout
            return stdout
        elif type == "CodedTeraSort":
            args = ["mpirun", "-np", "32", "--oversubscribe", "./MergeCDC/CodedTeraSort"]
            result = subprocess.run(args, capture_output = True, text = True)
            stdout = result.stdout
            return stdout
    except Exception as e:
        return str(e)
