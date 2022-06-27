import subprocess
import GetServices
import GetPortAndServicesResolver

res=GetPortAndServicesResolver.get_ports() #list has format Port:PID

services=GetServices.get_services() #list has format PID:Services

#When value of value in res same as key in servces update it in another dictionary
final_dict={}
for x in range(0,len(services),1):
    for key in res:
        for keys in services:
            if res[key]==keys:
                final_dict[key]=services[keys]




print(final_dict)

