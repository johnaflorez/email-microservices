import json
import pika

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

    archivo = '\nEmail Logs\n'
    archivo += 'Subject: {} \nFrom email: {} \n To: {} \n'.format(data['subject'], data['from_email'], data['to'])
    archivo += 'Message: \n'
    archivo += '\tType: {} \n\tCode: {} \n\tMessage: {}\n'.format(data['type'], data['code'], data['message'])
    archivo += '-'*50

    file = open('logs.txt', 'a')
    file.write(archivo)
    file.close()


channel.basic_consume(callback, queue=queue_name, no_ack=False)

channel.start_consuming()
