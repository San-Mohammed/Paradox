# Smart University Ecosystem – Requirements Summary

# Team Members and Roles

| Team Member | Role | Responsibilities |
|-------------|------|-----------------|
| Ramyar Mhamad | Role 1 – Requirements Elicitation Lead | Conduct interviews and brainstorming, collect raw requirements |
| Rewan       | Role 2 – Requirements Classification Specialist | Classify requirements (FR/NFR, User/System) |
| San         | Role 3 – Use Case Modeller | Create actors, use cases, and diagrams |
| San         | Role 4 – Structured Specification Developer | Develop detailed specs for critical FRs |
| Sovin       | Role 5 – Requirements Prioritization Analyst | Prioritize requirements (M/N/S) with justifications |
| Bagzad      | Role 6 – Validation & QA Lead | Perform validation, identify risks, propose mitigation |

---

## Summary of Elicitation Techniques & Questions

**Techniques Used:**  
1. **Interviews** – Conducted with Teachers, Registrar, and Students.   
2. **Brainstorming** – Team session to identify additional potential requirements.  

---

## 🎓 **Interview Documentation – Teacher**

**Interviewer:** Ramyar Mhamad  
**Interviewee:** Dr.kamal  
**Date:** 3/11/2025 
**Role:** Teacher  
**Purpose:** Collect requirements and understand challenges in attendance, learning, and scheduling.

### 🧩 Interview Questions & Responses (Teacher)

**1. Problems in current attendance/scheduling process:**  
- Paper attendance is error-prone (students write names for absent friends).  
- Platforms like Moodle take too long for large/merged classes.  
- Attendance process is time-consuming and sometimes inaccurate.  
- Teachers send attendance to registrar manually; sometimes corrections are needed.  

**2. Features to make attendance easier/faster:**  
- Face recognition, fingerprint, or NFC scanning (face recognition preferred).  
- Manual review/edit before sending to registrar.  

**3. Attendance results reporting:**  
- Clear, automatic summary of present/absent students, unregistered students.  
- Edit attendance before submission.  
- One-click send to registrar.  

**4. Preferred device/platform:**  
- Mobile (in-class attendance) and laptop (review/upload management).  

**5. Security/privacy concerns:**  
- Attendance and face data must remain private.  
- Only authorized teachers and registrars can access records.  

**6. Improvement in current system:**  
- Smart attendance system with face recognition, instant reporting, easy send to registrar.  

**7. Automatic or manual attendance:**  
- Automatic (Face Recognition) preferred.  

**8. Additional tools/features:**  
- Teacher dashboard to upload PDFs.  
- AI-generated quizzes (~50 questions per PDF).  
- Smart student planners with reference books, video links, and personalized learning suggestions.  

### 🧠 Summary of Key Requirements (Teacher)

| Type            | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| Problem         | Manual attendance is time-consuming, inaccurate, and must be sent to registrar manually.     |
| Desired Feature | Automatic face recognition attendance system with review and edit options.                   |
| Data Flow       | Teacher collects attendance → can edit → send to registrar.                                  |
| Devices         | Mobile (for attendance) and laptop (for management & uploads).                               |
| Extra Feature   | AI Dashboard: upload PDFs, auto-generate quizzes, smart study plans.                         |
| Security        | Data privacy and limited access for teachers and registrars only.                            |
| Vision          | One-button system that automates attendance and enhances student learning with AI tools.     |

---

## 🎓 **Interview Documentation – Registrar**

**Interviewer:** Ramyar Mhamad  
**Interviewee:** ms.avan  
**Date:** 4/11/2025  
**Role:** Registrar  
**Purpose:** Understand requirements for course management, student records, and attendance tracking.

### 🧩 Interview Questions & Responses (Registrar)

**1. What are your main responsibilities?**  
- Managing student records, courses, and class schedules.  
- Receiving attendance reports from teachers.  
- Approving changes in attendance or student records.  

**2. How do you currently receive attendance from teachers?**  
- Teachers send via email or manually in spreadsheets.  
- Sometimes data is incomplete or has errors.  

**3. What problems do you face in the current system?**  
- Time-consuming verification of attendance.  
- Errors from manual submissions (missed students, duplicates).  

**4. How would you like attendance submission to work?**  
- Teachers send attendance automatically through the system.  
- Ability to review/edit before final approval.  

**5. What kind of reports or analytics do you need?**  
- Attendance summaries per student, per class, and overall percentages.  
- Notifications for missing or incomplete data.  
- Quick access to course schedules and student progress.  

**6. Device/platform preference:**  
- Mainly laptop, some mobile use for quick checks.  

**7. Security or privacy concerns:**  
- Only authorized staff can access sensitive data.  
- Data encryption and logging for auditing purposes.  

**8. Additional suggestions:**  
- Integration with other university systems.  
- Notifications for teachers when attendance is incomplete.  

### 🧠 Summary of Key Requirements (Registrar)

| Type            | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| Data Flow       | Teachers submit attendance → Registrar reviews → Registrar approves/finalizes records.       |
| Devices         | Laptop (primary), mobile (optional quick access).                                            |
| Reports         | Attendance summaries, student progress, missing data alerts.                                  |
| Security        | Role-based access, encryption, auditing, and logging.                                         |
| Integration     | Support for linking with existing university systems.                                         |

---

## 🎓 **Interview Documentation – Student**

**Interviewer:** Ramyar Mhamad  
**Interviewee:** Hana  
**Date:** 1/11/2024  
**Role:** Student  
**Purpose:** Understand student needs for dashboards, notifications, and learning experience.

### 🧩 Interview Questions & Responses (Student)

**1. What features do you expect from your student dashboard?**  
- View attendance percentage and history.  
- Access to class schedules and upcoming sessions.  
- Notifications about quizzes, assignments, or important updates.  

**2. How do you track your attendance, quizzes, and assignments?**  
- Currently via multiple platforms or manual notes; inconsistent.  

**3. Notifications preference:**  
- Real-time notifications for new quizzes, grades, or attendance issues.  

**4. Preferred device/platform:**  
- Mostly mobile for quick access, laptop for detailed study.  

**5. Additional suggestions:**  
- Smart study planner based on uploaded materials.  
- Gamified progress and points system for motivation.  

### 🧠 Summary of Key Requirements (Student)

| Type            | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| Dashboard       | Attendance tracking, schedules, notifications.                                               |
| Study Tools     | AI-generated smart planner, references, videos.                                              |
| Motivation      | Gamified points, trophies, progress tracking.                                               |
| Devices         | Mobile (primary), laptop (secondary).                                                      |
| Notifications   | Real-time updates for assignments, quizzes, and attendance.                                  |

---

## 3. Role Requirements (Mixed Functional & Non-Functional)

- User login and authentication for students, teachers, registrar, and admins  
- Digital attendance system supporting automatic (face recognition) and manual input  
- Role-based access control (RBAC)  
- Multi-teacher simultaneous attendance management  
- Dashboards: Student, Teacher, Registrar, Admin  
- Upload lecture materials and AI-generated quizzes for students  
- Student planners generated by AI with references, videos, and guidance  
- Gamification: points, trophies, progress tracking  
- Real-time notifications (quizzes, grades, attendance issues)  
- Data security: encryption, audit logs, secure sessions  
- Mobile and desktop responsive interface  
- Search functionality for courses, students, teachers, and records  
- Scheduling system for classes and sessions  
- Reporting system for attendance, quizzes, and leaderboards  
- Logging and monitoring system performance and errors  
- User-friendly and accessible interface  
- Support for future AI integrations and scalability  

---


----------
# The requirements listed above are based on the initial interviews conducted with teachers, registrars, and students. This is part of an ongoing requirements elicitation process, and we plan to conduct additional interviews and data collection to further refine and validate these requirements.

-------

# Smart University Ecosystem – Requirements Classification

## 1. Functional Requirements (FR)

| ID       | Requirement Description                                                                 | Stakeholder |
|----------|-----------------------------------------------------------------------------------------|-------------|
| FR-001   | User login and authentication for students, teachers, registrar, and admins            | All         |
| FR-002   | Digital attendance system supporting automatic (face recognition) and manual input     | Teacher     |
| FR-003   | Multi-teacher simultaneous attendance management                                        | Teacher     |
| FR-004   | Manual override for attendance before sending to registrar                              | Teacher     |
| FR-005   | Student dashboards showing attendance %, schedules, notifications, and progress         | Student     |
| FR-006   | Teacher dashboards for uploading lecture materials and generating AI quizzes            | Teacher     |
| FR-007   | Registrar dashboard for course registration, student record management, and attendance | Registrar   |
| FR-008   | Admin dashboard for managing users, roles, permissions, and monitoring activity        | Admin       |
| FR-009   | Upload lecture materials and AI-generated quizzes for students                          | Teacher     |
| FR-010   | Smart student planner with references, video links, and personalized learning          | Student     |
| FR-011   | Gamified student progress system (points, trophies, progress tracking)                 | Student     |
| FR-012   | Scheduling system for classes, sessions, and exams                                      | Registrar   |
| FR-013   | Search functionality for courses, students, teachers, and records                        | All         |
| FR-014   | Reporting system for attendance, quizzes, and leaderboards                                | Teacher/Registrar |
| FR-015   | Real-time notifications for attendance, quiz updates, and grades                         | All         |

---

## 2. Non-Functional Requirements (NFR)

| ID        | Requirement Description                                                            | Category               |
|-----------|------------------------------------------------------------------------------------|-----------------------|
| NFR-001   | Data encryption for sensitive information (grades, attendance, personal info)      | Security              |
| NFR-002   | Audit logging of all user activities                                              | Security/Traceability |
| NFR-003   | Secure sessions with automatic timeout and logout                                  | Security              |
| NFR-004   | System scalability to handle all students, teachers, and admins                   | Performance           |
| NFR-005   | Mobile and desktop responsive interface                                           | Usability             |
| NFR-006   | Accessibility options for all users                                               | Usability             |
| NFR-007   | Notifications delivered reliably and in real-time                                  | Reliability           |
| NFR-008   | Integration support with existing university systems                               | Portability/Integration |
| NFR-009   | System monitoring and error logging                                               | Reliability/Maintainability |
| NFR-010   | Support for future AI integration and personalized learning features              | Maintainability/Extensibility |
| NFR-011   | User-friendly interface                                                            | Usability             |
| NFR-012   | Performance: quick attendance capture and reporting without delay                 | Performance           |

---

### ✅ Notes on Accuracy:

- Each requirement is **atomic** and **testable**.  
- FR/NFR classification is **unambiguous**.  
- Stakeholders are clearly mapped for traceability.  
- Non-functional requirements are categorized using **Performance, Security, Reliability, Usability, Compliance, Maintainability, Portability** where appropriate.  

---

# Smart University Ecosystem - Requirement Prioritization

This document outlines the prioritized requirements for the Smart University Ecosystem project, categorized using the MoSCoW method (Mandatory, Nice to Have, Superfluous). This prioritization helps in defining the scope for the Minimum Viable Product (MVP) and future development phases.

## Prioritized Requirements List

| Req. No. | Requirement Description | Priority (M/N/S) | Reason |
| :------- | :---------------------- | :--------------- | :----- |
| R1       | Webcam-based face detection (recognition). | M | Core MVP feature; directly solves manual attendance. Browser-based avoids installation. |
| R2       | Face images must be encoded into an irreversible format that cannot be decoded back to the original image | M | Ensures privacy and ethical compliance; avoids legal risks. |
| R3       | Teacher dashboard showing attendance results (TanStack full-stack integration). | M | Central for attendance management and teacher usability. |
| R4       | Accurate attendance marking with target accuracy baseline. | M | Must be accurate enough to replace manual methods. |
| R5       | Webcam face detection during class with timestamp and session metadata. | M | Needed for real-time attendance tracking and auditability. |
| R6       | Teacher ability to correct or override attendance results in dashboard. | M | Reduces risk from false positives/negatives; practical control. |
| R7       | Student and teacher authentication (basic accounts). | M | Core security and access control. |
| R8       | PDF upload by teachers for AI Student Planner. | M | Core feature of the AI Planner. |
| R9       | AI model analyzes PDFs and provides study resources. | M | Adds learning value; central to Student Planner. |
| R10      | English-only interface initially. | M | Limits complexity for MVP delivery. |
| R11      | Logging of attendance events and minimal audit trail (no raw image storage). | M | Supports verification, debugging, and privacy compliance. |
| R12      | Clear consent/opt-out workflow for students. | M | Ethical requirement for responsible AI usage. |
| R13      | Improve face recognition accuracy via research or retraining. | N | Needed long-term to improve reliability. |
| R14      | AI quiz generation from uploaded PDFs. | N | Extends value of the AI planner in later versions. |
| R15      | Permanent storage of face images for audit/training. | S | Conflicts with privacy; avoid for MVP. |
| R16      | High-availability enterprise hosting & SSO integration. | S | Too advanced for student proof-of-concept. |
| R17      | Fancy UI/UX polish beyond usability (animations, advanced themes). | S | Aesthetic only; not needed for core function. |
| R18      | Automated student attendance appeals workflow. | S | Complex process tied to policies; beyond MVP. |
| R19      | User login and authentication for students, teachers, registrar, and admins. | M | Expands R7 for all roles; essential for secure access. |
| R20      | Handle multiple classrooms/teachers using cameras simultaneously. | M | Needed for scalability and real classroom operation. |
| R21      | Manual attendance marking when face recognition fails. | M | Critical fallback ensures continuity. |
| R22      | Role-Based Access Control (RBAC) for users. | M | Security and permission structure for all roles. |
| R23      | Digital attendance automatically updated across dashboards. | M | Central synchronization feature connecting modules. |
| R24      | Attendance verification via camera/AI recognition. | M | Core functional requirement confirming attendance validity. |
| R25      | Student dashboard showing attendance %, schedules, notifications, progress. | M | Required student visibility and engagement. |
| R26      | Teacher dashboard for uploading lectures, generating quizzes, managing attendance. | M | Core teacher-facing feature for teaching flow. |
| R27      | Registrar dashboard for course registration and record management. | M | Required for university record operations. |
| R28      | Admin dashboard for managing users, roles, security, and monitoring. | M | Essential system control and governance. |
| R29      | Gamified student scoring system (points, trophies, progress). | N | Encourages engagement; not critical for MVP. |
| R30      | Real-time notifications (attendance issues, quiz updates, grades). | M | Improves usability and responsiveness. |
| R31      | Secure data handling and encryption for sensitive info. | M | Legal and ethical necessity for user data. |
| R32      | Integration capability with existing university systems. | N | Increases value but requires later permissions. |
| R33      | Mobile and desktop responsive design. | M | Ensures accessibility and usability on all devices. |
| R34      | Session management (active user control, timeouts). | M | Security and resource management requirement. |
| R35      | Password reset and account recovery system. | M | Core user experience and security requirement. |
| R36      | Logging and auditing of user activities. | M | Needed for transparency and system oversight. |
| R37      | Support uploading and accessing lecture materials/documents. | M | Academic requirement; supports teaching process. |
| R38      | Quiz and assignment management with automated grading. | N | Added value; AI-enhanced extension. |
| R39      | Search functionality for courses, teachers, and students. | M | Improves navigation and user productivity. |
| R40      | Scheduling system for classes and sessions. | M | Core academic management functionality. |
| R41      | Reporting system for attendance, quizzes, leaderboards. | M | Required for analytics and tracking performance. |
| R42      | Notification system via email or system messages. | M | Ensures users are informed and engaged. |
| R43      | User-friendly interface with accessibility options. | M | Required for usability and inclusion. |
| R44      | Future AI integration for recommendations/personalized learning. | N | Long-term AI enhancement for adaptive learning. |
| R45      | Scalability to support full university population. | N | Important for production phase, not MVP. |
| R46      | Secure login sessions with timeout and auto logout. | M | Prevents unauthorized access. |
| R47      | System performance logging and error monitoring. | M | Essential for maintenance and reliability. |

## Summary of Prioritization

*   **Mandatory (M):** 36 requirements
*   **Nice to Have (N):** 7 requirements
*   **Superfluous (S):** 4 requirements