# Cashriver Setup Developement
High performance financial dashboard built with **FastAPI, React and PostgreSQL** to help achieve sub 100ms UI updates.

## Tech Stack
**Frontend:** Vite + React + TypeScript + Tailwind CSS\
**Backend:** FastAPI (For fast API calls)\
**Charts:** ChartJS (Alpha/Beta trends Visualization)\
**Database:** PostgreSQL (Server : Raspberry PI 4)

## System Architectures
The app follows a **Tier-1 Architecture**:
1. **Frontend:** Client-side rendering for real-time ticker updates.
2. **API Layer:** FastAPI serves as the "Execution Engine," handling data validation.
3. **Storage Layer:** PostgreSQL ensures ACID compliance for every financial record.

## Setup
### Database Setup (Server)
Before beginning, ensure that the SSD is mounted to the server.
```bash
#Enter the Postgres vault
sudo -u postgres psql

#Execute the Initialization Script
CREATE DATABASE finance_db;
CREATE USER dev_admin WITH PASSWORD 'give it a password';
GRANT ALL PRIVILAGES ON DATABASE finance_db TO dev_admin;
```
### Backend Setup (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate # Use this before working on the backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000 # Use this as well to start your local server
```
### Frontend Setup (Vite + React)
```bash
cd frontend
npm install
npm run dev
```
