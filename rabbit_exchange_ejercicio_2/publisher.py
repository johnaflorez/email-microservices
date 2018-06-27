import json
import pika
import sys

"""
subject = input("Ingrese asunto: >")
from_email = input("Ingrese email remitente: >")
to = input("Ingrese email destino: >")
body = input("Ingrese mensaje: >")
"""

subject = "Saludos"
from_email = "pruebadajngo@gmail.com"
to = "johnflorez_1289@hotmail.com"
type = "error"
code = "302"
message = "error de servidor"

info = {
    'subject': subject,
    'from_email': from_email,
    'to': to,
    'type': type,
    'code': code,
    'message': message
}

data = json.dumps(info)

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='direct'
)

message = ' '.join(sys.argv[1:]) or 'info: hello world'

channel.basic_publish(
    exchange='logs',
    routing_key=type,
    body=data
)

print("[*] Sent message: {}".format(message))

connection.close()
