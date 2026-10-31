# AWS Industrial Digital Twin & Cloud-Native IIoT Platform

A learning and engineering project that progressively builds a smart
manufacturing digital twin using simulated industrial equipment.

## Industrial scenario

Initially simulate three machines: a conveyor motor, a pump, and a compressor.
Telemetry will include equipment identifiers, timestamps, operating states,
and relevant measurements such as temperature, vibration, and RPM.

The planned digital twin will maintain machine state, health indicators,
and equipment relationships, with historical data and APIs.

## Roadmap

1. Industrial simulator and MQTT foundation
2. Kafka event streaming
3. Digital twin engine with PostgreSQL and FastAPI
4. Kubernetes, Helm, and Argo CD GitOps
5. AWS IoT Core and Terraform
6. Observability, CI/CD, and reliability
7. AWS deployment validation and final showcase

Each phase requires implementation, testing, documentation, and revision
notes before progressing. There are no fixed deadlines.

## Current status

- EC2 development environment verified.
- Git and GitHub CLI configured.
- Public GitHub repository created.
- Initial Python simulator implemented and verified from two working directories.

## Development principles

- Run the Python simulator directly before introducing MQTT and Docker.
- Introduce each technology only when it solves a demonstrated problem.
- Validate behavior using actual terminal output and failure testing.
- Keep credentials out of Git and infrastructure costs low.
- Use simulated equipment; this is not a live factory deployment.

## Run the initial simulator

Requires Python 3. Tested on Python 3.14.4; no external packages are required.

From the repository root:

```bash
python3 simulator/simulate.py
```

The script prints three JSON events and exits. Readings are illustrative,
all machines are running, and no MQTT connection is made yet.

See [consolidated revision notes](docs/interview-revision/revision.md)
for design decisions, validation, and current limitations.
