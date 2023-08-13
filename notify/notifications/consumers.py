from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name="test_consumer"
        self.room_group_name="test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            #order of both of these matters 
            # self.room_group_name,self.channel_name
            self.room_group_name,self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected from django channels'}))
        
    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        self.send(text_data=json.dumps({'status':'we got you'}))
    
    
    def disconnect(self, code):
        print("Disconnected..")
        
        
    def send_notification(self,event):
        print('send_notification')
        print(event)
        self.send(json.dumps(event['value']))
        print('send_notification')