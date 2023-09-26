# Docker and Kafka Setup

This README provides a guide on setting up Docker and Kafka with the listed commands.

- `docker-compose -f docker-compose.yml up -d`: Start Docker services defined in `docker-compose.yml` in detached mode.
- `docker images`: List Docker images.
- `docker ps`: List running Docker containers.
- `docker exec -it kafka /bin/sh`: Execute an interactive shell in the Kafka container.
- `cd /opt/kafka_2.13-2.8.1`: Change directory to the Kafka installation path.
- `bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --topic ai_data_topic --partitions 1 --replication-factor 1`: Create a Kafka topic named `ai_data_topic`.
- `bin/kafka-topics.sh --list --bootstrap-server localhost:9092`: List Kafka topics using the specified bootstrap server.
- `bin/kafka-console-consumer.sh --topic ai_data_topic --from-beginning --bootstrap-server localhost:9092`: Start a console consumer for the `ai_data_topic`.

These commands facilitate setting up and managing a Kafka instance using Docker containers.
