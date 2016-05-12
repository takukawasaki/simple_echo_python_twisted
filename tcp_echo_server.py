#!/Users/kawasakitaku/Documents/python-PVM/ln-python3.4/bin/python3.4

from twisted.internet import protocol,reactor

class Echo (protocol.Protocol):
    def dataReceived (self,data):
        self.transport.write(data)

class EchoFactory (protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()

reactor.listenTCP(8000,EchoFactory())

reactor.run()
