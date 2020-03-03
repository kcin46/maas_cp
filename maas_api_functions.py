import requests, json

#API call for MaaS Tenant
def maas_api_call(command, json_payload, service_id, secret, sid = ''):
    url = 'https://' + service_id + '.maas.checkpoint.com/' + secret + '/web_api/' + command
    if(sid == ''):
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    try:
        r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
        if(r.status_code == 200):
            return r.json()
        else:
            print(r.status_code)
            return None
    except Exception as e:
        print("Connection error:\n")

def maas_login(user, password, service_id, secret):
    payload = {'user' : user, 'password' : password}
    response = maas_api_call('login', payload, service_id, secret)

    if(response is None):
        return None
    else:
        return response["sid"]

# Logs out of the current session
def maas_logout(service_id, shared_sec, sid):
    logout_result = maas_api_call('logout', {}, service_id, shared_sec, sid)
    print("logout result: " + json.dumps(logout_result))

# Publish current session
def maas_publish(service_id, shared_sec, sid):
    publish_result = maas_api_call('publish', {}, service_id, shared_sec, sid)
    print("publish result: " + json.dumps(publish_result))

# Add a new host object
def maas_add_host(name, new_host_ip_addr, service_id, shared_sec, sid):
    payload = {'name': name, 'ip-address': new_host_ip_addr }
    new_host_result = maas_api_call('add-host', payload, service_id, shared_sec, sid)
    print(json.dumps(new_host_result))

# Delete host object
def maas_delete_host(name, service_id, shared_sec, sid):
    payload = { 'name': name }
    delete_host_result = maas_api_call('delete-host', payload, service_id, shared_sec, sid)
    print(json.dumps(delete_host_result))

def maas_where_used(service_id, shared_sec, sid, uid):
    payload = { 'uid' : uid }
    where_used = maas_api_call('where-used', payload, service_id, shared_sec, sid)
    print(where_used)

def maas_show_times(service_id, shared_sec, sid):
    payload = { 'details-level' : 'full'}
    times = maas_api_call('show-times', payload, service_id, shared_sec, sid)

    for obj in times['objects']:
        uid = obj['uid']
        maas_where_used(service_id, shared_sec, sid, uid)
    #print(times)
