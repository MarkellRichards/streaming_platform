## Images

- Zookeeper
- Kafka Server
- Connect
- Schema Regsitry
- Control Center
- sql-client (flink)
- Job Manager (flink)
- Task Manager (flink)
- Debezium Postgres
- Elastic Search
- Kibana
- Prometheus
- Grafana

## Docker commands

Run `docker-compose up --build -d`
Then `docker-compose run sql-client`

## Debezium

After starting Kafka Connect, setup Debezium postgres connecting using the configuration provided in the connectors directory labeled `postgres-debezium.json`:

```bash
curl -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d @/connectors/postgres-debezium.json'
```

## Documentation

- Elastic Search and Kibana images can be found at: [Elastic Images](https://www.docker.elastic.co/)
- Where to download JMX_Exporter for metrics collection: [jmx_exporter](https://github.com/prometheus/jmx_exporter?tab=readme-ov-file)
