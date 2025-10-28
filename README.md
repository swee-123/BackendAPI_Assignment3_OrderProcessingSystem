🚀 Azure Service Bus Order Processing API

A simple FastAPI-based API that sends order data to an Azure Service Bus Topic.
This project demonstrates how to connect FastAPI with Azure Service Bus for event-driven order processing.

📘 Features

Receive new order requests via REST API

Publish order messages to Azure Service Bus Topic

Easily extensible for order tracking or email notifications

🛠️ Tech Stack

Python 3.10+

FastAPI

Azure Service Bus SDK

dotenv

Mailtrap (optional, for email simulation)

⚙️ Setup Instructions
1️⃣ Clone this repository
git clone https://github.com/<your-username>/Azure_Order_Processing_System.git
cd Azure_Order_Processing_System

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create a .env file

Create a file named .env in your project folder and add the following:

SERVICE_BUS_CONNECTION_STR=your_azure_service_bus_connection_string
TOPIC_NAME=your_topic_name


⚠️ Note: Do not share your connection string publicly.

▶️ Running the Application

Start the FastAPI development server using:

fastapi dev main.py


The API will start at:

http://127.0.0.1:8000

📬 API Endpoint
POST /place-order

Description:
Receives an order JSON payload and publishes it to the Azure Service Bus Topic.

Example Request (JSON):

{
  "orderId": "ORD102",
  "customerName": "Alice",
  "product": "Bluetooth Speaker",
  "quantity": 3,
  "price": 1799.50
}


Example Response:

{
  "status": "success",
  "message": "Order published successfully"
}

☁️ Azure Service Bus Setup

Go to your Azure portal → Create a Service Bus Namespace

Inside it, create a Topic (e.g., order-topic)

Copy your Connection String from the Shared Access Policies section

Paste it into your .env file

🧩 Project Structure
Order_Processing_System/
│
├── main.py                  # FastAPI app (publishes messages)
├── consumer.py              # Reads messages from Azure topic/subscription
├── email_sender.py          # Sends emails via Mailtrap
├── .env                     # Environment variables
├── .gitignore               # Ignore sensitive files
├── requirements.txt          # Dependencies
└── README.md                # Documentation

🚀 Future Enhancements

Add a subscription-based consumer to process messages in real-time

Integrate with Mailtrap or SendGrid for email alerts

Store order data in Azure SQL or Cosmos DB

🧑‍💻 Author

Swetha
