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
