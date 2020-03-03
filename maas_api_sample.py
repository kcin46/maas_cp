import maas_api_functions as functions, getpass as gp, sys, time, json
from pyfiglet import Figlet

print("\n*************************************************************************")

banner = Figlet(font='doom')
print(banner.renderText('Check Point API'))

sid = None
login_attempts = 0

#Loop that allows user 3 attempts to login
while(sid is None):
    if(login_attempts >= 0 and login_attempts < 3):
        login_attempts += 1
    else:
        print("You have exceeded your login attempts")
        print("Goodbye")
        time.sleep(5)
        sys.exit()

    #Prepare for MaaS tenant login
    service_id = input("Please enter service identifier of MaaS tenant: ")
    shared_sec = input("Please enter shared secret of MaaS tenant: ")
    user = input("Username: ")
    password = gp.getpass()
    print("\n")
    sid = functions.maas_login(user, password, service_id, shared_sec)
    print(sid)
    print("*****")
    if(sid is None):
        print("The information you have entered is incorrect.\n")

exit = 0
first_iteration = 1

#Infinite loop that displays API Commands until user logs out
while(exit == 0):
    if(first_iteration == 1):
        print("Welcome " + user)

    print("Configuration Options:")
    print("----------------------")
    print("(1)\tAdd Host")
    print("(2)\tDelete Host")
    print("(3)\tAdd Network")
    print("(4)\tDelete Network")
    print("(5)\tPublish")
    print("(6)\tLogout\n")
    print("(7)\tShow Time Objects\n")
    response = input("Enter your choice number: ")

    if(response == '1'):
        name = input("Enter Host Name: ")
        host_addr = input("\nEnter Host IP Address: ")
        response = functions.maas_add_host(name, host_addr, service_id, shared_sec, sid)
        #response = maas_func.add_host
        #response = functions.add_host(name, host_addr, mgmt_ip, sid)

    if(response == '2'):
        name = input("Enter host name to be deleted: ")
        response = functions.maas_delete_host(name, service_id, shared_sec, sid)
    '''
    if(response == '3'):

    if(response == '4'):
    '''

    if(response == '5'):
        functions.maas_publish(service_id, shared_sec, sid)
    #Completed 6
    if(response == '6'):
        logout_result = functions.maas_logout(service_id, shared_sec, sid)
        exit = 1

    if(response == '7'):
        time_objs = functions.maas_show_times(service_id, shared_sec, sid)

    first_iteration += 1
