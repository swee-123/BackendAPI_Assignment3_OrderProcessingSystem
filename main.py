from fastapi import FastAPI, HTTPException
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os, json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Azure Order Processing System")

CONN_STR = os.getenv("SERVICE_BUS_CONNECTION_STR")
TOPIC_NAME = os.getenv("TOPIC_NAME")

@app.post("/place-order")
def place_order(order: dict):
    """
    Receive order from Postman and publish to Azure Service Bus topic.
    """
    try:
        sb_client = ServiceBusClient.from_connection_string(conn_str=CONN_STR)
        with sb_client:
            sender = sb_client.get_topic_sender(topic_name=TOPIC_NAME)
            with sender:
                message = ServiceBusMessage(json.dumps(order))
                sender.send_messages(message)
                print(f"✅ Order sent to Service Bus: {order['orderId']}")
        return {"status": "success", "message": "Order published successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
