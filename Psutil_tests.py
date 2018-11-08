import psutil
import datetime
import platform

cpu_stats = psutil.cpu_stats()
print(cpu_stats)
cpu_logical_count = psutil.cpu_count()
print ("Your computer have {} logical cpus cores !".format(cpu_logical_count))
boot_time =  datetime.datetime.fromtimestamp(psutil.boot_time())
print ("You are logged in your system since: {}".format(boot_time))
system, vendor, release, version, arch, processor  = platform.uname()
system = system.split('-')[0]

print("Machine OS: {} \nVendor: {} \nRelease: {} \nVersion {} \nArchiteture: {} \nProcessor: {} ".format(system,vendor,release,version,arch,processor))