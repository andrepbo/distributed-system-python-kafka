from confluent_kafka import Consumer, KafkaException

# Server configuration
# Specify your Kafka bootstrap servers
bootstrap_servers = 'localhost:9092'
topic = 'ai_data_topic'  # Specify the Kafka topic

# Kafka consumer configuration
conf = {'bootstrap.servers': bootstrap_servers,
        'group.id': 'ai_server_group',
        'auto.offset.reset': 'earliest'}
consumer = Consumer(conf)
consumer.subscribe([topic])

print('Waiting for messages from Kafka topic:', topic)

try:
    while True:
        msg = consumer.poll(timeout=1000)  # Timeout in milliseconds
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event, not an error
                continue
            else:
                raise KafkaException(msg.error())
        # Process the received message
        print('Received message: {}'.format(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    # Close down consumer to commit final offsets.
    consumer.close()
