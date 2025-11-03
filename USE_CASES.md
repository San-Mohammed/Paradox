# USE_CASES.md

## 🎯 Objective

This document models the **Smart University Ecosystem** — a learning management system with integrated **AI-based face recognition attendance** and **AI-powered quiz generation**.  
The goal of this use case modeling is to identify all **actor–system interactions** and provide a **complete and detailed overview** of system functionality as derived from the elicitation requirements.

---

## 1. Abstract Use Case Diagram (System Overview)

The following diagram represents the **entire system** and its primary actors.  
It shows all user roles and external systems interacting with the Smart University Ecosystem.

![System-Level Use Case Diagram](/assets/usecase-overview.jpg)

**Actors:**

- Teacher
- Student
- Registrar
- Admin
- Face Recognition Device (AI)
- Quiz Generator API (OpenAI)

---

## 2. Subsystem Use Case Diagrams

Each actor has specific interactions within the system.  
Below are detailed sub-diagrams focusing on each actor’s related use cases.

---

### 📘 2.1 Teacher Subsystem Use Case Diagram

**Actors:** Teacher, Face Recognition Device (AI Camera), Quiz Generator API (OpenAI)

**Use Cases:**

- Record Attendance with Face Recognition
- Manual Attendance (<<extend>>)
- Upload Lecture
- Generate Quiz (with AI API)
- Grade Student Submissions

![Teacher Subsystem Diagram](/assets/TeacherUseCase.jpg)

---

### 📗 2.2 Student Subsystem Use Case Diagram

**Actors:** Student

**Use Cases:**

- View Attendance Dashboard
- Submit Assignment/Quiz
- View Grades and Progress
- Receive Notifications
- Access Uploaded Lectures

![Student Subsystem Diagram](/assets/StudentUseCase.jpg)

---

### 📙 2.3 Registrar Subsystem Use Case Diagram

**Actors:** Registrar

**Use Cases:**

- Generate Attendance Reports
- Create and Manage Courses
- Assign Students and Teachers to Courses
- Manage Schedule and Timetables

![Registrar Subsystem Diagram](/assets/RegistrarUseCase.jpg)

---

### 📒 2.4 Admin Subsystem Use Case Diagram

**Actors:** Admin

**Use Cases:**

- Manage Users and Roles
- Monitor System Logs and Security
- Manage Announcements
- Backup and System Maintenance

![Admin Subsystem Diagram](/assets/AdminUseCase.jpg)

---

## 3. Detailed Use Case Descriptions

---

### UC-01 – Record Attendance with Face Recognition

| **Item**             | **Details**                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Primary Actor**    | Teacher                                                                                                                              |
| **Supporting Actor** | Face Recognition Device (AI)                                                                                                         |
| **Goal**             | Automatically record attendance using facial recognition cameras.                                                                    |
| **Pre-Conditions**   | Teacher logged in and session created.                                                                                               |
| **Post-Conditions**  | Attendance records saved with timestamps.                                                                                            |
| **Main Flow**        | 1. Teacher starts session.<br>2. System activates camera.<br>3. Device scans students.<br>4. Matches ≥85%.<br>5. Records attendance. |
| **Alternate Flow**   | Face not detected → teacher marks manually.                                                                                          |
| **Exceptions**       | Camera or network failure.                                                                                                           |
| **Relationship**     | <<extend>> UC-02 Manual Attendance                                                                                                   |

---

### UC-02 – Manual Attendance

| **Item**            | **Details**                                                        |
| ------------------- | ------------------------------------------------------------------ |
| **Primary Actor**   | Teacher                                                            |
| **Goal**            | Allow manual attendance if recognition fails.                      |
| **Pre-Conditions**  | Active attendance session exists.                                  |
| **Post-Conditions** | Manual attendance saved.                                           |
| **Main Flow**       | 1. Open manual attendance.<br>2. Mark students.<br>3. Save record. |
| **Exceptions**      | Unauthorized access.                                               |

---

### UC-03 – Upload Lecture

| **Item**            | **Details**                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Teacher                                                                                       |
| **Goal**            | Upload course materials (PDF, PPTX, etc.).                                                    |
| **Pre-Conditions**  | Teacher authenticated and assigned to a course.                                               |
| **Post-Conditions** | Files stored and available for students.                                                      |
| **Main Flow**       | 1. Teacher uploads.<br>2. System validates.<br>3. Stores in DB.<br>4. Confirmation displayed. |
| **Exceptions**      | File too large or invalid.                                                                    |

---

### UC-04 – Generate Quiz

| **Item**             | **Details**                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**    | Teacher                                                                                                                                        |
| **Supporting Actor** | Quiz Generator API (OpenAI)                                                                                                                    |
| **Goal**             | Automatically generate quiz based on lecture content.                                                                                          |
| **Pre-Conditions**   | Lecture uploaded.                                                                                                                              |
| **Post-Conditions**  | Quiz saved in database.                                                                                                                        |
| **Main Flow**        | 1. Teacher selects lecture.<br>2. Chooses “Generate Quiz.”<br>3. System sends lecture text to API.<br>4. Receives questions.<br>5. Saves quiz. |
| **Exceptions**       | API failure or no internet.                                                                                                                    |

---

### UC-05 – Grade Student Submissions

| **Item**            | **Details**                                                                      |
| ------------------- | -------------------------------------------------------------------------------- |
| **Primary Actor**   | Teacher                                                                          |
| **Goal**            | Review and grade student work.                                                   |
| **Pre-Conditions**  | Submissions exist.                                                               |
| **Post-Conditions** | Grades recorded and visible to students.                                         |
| **Main Flow**       | 1. Open submission.<br>2. Review answers.<br>3. Assign grade.<br>4. Save result. |
| **Exceptions**      | Database write failure.                                                          |

---

### UC-06 – View Attendance Dashboard

| **Primary Actor** | Student |
| **Goal** | View attendance rates and history. |
| **Pre-Conditions** | Student enrolled in courses. |
| **Post-Conditions** | Dashboard displays accurate attendance %. |
| **Main Flow** | 1. Student logs in.<br>2. Opens dashboard.<br>3. Data displayed per course. |
| **Exceptions** | Missing data or backend error. |

---

### UC-07 – Submit Assignment/Quiz

| **Primary Actor** | Student |
| **Goal** | Submit answers to assignments or quizzes. |
| **Pre-Conditions** | Quiz published and open. |
| **Post-Conditions** | Submission saved with timestamp. |
| **Main Flow** | 1. Student opens quiz.<br>2. Answers and submits.<br>3. Confirmation shown. |
| **Exceptions** | Late or incomplete submission. |

---

### UC-08 – View Grades and Progress

| **Primary Actor** | Student |
| **Goal** | View scores, grades, and gamified progress. |
| **Pre-Conditions** | Graded data exists. |
| **Post-Conditions** | Dashboard updated with results. |
| **Main Flow** | 1. Student opens progress tab.<br>2. System fetches data.<br>3. Displays grades and trophies. |
| **Exceptions** | No graded items available. |

---

### UC-09 – Receive Notifications

| **Primary Actor** | Student |
| **Goal** | Receive alerts (grades, new materials, quizzes). |
| **Pre-Conditions** | Student enrolled in courses. |
| **Post-Conditions** | Notifications delivered and stored. |
| **Main Flow** | 1. Event triggered (e.g., new quiz).<br>2. System sends alert.<br>3. Student reads notification. |

---

### UC-10 – Access Uploaded Lectures

| **Primary Actor** | Student |
| **Goal** | Access stored lecture materials. |
| **Main Flow** | 1. Opens course.<br>2. Views available files.<br>3. Downloads material. |
| **Exceptions** | File missing or permission denied. |

---

### UC-11 – Generate Attendance Reports

| **Primary Actor** | Registrar |
| **Goal** | Generate attendance summaries for courses. |
| **Pre-Conditions** | Attendance data available. |
| **Post-Conditions** | Report generated (PDF/CSV). |
| **Main Flow** | 1. Registrar selects course/date.<br>2. System compiles data.<br>3. Exports report. |

---

### UC-12 – Manage Courses

| **Primary Actor** | Registrar |
| **Goal** | Create, edit, or remove courses. |
| **Main Flow** | 1. Open course manager.<br>2. Add/edit course info.<br>3. Save changes. |

---

### UC-13 – Assign Students and Teachers to Courses

| **Primary Actor** | Registrar |
| **Goal** | Assign users to existing courses. |
| **Pre-Conditions** | Courses and users exist. |
| **Post-Conditions** | Enrollments saved. |

---

### UC-14 – Manage Schedule and Timetables

| **Primary Actor** | Registrar |
| **Goal** | Define schedules for classes. |
| **Main Flow** | 1. Choose course.<br>2. Set class time.<br>3. Save. |

---

### UC-15 – Manage Users and Roles

| **Primary Actor** | Admin |
| **Goal** | Manage all users and assign roles. |
| **Main Flow** | 1. Add/edit users.<br>2. Set permissions.<br>3. Save changes. |

---

### UC-16 – Monitor System Logs and Maintenance

| **Primary Actor** | Admin |
| **Goal** | Monitor activity logs and perform backups. |
| **Main Flow** | 1. Open logs panel.<br>2. Review user actions.<br>3. Trigger backup or maintenance task. |

---

## 4. Relationships and Interactions

| **Relationship Type**     | **Description**                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **<<extend>>**            | “Record Attendance with Face Recognition” extends “Manual Attendance.” |
| **<<include>>**           | “Generate Quiz” includes “Send Request to OpenAI API.”                 |
| **External System Links** | Face Recognition Device provides input; OpenAI API returns quiz data.  |

---

**End of Document**
