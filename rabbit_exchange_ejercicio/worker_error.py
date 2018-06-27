import pika
import json

from send_email import enviar_email

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

results = channel.queue_declare(exclusive=True)

queue_name = results.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print("[*] Starting worker with queue {}".format(queue_name))


def callback(ch, method, properties, body):
    data = json.loads(str(body)[2:-1])

    if data['type'] == 'error':
        msg = 'Tipo: {} \nCódigo: {} \nMensaje: {}'.format(data['type'], data['code'], data['message'])
        enviar_email(data['subject'], data['to'], data['from_email'], msg)


channel.basic_consume(callback, queue=queue_name, no_ack=False)

channel.start_consuming()
