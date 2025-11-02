# 🎯 USE_CASES.md

## 1️⃣ Purpose

The purpose of this document is to describe how different **actors** interact with the **Smart University Ecosystem**.  
Use cases visualize user actions, system responses, and relationships between core functions such as attendance, course management, and reporting.

---

## 2️⃣ Key Actors

| **Actor**                        | **Role / Responsibility**                                              | **Example Tasks**                                            |
| -------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Teacher**                      | Manages attendance, uploads lecture materials, reviews quizzes.        | Open attendance session, upload lecture, view reports.       |
| **Student**                      | Views attendance, takes quizzes, accesses materials.                   | Scan face for attendance, check dashboard, complete quizzes. |
| **Registrar**                    | Handles course enrollment, maintains academic records.                 | Assign students to courses, monitor attendance.              |
| **Admin**                        | Controls user accounts, permissions, and monitoring.                   | Add/remove users, view analytics, ensure security.           |
| **AI Module (System Component)** | Performs automatic tasks such as quiz generation and face recognition. | Analyze lecture files, mark attendance automatically.        |

---

## 3️⃣ Use Case List (Overview)

| **Use Case ID** | **Use Case Name**                       | **Primary Actor(s)** | **Brief Description**                                                  |
| --------------- | --------------------------------------- | -------------------- | ---------------------------------------------------------------------- |
| UC-01           | Record Attendance with Face Recognition | Teacher, Student     | Teacher opens session; students scan faces; system records attendance. |
| UC-02           | Upload Lecture and Generate Quiz        | Teacher, AI Module   | Teacher uploads lecture materials; AI automatically generates a quiz.  |
| UC-03           | View Attendance Dashboard               | Student              | Student views attendance percentage and progress.                      |
| UC-04           | Generate Attendance Reports             | Registrar, Admin     | System generates weekly/monthly attendance reports.                    |
| UC-05           | Manage Users and Roles                  | Admin                | Admin creates and manages user accounts and permissions.               |

---

## 4️⃣ Detailed Use Case Descriptions

### UC-01 – Record Attendance with Face Recognition

| **Item**             | **Details**                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Teacher, Student                                                                                                                                                                   |
| **Goal**             | Automatically record student attendance using face recognition.                                                                                                                    |
| **Pre-Conditions**   | Teacher has created and opened a session; camera and internet available.                                                                                                           |
| **Post-Conditions**  | Attendance record saved with timestamp and confidence score.                                                                                                                       |
| **Main Flow**        | 1. Teacher opens attendance session.<br>2. System activates camera.<br>3. Students scan faces.<br>4. System matches face ≥ 85%.<br>5. Marks student as _Present_ and saves record. |
| **Alternate Flow**   | If recognition fails, teacher manually marks attendance.                                                                                                                           |
| **Exceptions**       | No camera or internet → attendance queued for retry.                                                                                                                               |

---

### UC-02 – Upload Lecture and Generate Quiz

| **Item**             | **Details**                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Teacher, AI Module                                                                                                                                                   |
| **Goal**             | Allow teachers to upload materials and enable AI to generate quizzes.                                                                                                |
| **Pre-Conditions**   | Teacher is logged in and assigned to a course.                                                                                                                       |
| **Post-Conditions**  | Lecture is stored; optional quiz generated.                                                                                                                          |
| **Main Flow**        | 1. Teacher uploads file (PDF, DOCX, PPTX, MP4).<br>2. System validates and stores file.<br>3. AI analyzes content.<br>4. System generates and links quiz to lecture. |
| **Alternate Flow**   | If AI fails → lecture saved without quiz.                                                                                                                            |
| **Exceptions**       | Invalid file format or upload exceeds limit.                                                                                                                         |

---

### UC-03 – View Attendance Dashboard

| **Item**             | **Details**                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Student                                                                                                                     |
| **Goal**             | Allow students to view attendance rate, courses, and notifications.                                                         |
| **Pre-Conditions**   | Student logged in and enrolled in at least one course.                                                                      |
| **Post-Conditions**  | Dashboard displays attendance percentage and latest updates.                                                                |
| **Main Flow**        | 1. Student opens dashboard.<br>2. System fetches attendance records.<br>3. Displays data per course with leaderboard score. |
| **Alternate Flow**   | If data unavailable, system shows “no records found”.                                                                       |
| **Exceptions**       | Database or network error.                                                                                                  |

---

### UC-04 – Generate Attendance Reports

| **Item**             | **Details**                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Registrar, Admin                                                                                                                                                      |
| **Goal**             | Generate attendance reports for selected courses and time periods.                                                                                                    |
| **Pre-Conditions**   | Attendance records exist in the system.                                                                                                                               |
| **Post-Conditions**  | Report generated and available in PDF/CSV format.                                                                                                                     |
| **Main Flow**        | 1. User selects course/date range.<br>2. System retrieves attendance data.<br>3. Aggregates and calculates percentages.<br>4. Generates report for viewing or export. |
| **Alternate Flow**   | If no records found, system displays notification.                                                                                                                    |
| **Exceptions**       | Invalid date range or permission error.                                                                                                                               |

---

### UC-05 – Manage Users and Roles

| **Item**             | **Details**                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Primary Actor(s)** | Admin                                                                                                                                                  |
| **Goal**             | Manage user accounts and assign roles (Teacher, Student, Registrar, Admin).                                                                            |
| **Pre-Conditions**   | Admin authenticated with valid credentials.                                                                                                            |
| **Post-Conditions**  | User account created/updated successfully.                                                                                                             |
| **Main Flow**        | 1. Admin opens user management panel.<br>2. Adds or edits user.<br>3. Assigns role and permissions.<br>4. System saves changes and sends confirmation. |
| **Alternate Flow**   | Admin disables user instead of deleting.                                                                                                               |
| **Exceptions**       | Duplicate username or invalid data.                                                                                                                    |

---

## 5️⃣ Text-Based UML Diagram Representation

```text
             +-------------------+
             |       Admin       |
             +---------+---------+
                       |
                       |  UC-05 Manage Users & Roles
                       |
 +-----------+    +----v----+     +-------------+
 |  Teacher  |--->|  System |<----|  Registrar  |
 +-----------+    +----+----+     +-------------+
      |                ^
      |                |
      |                |  UC-04 Generate Reports
      |                |
      |------> UC-01 Record Attendance
      |------> UC-02 Upload Lecture / Quiz
 +-----------+
 |  Student  |
 +-----------+
      |
      |------> UC-03 View Dashboard
```
