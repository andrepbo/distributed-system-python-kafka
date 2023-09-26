import json
from confluent_kafka import Producer

# Client configuration
# Specify your Kafka bootstrap servers
bootstrap_servers = 'localhost:9092'
topic = 'ai_data_topic'  # Specify the Kafka topic

# Simulated data to send to the AI server
data = {"input": [0.1, 0.2, 0.3]}

print('Sending data to the AI server:', data)  # Display the sent data

# Kafka producer configuration
conf = {'bootstrap.servers': bootstrap_servers}
producer = Producer(conf)

# Produce the data to the Kafka topic
producer.produce(topic, key='ai_input', value=json.dumps(data))
producer.flush()

print('Data sent to Kafka topic:', topic)
