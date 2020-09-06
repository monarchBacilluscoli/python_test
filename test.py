import subprocess

port_assigned = {0: 0}
f = open("/home/liuyongfeng/sc2output")
f2 = open("/home/liuyongfeng/sc2output_modified", 'w')
line = f.readline()
while line:
    # print(type(line))
    if 'distributed' in line:
        # line = line.replace("Waiting for connection", "").replace(".", '')
        # print(line)
        start_index = line.find("distributed")
        line = line[start_index+12:-1]
        mid_index = line.find("target")
        line = line[:mid_index]+line[mid_index+8:]+"\n"
        print(int(line[:mid_index-2]))
        if int(line[:mid_index-2]) in port_assigned:
            port_assigned[int(line[:mid_index-2])] += 1
        else:
            port_assigned[int(line[:mid_index-2])] = 1

        f2.write(line)
    line = f.readline()

f.close()
f2.close()
a = subprocess.run("netstat -ntulp | grep SC2 | sort -k 4",
                   text=True, shell=True, capture_output=True)
results = a.stdout.split('\n')

for item in results:
    if(item == ''):
        results.remove(item)

print(len(results))


print("唉，夏海")
