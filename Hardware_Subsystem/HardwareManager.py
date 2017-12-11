from VirtualMachine import VirtualMachine
from Server import Server


class HardwareManager:

    ServerList = []
    totalVmList = []

    def __init__(self):
        #s = Server("172.0.0.1", "root", "123456")
        self.createServer("172.0.0.1", "root", "123456")
        self.totalVmList = self.ServerList[0].pollVboxVMList()
        for lines in self.totalVmList:
            print lines.name, lines.networkAdapter, lines.vrdp, lines.currentSnapshot

    def updateVm(self, vm, name, vrdp, networkAdapter, currentSnapshot, hostName):
        vm.setName(name)
        vm.setVrdp(vrdp)
        vm.setNetworkAdapter(networkAdapter)
        vm.setCurrentSnapshot(currentSnapshot)
        vm.setHostname(hostName)

    def updateServer(self, server, ipAddress, userName, password):
        if isinstance(server, Server):
            server.setIpAddress(ipAddress)
            server.setUserName(userName)
            server.setPassword(password)

    def createServer(self, ipAddress, userName, password):
        sList=self.getServerList()
        for serverS in sList:
            if serverS.getUserName() == userName:
                return "Workshop group name is not unique"
        newServer = Server(ipAddress, userName, password)
        self.addServer(newServer,sList)
        return sList #delete
        #update database

    def addServer(self,server,serverList):
        serverList.append(server)
        #update mongo

    def deleteServer(self,server,serverList):
        serverList.remove(server)
        #update mongo

    def getServerList(self):
        return self.ServerList

    def getTotalVmList(self):
        return self.totalVmList


hm = HardwareManager()
#s = Server("172.0.0.1", "root", "123456")
#hm.createServer("172.0.0.1", "root", "123456")
#hm.totalVmList = hm.ServerList[0].pollVboxVMList()


