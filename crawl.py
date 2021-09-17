import subprocess

file = open("raw_data.txt", "w")

start = 18020574
end = 18020579

for i in range(start, end):
    cmd = 'curl -F "keysearch=' + \
        str(i) + '" http://112.137.129.87//congdaotao/module/dsthi/index.php?r=lopmonhoc/napmonthi'
    raw_data = subprocess.check_output(cmd, shell=True)

    file.write(str(raw_data) + "\n")
