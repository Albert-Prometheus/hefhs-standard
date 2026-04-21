# AGENTS.md - HEFHS 數據湖庫專案

## 自然語言原則

- **輸出語言**：繁體中文
- **思維鏈順序**：繁體中文 → 英文 → 簡體中文（补充推理用）

## 快速啟動

### 本地開發環境

```bash
# Docker network（啟動 Docker Desktop 後）
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

| 服務 | Port |
|------|------|
| Jupyter (PySpark) | 8888 |
| PostgreSQL | 5048 |
| pgvector | 5049 |
| pgAdmin | 5050 |
| FerretDB | 37017 |

## 技術架構

- **程式語言**：Python
- **框架**：PySpark, Jupyter
- **資料庫**：PostgreSQL, pgvector, FerretDB
- **Harness Engineering & AI Agentic Coding**：OpenCode with Oh-My-OpenAgent Plug-in

## 待完成

- [ ] README 專案概述
- [ ] 入口點與套件結構
- [ ] .env 模板
- [ ] 建置/測試/代碼風格命令