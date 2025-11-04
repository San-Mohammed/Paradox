# REQUIREMENTS.md

## 1. Requirements Elicitation Process

### Elicitation Techniques Used
For this project, we used **two elicitation techniques**:
1. **Interviews**
2. **Brainstorming Session**

---

## 2. Interview Process

### Purpose
The goal of the interviews was to collect real information about how university staff and students currently work, what problems they face, and what features they need in the new **Smart University Ecosystem (SRS)** system.

### Participants
We interviewed the following stakeholders:
- **1 Registrar Staff Member**
- **1 Teacher**
- **1 Admin Staff Member**
- **1 Student (our team representative)**

### Interview Details

#### A. Teacher Interview
We first interviewed one of the teachers.  
We asked:
- How do you take student attendance?
- How do you share this attendance with the registrar?
- What problems do you face in this process?
- What features would you like to see in a new system?

**Key Findings:**
- Teachers currently take attendance manually in the classroom by calling students’ names and marking “yes” or “no”.  
- After class, they send this attendance manually to the registrar’s office.  
- Teachers mentioned that this process is slow and can lead to errors or missing records.  
- Teachers want a **digital attendance system** that automatically stores and sends attendance to the registrar.  
- They also want to **upload lecture materials** and have an **easier grading system**.

---

#### B. Registrar Interview
After talking to the teacher, we interviewed one **registrar staff member**.  
We asked:
- How do you collect attendance from teachers?
- What problems do you face when working manually?
- What new features do you want to make your work easier?

**Key Findings:**
- The registrar currently receives attendance sheets manually from teachers.  
- This causes **mistakes**, **missing data**, and **time delays**.  
- The registrar needs a system that automatically collects attendance and updates student records in real time.  
- They also want to manage course registration, grades, and schedules in one platform.

---

#### C. Admin Staff Interview
We then talked with an **admin staff member** who manages both teachers and registrars.  
We asked:
- How do you manage user access and permissions?
- What problems do you face when coordinating between departments?
- What do you need from the new system?

**Key Findings:**
- The admin manually manages user accounts and permissions, which takes time.  
- They want an **automatic user management system** that allows easy role assignment (student, teacher, registrar, admin).  
- They also want tools to **monitor activities** and ensure data security.

---

#### D. Student Interview
Finally, we interviewed one **student (from our team)** to represent the student users.  
We asked:
- What features would make the system more useful for you?
- How do you want to access the system (mobile or desktop)?
- What problems do you face with the current system?

**Key Findings:**
- Students want a **simple and modern dashboard** to see grades, attendance, announcements, and schedules.  
- They want a **gamified experience** — for example, a scoring or progress system that motivates them.  
- They also want to easily access uploaded lecture materials and reminders for upcoming tasks.

---

## 3. Brainstorming Session

### Purpose
After finishing all interviews, our team held a brainstorming session to combine all collected ideas and find the most important requirements for our Smart University Ecosystem system.

### Session Details
- **Date:** October 30, 2025  
- **Participants:** All 5 team members  
- **Facilitator:** Requirements Elicitation Lead  
- **Duration:** 1 hour

### Process
1. We reviewed all interview results (teacher, registrar, admin, and student).  
2. We listed all problems, ideas, and features on a shared document.  
3. We grouped them into four categories: Student, Teacher, Registrar, and Admin.  
4. We discussed which features were essential for version 1 of the system.  
5. We finalized the list of functional and non-functional requirements.

### Key Discussion Points
- Automate attendance process between teachers and registrar  
- Add grade and lecture upload system for teachers  
- Add student dashboard with gamified progress  
- Add admin management for roles and permissions  
- Make the system responsive for desktop and mobile users  

---

---


## 4. Raw Requirements List

- User login and authentication for students, teachers, registrar, and admins
- We want the system to handle several teachers taking attendance at the same time,  cameras in different classes, without any problem
- The system shall allow teachers to manually record student attendance in case the face recognition system is unavailable or inaccurate.
- Role-based access control (RBAC) for different users  
- Digital attendance system (teachers mark attendance, automatically updated for registrar and student dashboards)  
- Attendance verification using camera or facial recognition AI based 
- Student dashboards showing percentage rate attendance, schedules, notifications, and progress  
- Teacher dashboards for uploading lecture materials, automaticly generate quizzes base on the lectures , and attendance management  
- Registrar dashboard for course registration, student record management, and attendance tracking  
- Admin dashboard for managing users, roles, permissions, monitoring system activity, and security blocking users
- Gamified student scoring system (points, trophy, progress tracking)  
- Real-time notifications (e.g., for quizze update , quize grades, attendance issues)  
- Secure data for sensitive data  
- Ability to integrate with existing university systems if needed  
- Mobile and desktop responsive interface  
- Session management for active users  
- Password reset and account recovery system  
- Data encryption for sensitive information (grades, attendance, personal info)  
- Logging of all user activities for auditing   
- Support for uploading, storing, and accessing lecture files and documents  
- Camera integration for face detection for attendance or verification  
- Quiz and assignment management with automated grading  
- Search functionality for courses, students, teachers, and records  
- Scheduling system for classes, and sessions  
- Reporting system for attendance , and quizes leader board  
- Notification system for alerts via email or system messages    
- User-friendly interface with accessibility options  
- Support for future AI integration for recommendations and personalized learning  
- Scalability to handle all students, teachers, and admin staff in the university  
- Secure login sessions with timeout and automatic logout  
- Logging and monitoring for system performance and errors  

---
## 5. Summary
By using **interviews** and a **team brainstorming session**, we gathered realistic and detailed requirements for the **Smart University Ecosystem (SRS)**.  
The process gave us a deep understanding of how the current manual system works and what improvements users want.  
This documentation provides a strong foundation for the next steps — **system design and development**.



