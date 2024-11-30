@echo off
cd /d %~dp0
call venv\Scripts\activate
uvicorn main_registrations:app --reload --port 8003