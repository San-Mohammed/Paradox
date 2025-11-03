# USE_CASES.md

## 🎯 Objective

This document models the **Smart University Ecosystem** — a learning management system with integrated **AI-based face recognition attendance** and **AI-powered quiz generation**.  
The goal of this use case modeling is to identify all **actor–system interactions** and provide a **complete and detailed overview** of system functionality as derived from the elicitation requirements.

---

## 1. Abstract Use Case Diagram (System Overview)

The following diagram represents the **entire system** and its primary actors.  
It shows all user roles and external systems interacting with the Smart University Ecosystem.

![System-Level Use Case Diagram](/assets/usecase.jpg)

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

| **Item**            | **Details**                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Primary Actor**   | Student                                                                                                                  |
| **Goal**            | View personal attendance records and percentages per course.                                                             |
| **Pre-Conditions**  | Student is logged in and enrolled in at least one course.                                                                |
| **Post-Conditions** | Attendance data displayed correctly on the dashboard.                                                                    |
| **Main Flow**       | 1. Student logs in.<br>2. Opens dashboard.<br>3. System fetches attendance data.<br>4. Displays records and percentages. |
| **Alternate Flow**  | If connection fails, cached data is shown.                                                                               |
| **Exceptions**      | Missing or corrupted data from backend.                                                                                  |

---

### UC-07 – Submit Assignment / Quiz

| **Item**            | **Details**                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Student                                                                                                                                       |
| **Goal**            | Submit assignments or quizzes online.                                                                                                         |
| **Pre-Conditions**  | The quiz or assignment is published and open for submission.                                                                                  |
| **Post-Conditions** | Submission stored with timestamp and confirmation message.                                                                                    |
| **Main Flow**       | 1. Student opens assigned quiz.<br>2. Completes answers or uploads file.<br>3. Submits response.<br>4. System stores and confirms submission. |
| **Exceptions**      | Late or incomplete submission.                                                                                                                |

---

### UC-08 – View Grades and Progress

| **Item**            | **Details**                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Student                                                                                                                                |
| **Goal**            | View overall course grades, leaderboard, and gamified progress.                                                                        |
| **Pre-Conditions**  | Teacher has graded submissions.                                                                                                        |
| **Post-Conditions** | Dashboard updated with grades and progress indicators.                                                                                 |
| **Main Flow**       | 1. Student logs in.<br>2. Opens progress dashboard.<br>3. System fetches grades and badges.<br>4. Displays results and level progress. |
| **Exceptions**      | No grades available or server fetch error.                                                                                             |

---

### UC-09 – Receive Notifications

| **Item**            | **Details**                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Student                                                                                                                                         |
| **Goal**            | Receive system notifications about grades, new lectures, or upcoming quizzes.                                                                   |
| **Pre-Conditions**  | Student enrolled in courses and notifications enabled.                                                                                          |
| **Post-Conditions** | Notifications displayed in system UI and stored in database.                                                                                    |
| **Main Flow**       | 1. Teacher or system triggers notification.<br>2. System sends message to student dashboard.<br>3. Student views and acknowledges notification. |
| **Exceptions**      | Notification delivery delay or network issue.                                                                                                   |

---

### UC-10 – Access Uploaded Lectures

| **Item**            | **Details**                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Student                                                                                           |
| **Goal**            | Access and download uploaded lecture materials.                                                   |
| **Pre-Conditions**  | Teacher has uploaded materials to the system.                                                     |
| **Post-Conditions** | Lecture successfully accessed or downloaded.                                                      |
| **Main Flow**       | 1. Student logs in.<br>2. Opens course page.<br>3. Selects material.<br>4. Downloads or views it. |
| **Exceptions**      | File missing, access denied, or server error.                                                     |

---

### UC-11 – Generate Attendance Reports

| **Item**            | **Details**                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Registrar                                                                                                              |
| **Goal**            | Generate attendance summaries for courses and departments.                                                             |
| **Pre-Conditions**  | Attendance data is available.                                                                                          |
| **Post-Conditions** | Report generated in PDF or CSV format.                                                                                 |
| **Main Flow**       | 1. Registrar selects course/date.<br>2. System compiles attendance data.<br>3. Generates report.<br>4. Enables export. |
| **Exceptions**      | No data found for selected period.                                                                                     |

---

### UC-12 – Manage Courses

| **Item**            | **Details**                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Registrar                                                                                                     |
| **Goal**            | Create, edit, or remove courses.                                                                              |
| **Pre-Conditions**  | Registrar authenticated.                                                                                      |
| **Post-Conditions** | Course added, updated, or deleted successfully.                                                               |
| **Main Flow**       | 1. Registrar opens Course Management.<br>2. Adds or updates course details.<br>3. System validates and saves. |
| **Exceptions**      | Missing or duplicate course data.                                                                             |

---

### UC-13 – Assign Students and Teachers to Courses

| **Item**            | **Details**                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Registrar                                                                                                         |
| **Goal**            | Assign students and teachers to existing courses.                                                                 |
| **Pre-Conditions**  | Courses and user accounts exist in the system.                                                                    |
| **Post-Conditions** | Assignments saved successfully.                                                                                   |
| **Main Flow**       | 1. Registrar selects a course.<br>2. Chooses teacher and students.<br>3. System validates and stores assignments. |
| **Exceptions**      | User already assigned or not found.                                                                               |

---

### UC-14 – Manage Schedule and Timetables

| **Item**            | **Details**                                                                               |
| ------------------- | ----------------------------------------------------------------------------------------- |
| **Primary Actor**   | Registrar                                                                                 |
| **Goal**            | Define and update class schedules and timetables.                                         |
| **Pre-Conditions**  | Courses exist and have assigned instructors.                                              |
| **Post-Conditions** | Schedule stored and visible to students and teachers.                                     |
| **Main Flow**       | 1. Registrar selects course.<br>2. Defines class time and location.<br>3. Saves schedule. |
| **Exceptions**      | Conflicting schedule detected.                                                            |

---

### UC-15 – Manage Users and Roles

| **Item**            | **Details**                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Admin                                                                                             |
| **Goal**            | Add, edit, and remove users; assign system roles.                                                 |
| **Pre-Conditions**  | Admin logged in with permissions.                                                                 |
| **Post-Conditions** | User accounts and roles updated.                                                                  |
| **Main Flow**       | 1. Admin opens user management.<br>2. Edits or adds users.<br>3. Sets roles.<br>4. Saves changes. |
| **Exceptions**      | Duplicate username or insufficient privileges.                                                    |

---

### UC-16 – Monitor System Logs and Maintenance

| **Item**            | **Details**                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **Primary Actor**   | Admin                                                                                          |
| **Goal**            | Monitor user activities and perform maintenance or backups.                                    |
| **Pre-Conditions**  | Admin has access to system logs.                                                               |
| **Post-Conditions** | Logs reviewed and backups completed.                                                           |
| **Main Flow**       | 1. Admin opens logs panel.<br>2. Reviews user activity.<br>3. Initiates backup or maintenance. |
| **Exceptions**      | Backup failure or access denied.                                                               |

---

## 4. Relationships and Interactions

| **Relationship Type**     | **Description**                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| **<<extend>>**            | “Record Attendance with Face Recognition” extends “Manual Attendance.” |
| **<<include>>**           | “Generate Quiz” includes “Send Request to OpenAI API.”                 |
| **External System Links** | Face Recognition Device provides input; OpenAI API returns quiz data.  |

---

**End of Document**
