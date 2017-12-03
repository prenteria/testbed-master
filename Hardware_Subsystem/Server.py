import re, subprocess
from VirtualMachine import VirtualMachine
class Server:
    serverCount = 0
    vmList = []

    def __init__(self, ipAddress, userName, password):
        self.ipAddress = ipAddress
        self.userName = userName
        self.password = password
        self.status = self.establishConnection()
        self.vmList = self.pollVboxVMList()
        Server.serverCount += 1

    def getIpAddess(self):
        return self.ipAddress

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getStatus(self):
        return self.status

    def setIpAddess(self, ip):
        self.ipAddress = ip

    def setUserName(self, name):
        self.userName = name

    def setPassword(self, password):
        self.password = password

    def getvmlist(self):
        return self.vmList

    def list_vm_names(self):
        """
        Return list of vms with uuid combine into one string. will be replaced by pollVboxVMList

        """
        f = subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "list", "vms"]).splitlines()
        data = [eachLine for eachLine in f]
        return data

    def parse_vm_info(vm_name_list):
        """
        Parses the output of list_vm_names() to grab only the text name
        :param vm_name_list: A list of virtual machines in the format "VmName {UUID}"
        :return: List of only the "VmName format"
        """
        toparse = []
        for indexx in vm_name_list:
            toparse.append(re.findall(r'\"(.+?)\"', indexx))  # Regex to garb text between quotes
        return toparse

    def establishConnection(self):
        """
        TODO: Try establish a connection to the server at the ip stored in ipAddress
        
        :return: a boolean if the connection was seccessful or not
        """
        return False

    def pollVboxVMList(self):
        """
        TODO: Connects to the server and gets the list from it.
        
        :return: returns an updated list of vms that exist on a server
        """
        vmlist = []
        return  vmlist

    test = parse_vm_info(list_vm_names(0))
    for lines in test:
        print(lines)