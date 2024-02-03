from google.cloud import pubsub_v1
from random import choice, uniform
import json
import time
import random
from datetime import datetime, timedelta

# Initialize the Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()

# Project and Topic details
project_id = "gds-proj"
sales_topic_name = "sales-transaction"
inv_topic_name = "inventory_topic"
sales_topic_path = publisher.topic_path(project_id, sales_topic_name)
inv_topic_path = publisher.topic_path(project_id, inv_topic_name)


def generate_sales_transaction():
    transaction_id = f"T{random.randint(1000, 100000)}"
    product_id = f"P{random.randint(501, 510)}"
    timestamp = (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d %H:%M:%S")
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(50.0, 500.0), 2)
    store_id = f"W{random.randint(1, 10)}"

    return {
        "transaction_id": transaction_id,
        "product_id": product_id,
        "timestamp": f"{timestamp}",
        "quantity": f"{quantity}",
        "unit_price": f"{unit_price}",
        "store_id": store_id
    }

def generate_inventory_update(prod,qty,stor):
    product_id = prod
    timestamp = (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')
    quantity_change = qty
    store_id = stor
    
    return {
        "product_id": product_id,
        "timestamp": f"{timestamp}",
        "quantity_change": f"-{quantity_change}",
        "store_id": store_id
    }

def callback(future):
    try:
        # Get the message_id after publishing.
        message_id = future.result()
        print(f"Published message with ID: {message_id}")
    except Exception as e:
        print(f"Error publishing message: {e}")

# Print generated data
i=1000
while True:
    if i==99999:
       break
    try:
        i=i+1
        sales_data=generate_sales_transaction()
        prod = sales_data["product_id"]
        qty = sales_data["quantity"]
        stor = sales_data["store_id"]
        inv_data = generate_inventory_update(prod,qty,stor)
        print('JSON CREATED')
        json_sales_data = json.dumps(sales_data).encode('utf-8')
        json_inv_data = json.dumps(inv_data).encode('utf-8')

        print('ENCODED')
        sales_future = publisher.publish(sales_topic_path, data=json_sales_data)
        sales_future.add_done_callback(callback)
        sales_future.result()
        print('PUBLISHED FOR SALES')
        print("Sales_data : ",sales_data)
        print("inventory data : ",inv_data)
        inv_future = publisher.publish(inv_topic_path, data=json_inv_data)
        inv_future.add_done_callback(callback)
        inv_future.result()
        print('PUBLISHED FOR INV')
        print('-------------X---------------')
        time.sleep(2)
    except Exception as e:
        print(f"Exception encountered: {e}")