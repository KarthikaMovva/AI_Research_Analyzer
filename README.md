# 🤖 Multi-Agent AI Research System (LangGraph + RAG)

A multi-agent AI system built using **LangGraph, FastAPI, and React**, designed to simulate an intelligent research pipeline.  
It processes user queries through multiple AI agents and generates structured reports using a **RAG-based knowledge base**.

---

## 🚀 System Architecture
User

↓

React UI

↓

FastAPI Backend

↓

LangGraph Orchestrator

↓

Planner Agent

↓

Researcher Agent (RAG Retrieval from PDFs)

↓

Critic Agent (Validation & Refinement)

↓

Writer Agent (Report Generation)

↓

Final Report


---

## 🧠 Key Features

- Multi-Agent AI system using LangGraph
- Retrieval-Augmented Generation (RAG)
- PDF-based knowledge base (local `/Data` folder)
- Specialized agents:
  -  Planner → breaks down query
  -  Researcher → retrieves relevant context from PDFs
  -  Critic → validates and improves output
  -  Writer → generates final report
- FastAPI backend for orchestration
- React frontend for user interaction
- Modular architecture for future scaling

---
## Agents Description
  - Planner Agent
Breaks query into subtasks
Defines execution strategy
  - Researcher Agent
Retrieves relevant chunks from PDFs
Acts as RAG retriever
  - Critic Agent
Checks correctness and completeness
Improves reasoning output
  - Writer Agent
Generates final structured report
Ensures clarity and formatting

## Current Limitation
  - Only works with 2 PDFs in /Data folder
  - No dynamic upload feature yet
  - Static knowledge base

## Future Improvements
  - PDF upload API for dynamic ingestion