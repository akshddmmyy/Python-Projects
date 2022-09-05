import wmi
f = wmi.WMI()

pl=[]
for process in f.Win32_Process():
    pl.append(process)

killp=[]
for process in pl:
    if process.CommandLine == "\"C:\\Windows\\system32\\cmd.exe\" /c \"\"C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python39_64\\python.exe\" G:\\PythonApplication-PanBot\\Finalcode.py\" & pause" :
        killp.append(process)
        for j in pl:
            if(j.parentprocessid==process.processid):
                killp.append(j)
            '''for k in pl:
                if(k.parentprocessid==j.processid or k.parentprocessid==process.processid ):
                    killp.append(k)'''
for i in killp:
    if "python" in i.name:
        for j in pl:
            if(j.parentprocessid==i.processid):
                killp.append(j)
        break


for i in range(len(killp),0):
    killp[i].Terminate()
    
for i in killp:
    i.Terminate()
        
