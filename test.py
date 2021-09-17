import subprocess


data = subprocess.check_output('curl -F "sobaodanh=02000001" diemthi.hcm.edu.vn/Home/Show', shell= False)

decode = data.decode()

file = open("test.txt", "w", encoding='utf8')

file.write(str(decode))

print(len(data))

print(len(decode))