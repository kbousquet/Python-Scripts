import shutil
import psutil

# check_disk_usage will receive a disk to check usage and return TRUE if more than 20% is free, false it less.
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

# check_cpu_usage will check the usage over 1 full second and return TRUE if usage is less than 75%.
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("SUCCESS!")
