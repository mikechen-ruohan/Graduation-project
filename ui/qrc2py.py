import subprocess
import sys

# 确保路径正确，且路径中没有特殊字符
rcc_executable = r"E:\OpenProject_yolov8\0_test\MTSP-main\venv\Scripts\pyside6-rcc.exe"
qrc_file = r"E:\OpenProject_yolov8\0_test\main\ui\resources.qrc"
output_file = r"E:\OpenProject_yolov8\0_test\main\ui\resources.py"

# 调用 pyside6-rcc 编译资源文件
subprocess.run([rcc_executable, qrc_file, "-o", output_file], check=True)
