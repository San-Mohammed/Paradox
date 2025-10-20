# Smart University Ecosystem

## Overview

This project automates the university attendance system using **AI-based face recognition** and a **modern TanStack web backend**. It saves teachers’ time, prevents proxy attendance, and directly updates the registrar system with accurate records.

## Goal

To create a fully automated, reliable, and smart attendance system that supports teachers, students, and the registrar with real-time updates.

## Technologies

1. **FastAPI Backend (AI & Logic Layer):** Handles **face recognition**, **AI model training**, and **attendance verification**. This backend focuses on image processing, feature extraction, and student face matching.
2. **TanStack Start (Web Logic Layer):** Built with **Ract (App Router)**, **RPC**, **Prisma**, and **PostgreSQL**, hosted on **Vercel**. This handles user management, dashboards, data visualization, and API communication with the FastAPI module.
3. **Frontend:** Uses **TanStack Start (React framework)** with **shadcn/ui**, **TailwindCSS**, and **NextAuth** for secure login and role management.
4. **Database:** PostgreSQL, managed via Prisma ORM, shared between web and AI systems for synchronized data.

## Team

- **Ramyar** - Backend (face recognition, FastAPI, integrate with AI)
- **San** – Full Stack Developer
- **Rewan** – UI/UX Designer
- **Sovin** – Database Manager
- **Bagzad** – System Analyst

## Repository Structure

```md
smart-attendance/
│
├── ai-backend/ # Backend for AI modules and face recognition
│ ├── app/
│ │ ├── face_recognition/ 
│ │ ├── ai_automation/    #(PyTorch)
│ ├── models/  
│ ├── routes/ 
│ └── main.py 
│
├── tanstack/ # Full-stack web platform (TanStack + React + Prisma)
│ ├── src/
│ │ ├── components/ # Reusable UI components 
│ │ ├── routes/ # Application routes (dashboard, attendance, planner, admin)
│ │ ├── api/ # API handlers connecting frontend ↔ backend
│ │ ├── pages/ 
│ │ ├── utils/ 
│ ├── prisma/ # Database schema and migrations (PostgreSQL + Prisma ORM)
│ ├── styles/ 
│ └── package.json 
│
├── design/ # Figma design files, UI/UX mockups, and wireframes
│
├── docs/ # Project documentation (proposal, flowcharts, SDLC, diagrams)
│
└── README.md # Main project overview, setup guide, and contribution details
```
