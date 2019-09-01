import psutil
import datetime
import platform

cpu_stats = psutil.cpu_stats() // Retorna estatisticas da CPU:
print(cpu_stats)

//ctx_switches: number of context switches (voluntary + involuntary) since boot.
//interrupts: number of interrupts since boot.
//soft_interrupts: number of software interrupts since boot. Always set to 0 on Windows and SunOS.
//syscalls: number of system calls since boot. Always set to 0 on Linux.



cpu_logical_count = psutil.cpu_count(logical=True) // Número de CPUs lógicas (Physical cores only (hyper thread excluded)
cpu_physical_count = psutil.cpu_count(logical=False) //Numero de CPUs Físicas

print ("Your computer have {} logical cpus cores !".format(cpu_logical_count))
print ("Your computer have {} physical cpus cores !".format(cpu_physical_count))
                                                                              
                                                                              
boot_time =  datetime.datetime.fromtimestamp(psutil.boot_time())
                                                                              
                                                                              
print ("You are logged in your system since: {}".format(boot_time))
                                                                                                                                                            

// biblioteca Platform. plataform.uname retorna 6 atributos (system, node, release, version, machine e processor)
system, node, release, version, arch, processor  = platform.uname() 
system = system.split('-')[0]

print("Machine OS: {} \nVendor: {} \nRelease: {} \nVersion {} \nArchiteture: {} \nProcessor: {} ".format(system,vendor,release,version,arch,processor))
