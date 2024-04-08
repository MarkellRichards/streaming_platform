## Applications

- Zookeeper
- Kafka Broker
- Connect
- Schema Regsitry
- Control Center
- Flink
- Postgres
- Apache Pinot
- Prometheus
- Grafana

## Docker commands

- Run `docker-compose up --build -d` to build the custom Flink image initially and start rest of applications.
- `docker-compose run sql-client` to interact with Flink Sql Client.

## Debezium

After starting Kafka Connect, setup Debezium postgres connecting using the configuration provided in the connectors directory labeled `postgres-debezium.json`:

```bash
curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @connectors/postgres-debezium.json
```

## Documentation

- Where to download JMX_Exporter for metrics collection: [jmx_exporter](https://github.com/prometheus/jmx_exporter?tab=readme-ov-file)
