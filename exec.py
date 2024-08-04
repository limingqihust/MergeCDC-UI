import subprocess
from enum import Enum


class JobType(Enum):
    TeraSort = 1
    CodedTeraSort = 2


def Exec(type):
    try:
        if type == JobType.TeraSort:
            args = ["mpirun", "-np", "31", "--oversubscribe", "./MergeCDC/TeraSort"]
            result = subprocess.run(args, capture_output = True, text = True)
            stdout = result.stdout
            return stdout
        elif type == JobType.CodedTeraSort:
            args = ["mpirun", "-np", "32", "--oversubscribe", "./MergeCDC/CodedTeraSort"]
            result = subprocess.run(args, capture_output = True, text = True)
            stdout = result.stdout
            return stdout
    except Exception as e:
        return str(e)
