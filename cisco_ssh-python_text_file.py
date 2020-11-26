# Python Script using Netmiko to run commands on Cisco switches

from netmiko import ConnectHandler

with open('device_IPs.txt') as IP_LIST:
    for IP in IP_LIST:
        device_1 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62001,
        }   
        
        device_2 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62002,
        } 
        
        device_3 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62003,
        } 
        
        device_4 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62004,
        } 
        
        device_5 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62005,
        } 
        
        device_6 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62006,
        } 
        
        device_7 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62007,
        } 
        
        device_8 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62008,
        } 
        
        device_9 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62009,
        } 
        
        device_10 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62010,
        } 
        
        device_11 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62011,
        } 
        
        device_12 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62012,
        } 
        
        device_13 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62013,
        } 
        
        device_14 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62014,
        } 
        
        device_15 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62015,
        } 
        
        device_16 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62016,
        } 
        
        device_17 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62017,
        } 
        
        device_18 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62018,
        } 
        
        device_19 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62019,
        } 
        
        device_20 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62020,
        } 
        
        device_21 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62021,
        } 
        
        device_22 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62022,
        } 
        
        device_23 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62023,
        } 
        
        device_24 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62024,
        } 
        
        device_25 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62025,
        }
        
        device_26 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62026,
        }
        
        device_27 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62027,
        }
        
        device_28 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62028,
        }
        
        device_29 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62029,
        }
        
        device_30 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62030,
        }
        
        device_31 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62031,
        }
        
        device_32 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'declan.knittel@fakemail.com',
        'password': 'REDACTED',
        'port': 62032,
        }
        
        all_devices = [device_1, device_2, device_3, device_4, device_5, device_6, 
                        device_7, device_8, device_9, device_10, device_11, device_12, 
                        device_13, device_14, device_15, device_16, device_17, device_18, 
                        device_19, device_20, device_21, device_22, device_23, device_24, 
                        device_25, device_26, device_27, device_28, device_29, device_30,
                        device_31, device_32]
        
        for x in all_devices:
            try:
                print ('\n Connecting to the device @ ' + IP)
                net_connect = ConnectHandler(**x)

                # enter enable mode
                net_connect.enable()

                # Execute the command(s) you want
                output = net_connect.send_command("show clock")

                print(output)
                
                # enter config mode
                net_connect.send_config_set()

                # send configuration commands to this device
                net_connect.send_config_set(['ntp server 88.88.88.88',  
                              'end'])
                
                # save config
                net_connect.save_config()
                
                output = net_connect.send_command("show clock")
                
                print(output)

            except:
                print('!!!!!Unable to connect to switch!!!!!')