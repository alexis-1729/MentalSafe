# MentalSafe

MentalSafe is a microservices-based platform focused on mental health support, counseling, educational content, AI-assisted interactions, and monitoring. The project combines multiple specialized services for authentication, user management, chat, course delivery, professional access, NLP/LLM analysis, and notifications.

## Overview

The repository is organized as a set of independent services that communicate through a shared Docker network. The main goal is to provide a modular platform where different components handle specific business capabilities without coupling them tightly.

The platform includes:

- user authentication and session management
- user profiles and account workflows
- course and educational content delivery
- professional or expert domain services
- chat and messaging features
- notification management
- NLP-based analysis and LLM-powered assistance
- retrieval-augmented generation (RAG) support
- test or assessment services

## Architecture

The project uses Docker Compose to orchestrate the complete system. The main infrastructure includes:

- multiple FastAPI-based microservices
- PostgreSQL instances per service or domain
- a Qdrant vector database for retrieval workflows
- a shared internal Docker network named `mentalnet`

A simplified view of the architecture is:

```text
MentalSafe
├── auth-service
├── users-service
├── course-service
├── profesional-service
├── chating-service
├── notification-service
├── nlp-service
├── llm-service
├── rag-service
├── test-service
├── qdrant
├── postgres databases
└── docker-compose.yml
```

## Repository structure

```text
MentalSafe/
├── .gitignore
├── docker-compose.yml
├── qdrant_storage/
├── services/
│   ├── auth-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── tests/
│   ├── chating-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── course-service/
│   │   ├── app/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── llm-service/
│   │   └── ...
│   ├── nlp-service/
│   │   └── ...
│   ├── notification-service/
│   │   └── ...
│   ├── profesionaL-service/
│   │   └── ...
│   ├── rag-service/
│   │   └── ...
│   ├── test-service/
│   │   └── ...
│   └── users-service/
│       └── ...
├── README.md
└── docker-compose.yml
```

## Services

### 1) auth-service
Responsible for authentication, JWT or token-based access control, user login, refresh tokens, and security-related utilities.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8000

### 2) users-service
Handles user registration, profile data, and user-related operations.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8010

### 3) course-service
Provides educational or training content management, course logic, chapters, sections, and materials.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8004

### 4) profesional-service
Covers professional user management, counselor or expert services, and domain-specific workflows.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8005

### 5) chating-service
Provides chat and messaging functions, room management, and notification integrations.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8006

### 6) notification-service
Handles push or service notifications for the platform.

- Main application: FastAPI
- Database: PostgreSQL
- Port: 8007

### 7) nlp-service
Focused on NLP or textual analysis workflows for mental health signal detection and similar classification tasks.

- Port: 8008

### 8) llm-service
Responsible for LLM-powered assistance, conversation generation, or AI support features.

- Port: 8009

### 9) rag-service
Provides retrieval-augmented generation capabilities, likely for context retrieval and grounding responses with external knowledge or platform data.

- Port: 8002
- Database: PostgreSQL
- Vector store: Qdrant

### 10) test-service
Runs testing or evaluation endpoints, likely for assessment tasks or validation flows.

- Port: 8003

## Data and infrastructure

The infrastructure defined in `docker-compose.yml` includes the following services:

- `authdb` on port 5436
- `test-db` on port 5435
- `rag-db` on port 5437
- `usersdb` on port 5438
- `course-db` on port 5439
- `profesional-db` on port 5440
- `chating-db` on port 5441
- `notification-db` on port 5442
- `qdrant` on port 6333

Each service uses its own database or storage layer depending on its domain.

## Prerequisites

Before running the project, make sure you have installed:

- Docker
- Docker Compose
- Git
- Python 3.10+ (for local services outside containers)

## Quick start

Clone the repository:

```bash
git clone https://github.com/alexis-1729/MentalSafe.git
cd MentalSafe
```

Start all services:

```bash
docker compose up --build
```

To stop the infrastructure:

```bash
docker compose down
```

To remove persistent volumes:

```bash
docker compose down -v
```

## Accessing services

After startup, the following local endpoints are exposed:

- Auth service: http://localhost:8000
- Test service: http://localhost:8003
- RAG service: http://localhost:8002
- Users service: http://localhost:8010
- Course service: http://localhost:8004
- Profesional service: http://localhost:8005
- Chat service: http://localhost:8006
- Notification service: http://localhost:8007
- NLP service: http://localhost:8008
- LLM service: http://localhost:8009
- Qdrant dashboard: http://localhost:6333

## Environment configuration

Some services use `.env` files and environment-based configuration. For example:

- `services/auth-service/.env`
- `services/course-service/.env`
- `services/profesional-service/.env`
- `services/chating-service/.env`
- `services/notification-service/.env`
- `services/rag-service/.env`
- `services/llm-service/.env`

Make sure those files exist and contain the required secrets and connection strings before running the stack in a real environment.

## Development notes

This is a modular platform designed for experimentation and deployment in a microservice environment. The codebase follows a layered structure in each service:

- API layer
- application/service layer
- domain layer
- infrastructure layer
- persistence models and repositories

This pattern is visible in services such as `auth-service` and `course-service`.

## Recommended workflow

1. Start the stack with Docker Compose.
2. Verify the database containers are healthy.
3. Test each service independently via its FastAPI endpoints.
4. Validate communication between services over the internal Docker network.
5. Use Qdrant and the LLM/RAG services for knowledge retrieval and AI-powered responses.

## Notes

This repository appears to be in a development stage and may still require:

- environment cleanup
- secret management improvements
- service health checks
- CI/CD configuration
- automated tests for all services
- documentation per service

## License

No explicit license file is currently present in the repository. If you plan to distribute or publish this project publicly, consider adding a license such as MIT or Apache 2.0.

## Contributing

Contributions are welcome. Before submitting changes, please:

- keep each service self-contained
- document API and configuration changes
- test locally with Docker Compose when possible
- keep environment variables secure and avoid committing secrets

## Contact

For questions, improvements, or collaboration, contact the repository owner or maintainers on GitHub.
