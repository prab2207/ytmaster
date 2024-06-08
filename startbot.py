import subprocess
import time

while(1==1):
    print("# starting process")
    edge_path = r"c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url="https://ytmaster.onrender.com/loadYT/8"
    #command = [brave_path,url, "--incognito"] #brave
    #command = [edge_path,url, "-inprivate"]
    command = [edge_path,url]
    subprocess.run(command)
    print("# started process")
    time.sleep(4*60*60)
    print("# resetting process")
    command = ["taskkill", "/F", "/IM", "msedge.exe"]
    subprocess.run(command)
    print("# closed all process")
    time.sleep(2)