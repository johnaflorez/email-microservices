import json
import pika

from send_email import enviar_email

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue="send_email")


def email(ch, method, properties, body):
    data = json.loads(str(body)[2:-1])
    enviar_email(data['subject'], data['to'], data['from_email'], data['body'])


channel.basic_consume(email, queue='send_email', no_ack=True)

print("Inicio worker")

channel.start_consuming()