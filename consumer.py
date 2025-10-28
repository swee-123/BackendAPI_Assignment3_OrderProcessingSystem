from azure.servicebus import ServiceBusClient
import os, json
from dotenv import load_dotenv
from email_sender import send_email

load_dotenv()

CONN_STR = os.getenv("SERVICE_BUS_CONNECTION_STR")
TOPIC_NAME = os.getenv("TOPIC_NAME")
SUBSCRIPTION_NAME = os.getenv("SUBSCRIPTION_NAME")

def main():
    print("👂 Waiting for new orders...")
    sb_client = ServiceBusClient.from_connection_string(conn_str=CONN_STR)
    with sb_client:
        receiver = sb_client.get_subscription_receiver(
            topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME
        )
        with receiver:
            for msg in receiver:
                order = json.loads(str(msg))
                print("📩 Received message:", order)
                send_email(order["customerEmail"], order)
                receiver.complete_message(msg)

if __name__ == "__main__":
    main()
