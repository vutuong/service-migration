import paramiko
import time
import request
import docker
def connect_api(ip_device, container_name):
	port = 4243
	base_url = "tcp://"+ str(ip_device) + ":" + str(port)
	# client = docker.DockerClient(base_url='tcp://192.168.10.252:4243')
	client = docker.DockerClient(base_url= base_url)
	container = client.containers.list(all, filters = {'name' :container_name})
	print(container)
	# print(container[0].id)
	# print(container[0].image)
	return container, client.containers
def get_container_id(container):
	return container[0].id
def get_container_image(container):
	return container[0].image
def create_container(container, image):
	container.create(image, name="cr")

def ssh(ip, username, password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=str(ip), port=int(22), username= username, password= password)
	shell = client.invoke_shell()
	time.sleep(1)
	return shell

def migrate():
	ip_source = "192.168.10.207"
	ip_dest = "192.168.10.22"
	user_source = "slave"
	pass_source = "slave"
	user_dest = "master"
	pass_dest = "master"
	# get container infomation from source node
	container_name = "k8s_tuong_tuong-manual_default_904f36bc-68b8-42d8-9b51-3b73aadab2b1_1"
	# container_source, client_source = connect_api(ip_source, container_name)
	# container_source_id = get_container_id(container_source)
	# container_source_image = get_container_image(container_source)

	# create container in destination node using source service image
	container_dest, client_dest = connect_api(ip_dest, container_name)
	# create_container(client_dest, container_source_image)
'''
	# get container infomation from destination node
	container_dest_id = get_container_id(container_dest)
	print(container_dest_id)

	# transfer checkpoint state from source to destination
	# client = paramiko.SSHClient()
	# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# client.connect(hostname='192.168.10.252', port=int(22), username='docker', password='docker')
	# shell = client.invoke_shell()
	# time.sleep(1)
	connect_source = ssh(ip_source, user_source, pass_source)
	cmd  = "sudo chmod -R 777 /var/lib/docker/containers/* \n"
	#  + str(container_source_id) +"/* \n"
	connect_source.send(cmd)
	time.sleep(1)
	cmd1 = "scp -r /var/lib/docker/containers/" + str(container_source_id)\
	+ "/checkpoints/checkpoint0 master@" + str(ip_dest) + ":/var/lib/docker/containers/" + \
	str(container_dest_id) + "/checkpoints \n"
	print(cmd1)
	connect_source.send(cmd1)
	time.sleep(2)
	result = connect_source.recv(65535).decode('ascii')
	print("aaaaaaa")
	print(result)
	connect_source.close()

	connect_dest = ssh(ip_dest, user_dest, pass_dest)
	# cmd1 = "sudo chmod 777 /var/lib/docker/containers/" + str(container_dest_id) +"/* \n"
	# connect_dest.send(cmd1)
	# result = connect_source.recv(65535).decode('ascii')
	# print("cccc")
	# print(result)

	time.sleep(1)
	cmd2 = "sudo docker start --checkpoint checkpoint0 " + str(container_name) + "\n"
	connect_dest.send(cmd2)
	time.sleep(2)
	connect_dest.send("\n")
	result = connect_source.recv(65535).decode('ascii')
	print("bbbb")
	print(result)'''
migrate()

# connect_api('192.168.10.252', 'cr')
# connect_api('192.168.10.143', 'cr')