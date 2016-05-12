#!/Users/kawasakitaku/Documents/python-PVM/ln-python3.4/bin/python3.4

from twisted.internet import protocol,reactor

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello World")

    def dataReceived(self,data):
        print("Server said: ", data)
        self.transport.loseConnection()

class EchoFactory (protocol.ClientFactory):
    def buildProtocol(self,addr):
        return EchoClient()

    def clientConnectionFailed(self,connector,reason):
        print("connection Error")
        reactor.stop()

    def clientConnectionLost(self,connector,reason):
        print ("Connection Lost")
        reactor.stop()

reactor.connectTCP("localhost",8000,EchoFactory())
reactor.run()
        
        
