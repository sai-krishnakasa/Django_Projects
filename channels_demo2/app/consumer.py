from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
class  MySyncConsumer(SyncConsumer):
    #This method is called when a websocket requests for a handshake
    # if two way hanshake acheives the connection will be 
    # successful and below method executes 
    def websocket_connect(self,event):
        print('websocket connection Success...',event)
        #unless we use the self.send() method 
        #below the connection could not be stable
        #it will get connected and disconnected 
        self.send({
            # This is an event (webscoket.accept) to accept the incoming connection
            'type':'websocket.accept'
        })
 

    #This method is called when  a message is sent from 
    #client side and we can read and do something with that 
    #using event['text'] get the sent text

    def websocket_receive(self,event):
        print('Message Received is...',event['text'])
        #the above line is to get data from the client
        #the below line is to send data from the application to client
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(1)

    def websocket_disconnect(self,event):
        print("Connection Closed...",event)
        raise StopConsumer()

# To run in postman 
# url ws://127.0.0.1:8000/ws/sc
# url ws://127.0.0.1:8000/ws/asc

class  MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print('  async websocket connection Success...',event)
        await self.send({
            'type':'websocket.accept'
        })
    async def websocket_receive(self,event):
        print(' async Message Received...',event)
        print(' async Message Received...',event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self,event):
        print("async Connection Closed...",event)
        raise StopConsumer()
