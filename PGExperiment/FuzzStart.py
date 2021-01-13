from subprocess import Popen, PIPE
import time
print("Fuzztainer..")

target_list = ["chris0", "chris1", "chris2", "chris3", "chris4", "chris5", "chris6", "chris7"]
cmds_list = [["../fuzztainer.py", "-w", "./PGResults/" + target, target] for target in target_list]

proc_list = []
for cmd in cmds_list:
	proc_list.append(Popen(cmd, stdout=PIPE))
	time.sleep(5)


for proc in proc_list:
	proc.wait()

#print("Commands: ", cmds_list)
#print("\n\nProcesses: ", proc_list)




#processes = []
#for i in range(8):
#	p = subprocess.Popen(["../fuzztainer.py", "-w", "./PGResults/" + str(i), "chris" + str(i)], stdout=subprocess.PIPE)
#	time.sleep(5)
#	processes.append(p)
#for p in processes:
#	p.wait()


