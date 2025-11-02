## 🎯 Objective

To identify the main actors and develop formal use cases that describe how users and external systems interact with the **Smart University Ecosystem** — an integrated LMS platform with AI-based face recognition attendance and AI quiz generation.

![use case](/Paradox/assets//usecase.jpg)

---

## 1. Key Actors

| **Actor**                               | **Type**        | **Description**                                                                         |
| --------------------------------------- | --------------- | --------------------------------------------------------------------------------------- |
| **Teacher**                             | Human           | Controls attendance sessions, uploads lectures, and generates quizzes.                  |
| **Student**                             | Human           | Views attendance, submits assignments/quizzes, and checks grades.                       |
| **Registrar**                           | Human           | Manages courses, assigns users, and generates attendance reports.                       |
| **Admin**                               | Human           | Manages system users, roles, and monitors platform activity.                            |
| **Face Recognition Device (AI Camera)** | External System | Detects and sends facial data to the system when a teacher opens an attendance session. |
| **Quiz Generator API (OpenAI)**         | External System | Generates quiz questions based on lecture materials when requested by the teacher.      |

---

## 2. Use Case List

| **Use Case ID** | **Use Case Name**                       | **Primary Actor(s)** | **Supporting Actor(s)**      |
| --------------- | --------------------------------------- | -------------------- | ---------------------------- |
| UC-01           | Record Attendance with Face Recognition | Teacher              | Face Recognition Device (AI) |
| UC-02           | Manual Attendance                       | Teacher              | —                            |
| UC-03           | Upload Lecture                          | Teacher              | —                            |
| UC-04           | Generate Quiz                           | Teacher              | Quiz Generator API (OpenAI)  |
| UC-05           | View Attendance Dashboard               | Student              | —                            |
| UC-06           | Submit Assignment/Quiz                  | Student              | —                            |
| UC-07           | Generate Attendance Reports             | Registrar            | —                            |
| UC-08           | Manage Users and Roles                  | Admin                | —                            |
| UC-09           | Course Making                           | Registrar            | —                            |
| UC-10           | Assign Students and Teachers to Courses | Registrar            | —                            |

---

## 3. Detailed Use Case Descriptions

---

### UC-01 – Record Attendance with Face Recognition

| **Item**                | **Details**                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)**    | Teacher                                                                                                                                                                                                          |
| **Supporting Actor(s)** | Face Recognition Device (AI)                                                                                                                                                                                     |
| **Goal**                | Automatically record student attendance through AI facial recognition.                                                                                                                                           |
| **Pre-Conditions**      | Teacher is logged in and has created a class session; camera device is connected.                                                                                                                                |
| **Post-Conditions**     | Attendance records saved with timestamps and confidence scores.                                                                                                                                                  |
| **Main Flow**           | 1. Teacher opens an attendance session.<br>2. System activates the face recognition device.<br>3. Students’ faces are scanned.<br>4. The system validates matches (≥85%).<br>5. Attendance stored automatically. |
| **Alternate Flow**      | AI fails to detect some faces → teacher manually marks them.                                                                                                                                                     |
| **Exceptions**          | Camera disconnected or network error.                                                                                                                                                                            |
| **Relationship**        | <<extend>> UC-02 Manual Attendance                                                                                                                                                                               |

---

### UC-02 – Manual Attendance

| **Item**             | **Details**                                                                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Teacher                                                                                                                |
| **Goal**             | Allow the teacher to manually mark attendance if AI recognition fails.                                                 |
| **Pre-Conditions**   | An active attendance session exists.                                                                                   |
| **Post-Conditions**  | Attendance records updated manually.                                                                                   |
| **Main Flow**        | 1. Teacher opens manual attendance form.<br>2. Selects absent/present students.<br>3. System updates attendance table. |
| **Exceptions**       | Unauthorized access or invalid session.                                                                                |

---

### UC-03 – Upload Lecture

| **Item**             | **Details**                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Primary Actor(s)** | Teacher                                                                                                            |
| **Goal**             | Allow teachers to upload lecture files (PDF, DOCX, PPTX, MP4).                                                     |
| **Pre-Conditions**   | Teacher is authenticated and assigned to a course.                                                                 |
| **Post-Conditions**  | Lecture materials stored in the system.                                                                            |
| **Main Flow**        | 1. Teacher uploads lecture file.<br>2. System validates and stores the file.<br>3. Confirmation message displayed. |
| **Exceptions**       | Invalid file format or upload failure.                                                                             |

---

### UC-04 – Generate Quiz

| **Item**                | **Details**                                                                                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)**    | Teacher                                                                                                                                                                                   |
| **Supporting Actor(s)** | Quiz Generator API (OpenAI)                                                                                                                                                               |
| **Goal**                | Generate quizzes automatically using OpenAI API based on uploaded lecture material.                                                                                                       |
| **Pre-Conditions**      | At least one lecture has been uploaded.                                                                                                                                                   |
| **Post-Conditions**     | Quiz generated and linked to the course.                                                                                                                                                  |
| **Main Flow**           | 1. Teacher selects a lecture.<br>2. Chooses “Generate Quiz.”<br>3. System sends request to OpenAI API.<br>4. API returns questions and answers.<br>5. System saves and displays the quiz. |
| **Exceptions**          | API rate limit exceeded or no internet connection.                                                                                                                                        |

---

### UC-05 – View Attendance Dashboard

| **Item**             | **Details**                                                                                   |
| -------------------- | --------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Student                                                                                       |
| **Goal**             | Display attendance records and course progress to the student.                                |
| **Pre-Conditions**   | Student logged in and enrolled in courses.                                                    |
| **Post-Conditions**  | Attendance percentage and alerts displayed.                                                   |
| **Main Flow**        | 1. Student opens dashboard.<br>2. System retrieves records.<br>3. Attendance chart displayed. |
| **Exceptions**       | Missing or corrupted attendance data.                                                         |

---

### UC-06 – Submit Assignment/Quiz

| **Item**             | **Details**                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Student                                                                                                                       |
| **Goal**             | Allow students to submit assignments or answer quizzes.                                                                       |
| **Pre-Conditions**   | Assignment/quiz available in the student’s course.                                                                            |
| **Post-Conditions**  | Submission recorded and stored.                                                                                               |
| **Main Flow**        | 1. Student opens quiz/assignment.<br>2. Uploads answers or submits responses.<br>3. System records submission with timestamp. |
| **Exceptions**       | Late submission or network failure.                                                                                           |

---

### UC-07 – Generate Attendance Reports

| **Item**             | **Details**                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Registrar                                                                                                                                    |
| **Goal**             | Generate attendance and participation reports for departments or courses.                                                                    |
| **Pre-Conditions**   | Attendance data exists in the system.                                                                                                        |
| **Post-Conditions**  | Report generated and downloadable (PDF/CSV).                                                                                                 |
| **Main Flow**        | 1. Registrar selects course/date range.<br>2. System fetches data.<br>3. Calculates attendance percentage.<br>4. Displays report for export. |
| **Exceptions**       | No data found for selected range.                                                                                                            |

---

### UC-08 – Manage Users and Roles

| **Item**             | **Details**                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Admin                                                                                                             |
| **Goal**             | Manage user accounts and assign roles (Teacher, Student, Registrar, Admin).                                       |
| **Pre-Conditions**   | Admin logged in with valid credentials.                                                                           |
| **Post-Conditions**  | User accounts updated successfully.                                                                               |
| **Main Flow**        | 1. Admin opens user management panel.<br>2. Adds/edits users.<br>3. Assigns roles.<br>4. System confirms changes. |
| **Exceptions**       | Duplicate username or invalid input.                                                                              |

---

### UC-09 – Course Making

| **Item**             | **Details**                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Registrar                                                                                               |
| **Goal**             | Create new courses in the system.                                                                       |
| **Pre-Conditions**   | Registrar authenticated.                                                                                |
| **Post-Conditions**  | Course added to catalog.                                                                                |
| **Main Flow**        | 1. Registrar clicks “Add Course.”<br>2. Fills in course details.<br>3. System saves course to database. |
| **Exceptions**       | Missing or duplicate course name.                                                                       |

---

### UC-10 – Assign Students and Teachers to Courses

| **Item**             | **Details**                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Primary Actor(s)** | Registrar                                                                                                   |
| **Goal**             | Assign students and teachers to specific courses.                                                           |
| **Pre-Conditions**   | Courses and users exist in the database.                                                                    |
| **Post-Conditions**  | Assignments saved successfully.                                                                             |
| **Main Flow**        | 1. Registrar selects a course.<br>2. Adds teacher and enrolled students.<br>3. System confirms assignments. |
| **Exceptions**       | User not found or already assigned.                                                                         |

---

## 4. Use Case Diagram Summary

**System Name:** Smart University Ecosystem

### Actors

- Teacher
- Student
- Registrar
- Admin
- Face Recognition Device (AI Camera)
- Quiz Generator API (OpenAI)

### Includes and Extends

- **UC-01** _Record Attendance with Face Recognition_ <<extend>> _UC-02 Manual Attendance_
- **UC-04** _Generate Quiz_ interacts with _Quiz Generator API (OpenAI)_

---

## 5. Summary Explanation

The **Smart University Ecosystem** integrates human actors and external systems to automate university operations.  
Teachers and devices collaborate in attendance marking, while OpenAI’s API assists with quiz creation.  
Students interact for learning and submission purposes, and administrators manage structure and security.  
This design ensures realistic modeling of both **human** and **system-level** interactions using standard UML practices.

---

**End of Document**
