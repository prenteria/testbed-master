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

    def parse_vm_name(self, vm_name_list):
        """
        Parses the output of list_vm_names() to grab only the text name
        :param vm_name_list: A list of virtual machines in the format "VmName {UUID}"
        :return: List of only the "VmName format"
        """
        toparse = []
        for indexx in vm_name_list:
            toparse.append(re.findall(r'\"(.+?)\"', indexx))  # Regex to garb text between quotes
        return toparse

    def parse_all(self, name=''):
        f = subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "showvminfo", name, "--machinereadable"]).splitlines()
        data = [eachLine for eachLine in f]
        toparse = []
        vrdp = -1
        network = "NoInternal"
        snapshot = "NoSnapshot"

        for indexx in data:
            if(re.findall(r'vrdeports', indexx)): #Checks if there is a vrde ports exist
                vrdp = re.findall(r'\"(.+?)\"', indexx) # then parses the value
            if (re.findall(r'intnet1', indexx)):
                network = re.findall(r'\"(.+?)\"', indexx)
            if (re.findall(r'CurrentSnapshotName', indexx)):
                snapshot = re.findall(r'\"(.+?)\"', indexx)

        if vrdp == -1:
            toparse.append('3389')
        else:
            toparse.append(vrdp)
        if network == "NoInternal":
            toparse.append('NoInternal')
        else:
            toparse.append(network)
        if snapshot == "NoSnapshot":
            toparse.append('NoSnapshot')
        else:
            toparse.append(snapshot)
        return toparse

    def establishConnection(self):
        """
        TODO: Try establish a connection to the server at the ip stored in ipAddress
        
        :return: a boolean if the connection was seccessful or not
        """
        return True

    def pollVboxVMList(self):
        """
        TODO: Connects to the server and gets the list from it.
        :return: returns an updated list of vms that exist on a server
        """
        vmlist = []
        server_response = self.parse_vm_name(self.list_vm_names())
        parsed_response = []
        for lines in server_response:
            parsed_response = self.parse_all(lines[0])
            vmlist.append(VirtualMachine(lines[0], ''.join(parsed_response[0]), ''.join(parsed_response[1]), ''.join(parsed_response[2]), self))
        #self.vmList = vmlist
        return vmlist


    def restore_snapshot(self, name):
        """
        Return list of vms with uuid combine into one string. will be replaced by pollVboxVMList
        """
        subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "snapshot", name , "restorecurrent"])


    def cloneVM(self, name, port, seed, numClone):
        info = []
        name_list = []
        s = str(seed)
        currCloneNum = 1
        while (currCloneNum <= numClone):
            cloneName = name + "(" + str(currCloneNum) + ")"
            name_list.append(cloneName)
            clonePort = str(port + int(currCloneNum))
            subprocess.check_output(
                ["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "clonevm", name, "--name", cloneName,
                 "--register"])
            # set VRDE port
            subprocess.check_output(
                ["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "modifyvm", cloneName, "--vrdeport", clonePort])
            # set seed
            subprocess.check_output(
                ["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "modifyvm", cloneName, "--intnet1", s])
            currCloneNum = currCloneNum + 1
        l = self.pollVboxVMList() #chase bank! Nice!
        count = 0
        while(count < len(l)):
            for x in range(0, currCloneNum-1):
              if(l[count].name == name_list[x]):
                    info.append(l[count])
                    break
            count += 1
        return info

#test = Server("test", "test", "test")
#hope = test.cloneVM("TinyLinux_plus", 5000, "test", 4)

#for lines in hope:
#    print lines.name, lines.networkAdapter, lines.vrdp, lines.currentSnapshot
