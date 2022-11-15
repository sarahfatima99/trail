#!/usr/bin/env python
import pika
import os
import json
from event_handlers import handlers



class consumer:

    def rabbit_connection(self):

        credentials = pika.PlainCredentials('root','root')
        pika.ConnectionParameters(credentials=credentials)

        connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))

        return connection   



    
    def create_queues(self,queue_name):

        connection = self.rabbit_connection()
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        return channel


    def receive_payload(self):

        connection = self.rabbit_connection()
        channel = connection.channel()

        result = channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            
           
            h=handlers(body)
            db_obj=h.get_db_object()
            db_obj.dump_into_database()           
         
    
        channel.queue_bind(exchange='new_exchange',queue=result.method.queue)
        channel.basic_consume(queue='hello',on_message_callback=callback, auto_ack=True)   
        channel.start_consuming()


    
# consumer, domain - business logic, infrastructre


    


