# cisco_ssh-python_text_file
Python Script using Netmiko to run commands on Cisco switches (read from a list of IPs in a text file - so that you can feed it the public IPs of your Firewall or other headend equipment, and it will parse through all of the port forwards you have set up in your Firewall etc. to access your Cisco switches (generally on private IPs) that sit behind the Firewall/controller etc., in order to run the script on the switches.

My goal was to create a script that you could feed a list of IPs (public IPs of Firewalls/MSM/Nomadii controllers which I manage), and access all of the networking switches behind these headend pieces of equipment to run commands en masse. In this scenario, if I have a Firewall on a public IP of 73.76.56.3 (for example) and I have 32 switches that sit behind it all accessible over port forwards on my Firewall (62001-62012), normally if I want to run a configuration on the switches I'd have to SSH into them over this public IP and the cooresponding port forward (the following IP/port for the core switch for example: 73.76.56.3:62001). So intead of having to do it manually this script will SSH into all switches that sit behind the public IPs you list in the text file, and access them over the port forwards you list in the Python script (62001 - 62032 in my exmple).
