import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

for x in range(20):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    time.sleep(1)

print(" [x] Sent 'Hello World!'")

connection.close()