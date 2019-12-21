# Type your code here
davy_auto_services = {'Oil change':35,'Tire rotation':19,'Car wash':7,'Car wax':12}
print("Davy's auto shop services")
for key,value in davy_auto_services.items():
 print(key,'-- $'+str(value))
 #print('')
first_service = input('\nSelect first service: \n\n')
#print('')
second_service = input('Select second service: \n\n')
#print('')
print("\nDavy's auto shop invoice\n")
if first_service in davy_auto_services and first_service !='-':
  print('Service 1:', first_service + ', $' + str(davy_auto_services[first_service]))   
else:
  print('Service 1: No service')
if second_service in davy_auto_services and second_service !='-':
  print('Service 2:', second_service + ', $' + str(davy_auto_services[second_service]))   
else:
  print('Service 2: No service')

if first_service=='-':
  total = davy_auto_services.get(second_service)
  print('Total: $'+ str(total))
elif second_service=='-':
  total = davy_auto_services.get(first_service)
  print('Total: $'+ str(total))
else:
  total = davy_auto_services.get(first_service) + davy_auto_services.get(second_service)
  print('Total: $'+ str(total))
   
