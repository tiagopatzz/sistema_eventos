@echo off
cd /d %~dp0
call venv\Scripts\activate
uvicorn main_events:app --reload --port 8002