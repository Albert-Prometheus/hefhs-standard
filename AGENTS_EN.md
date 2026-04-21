# AGENTS.md - HEFHS Data Lakehouse Project

## Natural Language Principles

- **Output Language**: English (Traditional Chinese for local context)
- **Thought Chain Order**: Traditional Chinese → English → Simplified Chinese (supplementary reasoning)

## Quick Start

### Local Development Environment

```bash
# Docker network (after starting Docker Desktop)
docker network create data-lakehouse 2>/dev/null || true

# Jupyter + PySpark (8888)
docker run -d --name all-spark --network data-lakehouse -e GRANT_SUDO=yes --user root -it -p 8888:8888 -v "C:\Users\Albert Yang\Documents\PySpark":/home/jovyan jupyter/all-spark-notebook:x86_64-spark-3.5.0

# PostgreSQL (5048)
docker run -d --name pgsql --network data-lakehouse -e POSTGRES_PASSWORD=admin -p 5048:5432 -v "C:\Docker\pgSQL_Data":/var/lib/postgresql/data postgres:16.11

# pgvector (5049)
docker run -d --name pgvector --network data-lakehouse -e POSTGRES_PASSWORD=admin -p 5049:5432 -v "C:\Docker\pgVector_Data":/var/lib/postgresql/data pgvector/pgvector:pg16

# pgAdmin (5050)
docker run -d --name pgadmin --network data-lakehouse -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=albert.ycd@gmail.com -e PGADMIN_DEFAULT_PASSWORD=admin dpage/pgadmin4

# FerretDB (37017)
docker run -d --rm --name ferretdb --network data-lakehouse -p 37017:27017 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin ghcr.io/ferretdb/ferretdb-eval:2
```

| Service | Port |
|--------|------|
| Jupyter (PySpark) | 8888 |
| PostgreSQL | 5048 |
| pgvector | 5049 |
| pgAdmin | 5050 |
| FerretDB | 37017 |

## Technical Architecture

- **Programming Language**: Python
- **Framework**: PySpark, Jupyter
- **Database**: PostgreSQL, pgvector, FerretDB
- **Harness Engineering & AI Agentic Coding**: OpenCode with Oh-My-OpenAgent Plug-in

## TODOs

- [ ] README with project overview
- [ ] Entry points and package structure
- [ ] .env template
- [ ] Build/test/lint commands