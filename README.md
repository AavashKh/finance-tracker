# Cashriver Setup Developement
High performance financial dashboard built with **FastAPI, React and PostgreSQL** to help achieve sub 100ms UI updates.

## Tech Stack
**Frontend:** Vite + React + TypeScript + Tailwind CSS (soon)
**Backend:** FastAPI (For fast API calls)
**Charts:** ChartJS (Alpha/Beta trends Visualization)
**Database:** PostgreSQL (Server : Raspberry PI 4)

## System Architectures
The app follows a **Tier-1 Architecture**:
1. **Frontend:** Client-side rendering for real-time ticker updates.
2. **API Layer:** FastAPI serves as the "Execution Engine," handling data validation.
3. **Storage Layer:** PostgreSQL ensures ACID compliance for every financial record.
