@echo off
cd /d %~dp0
call venv\Scripts\activate
uvicorn main_users:app --reload --port 8001