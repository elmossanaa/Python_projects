import subprocess
import datetime

#creating file to save the report
report_path = "system_health_report.txt"

#timestamp for report header
timestamp = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")

with open (report_path,"w") as report:
    report.write("=" * 40 + "\n")
    report.write(f"SYSTEM HEALTH REPORT - {timestamp} \n")
    report.write("=" * 40 + "\n")

    #test 1: ping

    report.write("[1] Ping Test (8.8.8.8)\n")
    result = subprocess.run(["ping", "-n","2", "8.8.8.8"],capture_output = True, text = True)
    report.write(result.stdout + "\n")

    #test 2: Disck Space
    report.write("[2] Disk Space\n")
    result = subprocess.run(["powershell", "-Command","Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, FreeSpace"],
                            capture_output = True, text = True)
    report.write(result.stdout + "\n")

    #test 3: System Boot time
    report.write("[3] System Boot Time\n")
    result = subprocess.run(["systeminfo"], capture_output = True, text = True)

    for i in result.stdout.split("\n"):
        if "Boot Time" in i:
            report.write(i.strip() + "\n")


    report.write("=" * 40 + "\n")
    report.write("End of Report \n")
