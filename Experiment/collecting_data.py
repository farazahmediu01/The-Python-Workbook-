import subprocess


tasks = subprocess.check_output(['tasklist','/NH', '/FO', 'CSV']).decode('cp1252').split('\r\n')
for i in tasks:      
    tasks[i].replace('"','').split(',')

