class VirtualMachine:
    vmCount = 0

    def __init__(self, name, vrdp, networkAdapter, currentSnapshot, hostName):
        self.name = name
        self.vrdp = vrdp
        self.networkAdapter = networkAdapter
        self.currentSnapshot = currentSnapshot
        self.hostName = hostName
        VirtualMachine.vmCount += 1

    def displayCount(self):
        print("Total VM %d" % VirtualMachine.vmCount)

    def getName(self):
        return self.name

    def getVrdp(self):
        return self.vrdp

    def getNetworkAdapter(self):
        return self.networkAdapter

    def getCurrentSnapshot(self):
        return self.currentSnapshot

    def getHostname(self):
        return self.hostName

    def setName(self, name):
        self.name = name

    def setVrdp(self, vrdp):
        self.vrdp = vrdp

    def setNetworkAdapter(self, networkAdapter):
        self.networkAdapter = networkAdapter

    def setCurrentSnapshot(self, currentSnapshot):
        self.currentSnapshot = currentSnapshot

    def setHostname(self, hostName):
        self.hostNam = hostName
