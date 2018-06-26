import json
import pika


subject = input("Ingrese asunto: >")
from_email = input("Ingrese email remitente: >")
to = input("Ingrese email destino: >")
body = input("Ingrese mensaje: >")

info = {
    'subject': subject,
    'from_email': from_email,
    'to': to,
    'body': body
}
data = json.dumps(info)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.queue_declare(queue="send_email")

channel.basic_publish(
    exchange="",
    routing_key="send_email",
    body=data
)

print("Finalizado")

connection.close()
