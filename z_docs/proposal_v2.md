## 🎓 Project Proposal

**Title:** Smart University Ecosystem
**Team Member:** Ramyar, Rewan, Sovin, Bagzad, San

---

### **Abstract**

This project aims to develop a **Smart Attendance System** that uses **AI-based face recognition** and a **modern web interface** to automate and digitalize the attendance process at universities. The system eliminates the need for manual attendance taking, prevents proxy attendance, reduces human errors, and automatically updates attendance records in the university’s register system. The project combines artificial intelligence with a powerful web-based management system to modernize academic operations for teachers, students, and administrators.

---

### **Goal**

The main goal of this project is to **automate the attendance process** in universities using **AI and modern web technologies**. It will help teachers save time, reduce student cheating (proxy attendance), and ensure accurate, real-time attendance updates directly to the registrar system.

---

### **Current Practice**

Today, most universities still rely on **manual attendance methods** such as:

- Teachers **calling names** and **marking attendance** on paper or Excel sheets.
- Some institutions use **QR code scanning** or **ID card systems**, but these can still be **manipulated** by students sharing codes.
- Existing **face recognition projects** (for example, some small Python or OpenCV apps) can detect faces but **lack integration** with a full web system or university database.
  https://www.researchgate.net/publication/341876647_Face_Recognition_based_Attendance_Management_System?utm_source=chatgpt.com

Our system is **better** because it integrates **real-time face recognition** (via FastAPI and AI models) with a **modern web backend (TanStack Start)** that syncs data automatically to the registrar. It also provides **dashboards**, **role-based access**, and **secure cloud storage** — something missing from current methods.

---

### **Novelty**

Our approach is new because it **combines AI-based recognition with a full-stack automated web system**. Unlike most projects that stop at face detection, ours offers:

- Dual backend architecture (AI + Web)
- Automatic attendance submission to the registrar
- Modern, responsive UI built with TanStack Start (Router + Query + Prisma + PostgreSQL)
- Secure, our authentication system is designed to only support UKH email accounts.
- Multi-role access (Student, Teacher, Registrar, Admin)
  This integration makes the system faster, smarter, and more practical for real-world university use.

---

### **Effects**

If successful, this project will significantly **reduce time waste** for teachers, **eliminate proxy attendance**, and **modernize university operations**. Students benefit from transparent records, teachers save hours every week, and registrars receive automatic data updates with zero manual input. Overall, it creates a **smarter, paperless, and more efficient academic environment**.

---

### **Technical Approach**

We will use a **dual-backend architecture**:

1. **FastAPI Backend (AI & Logic Layer):** Handles **face recognition**, **AI model training**, and **attendance verification**. This backend focuses on image processing, feature extraction, and student face matching.
2. **TanStack Start (Web Logic Layer):** Built with **Ract (App Router)**, **RPC**, **Prisma**, and **PostgreSQL**, hosted on **Vercel**. This handles user management, dashboards, data visualization, and API communication with the FastAPI module.
3. **Frontend:** Uses **TanStack Start (React framework)** with **shadcn/ui**, **TailwindCSS**, and **NextAuth** for secure login and role management.
4. **Database:** PostgreSQL, managed via Prisma ORM, shared between web and AI systems for synchronized data.

**Development Tools:**

- **FastAPI**, **OpenCV**, **Face Recognition API**, **some modern technique (TanStank router, query, hook) ** **Server function (RPC)**, **Prisma**, **PostgreSQL**, **TailwindCSS**, **shadcn/ui**, **Vercel**, **Docker**, and **Figma (for UI design)**.

---

### **Risks**

The main challenge is ensuring **accurate and fast face recognition** in real-world classroom conditions (different lighting, masks, or angles).
To minimize this risk, we will:

- Use **high-quality training datasets** for our AI model.
- Apply **data augmentation techniques** (rotations, brightness changes).
- Continuously test and fine-tune the model with real student data before final deployment.

---

### **Methodology**

We will follow the **Agile Methodology**, allowing continuous development and improvement through sprints. Each sprint will deliver a working version — first focusing on the web system, then on the AI module, and finally integrating both. Agile ensures flexibility, teamwork, and faster iteration.

---

### **Team Roles**

| Member          | Role                 | Responsibility                                                                     |
| --------------- | -------------------- | ---------------------------------------------------------------------------------- |
| **[Your Name]** | Full Stack Developer | Develop web backend (T3 Stack), integrate with AI backend                          |
| **San**         | Backend Developer    | Work on API logic and web backend features                                         |
| **Rewan**       | UI/UX Designer       | Create the full design using **Figma**, ensuring a modern and accessible interface |
| **Sovin**       | Database Engineer    | Design and manage database schema and relationships in **PostgreSQL/Prisma**       |
| **Bagzad**      | System Analyst       | Create **flow charts**, system architecture, and documentation                     |

---

### **Folder Structure (for the system)**

```
smart-attendance/
│
├── fastapi-backend/                  # Backend for AI modules and face recognition
│   ├── app/
│   │   ├── face_recognition/         # Handles facial detection & verification using OpenCV + DeepFace
│   │   ├── ai_automation/            # Smart semester planner and AI-based automation logic (PyTorch)
│   ├── models/                       # Database models for attendance & recognition data
│   ├── routes/                       # API routes exposed via FastAPI (face scan, planner API)
│   └── main.py                       # Entry point of the FastAPI backend
│
├── tanstack-backend/                 # Full-stack web platform (TanStack + React + Prisma)
│   ├── src/
│   │   ├── components/               # Reusable UI components (buttons, inputs, cards, modals)
│   │   ├── routes/                   # Application routes (dashboard, attendance, planner, admin)
│   │   ├── api/                      # API handlers connecting frontend ↔ backend
│   │   ├── pages/                    # Static or dynamic pages (Home, Login, Register)
│   │   ├── utils/                    # Helper functions and hooks (auth, data fetching)
│   ├── prisma/                       # Database schema and migrations (PostgreSQL + Prisma ORM)
│   ├── styles/                       # Global and modular styles (CSS/Tailwind)
│   └── package.json                  # Project dependencies and scripts
│
├── design/                           # Figma design files, UI/UX mockups, and wireframes
│
├── docs/                             # Project documentation (proposal, flowcharts, SDLC, diagrams)
│
└── README.md                         # Main project overview, setup guide, and contribution details

```
