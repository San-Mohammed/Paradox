# Structured Specifications

This document provides detailed specifications for three critical functional requirements of the Smart University Ecosystem. These specifications are intended to guide the development and testing of these features.

---

## 1. FR-002: Digital Attendance System

| | |
| :--- | :--- |
| **Purpose** | To automate the attendance process using face recognition and provide a manual override for teachers. |
| **Inputs** | - Live video stream from a camera in the classroom.<br>- Teacher's manual input for attendance corrections. |
| **Preconditions** | - The teacher is logged into the system and has started a class session.<br>- The system has access to the camera.<br>- Student profiles with face data are registered in the system. |
| **Normal Behavior** | 1. The system captures video from the classroom camera.<br>2. It detects faces in the video stream and compares them against the registered student profiles for the course.<br>3. For each recognized student, the system marks them as 'Present' with a timestamp.<br>4. The teacher can view the real-time attendance on their dashboard.<br>5. The teacher can manually mark students as 'Present', 'Absent', or 'Late'. |
| **Exceptions** | - **Camera not available:** The system notifies the teacher that the camera is not detected and switches to manual attendance mode.<br>- **Poor lighting/obstruction:** If face detection accuracy is low, the system notifies the teacher and suggests manual verification.<br>- **Unregistered student detected:** The system flags the unrecognized face for the teacher's attention. |
| **Side Effects** | - Attendance records are created and stored in the database.<br>- The student's attendance dashboard is updated. |
| **Postconditions** | - The attendance for the class session is accurately recorded.<br>- The attendance data is available for the registrar and students to view. |
| **Constraints** | - The face recognition process should be completed within the first 10-15 minutes of the class.<br>- The system must comply with data privacy regulations regarding the handling of biometric data. |
| **Related UCs** | UC-01, UC-02 |
| **Related NFRs** | NFR-001, NFR-004, NFR-012 |

### Acceptance Criteria (Gherkin Style)

```gherkin
Feature: Digital Attendance System

  Scenario: Successful automatic attendance marking
    Given a teacher is logged in and has started a class session
    And the classroom camera is active
    When the system detects and recognizes a registered student's face
    Then the student's attendance should be marked as 'Present'
    And the attendance status should be visible on the teacher's dashboard

  Scenario: Manual override by the teacher
    Given the attendance for a class session has been recorded
    When the teacher manually changes a student's status from 'Absent' to 'Present'
    Then the student's attendance record should be updated to 'Present'
```

---

## 2. FR-006: Teacher Dashboard

| | |
| :--- | :--- |
| **Purpose** | To provide teachers with a centralized dashboard to manage their courses, including uploading lecture materials and generating AI-powered quizzes. |
| **Inputs** | - PDF files for lecture materials.<br>- Teacher's command to generate a quiz. |
| **Preconditions** | - The teacher is logged into the system.<br>- The teacher is assigned to at least one course. |
| **Normal Behavior** | 1. The teacher navigates to their dashboard.<br>2. They can select a course and upload a PDF lecture file.<br>3. After uploading, the teacher can trigger the AI quiz generation feature.<br>4. The system processes the PDF and generates a set of quiz questions.<br>5. The teacher can review, edit, and publish the quiz to the students. |
| **Exceptions** | - **Invalid file format:** If the uploaded file is not a PDF, the system shows an error message.<br>- **AI service unavailable:** If the quiz generation service is down, the system informs the teacher and suggests trying again later. |
| **Side Effects** | - The uploaded PDF is stored and associated with the course.<br>- The generated quiz is saved in the database. |
| **Postconditions** | - Lecture materials are available for students to access.<br>- A new quiz is created and can be assigned to students. |
| **Constraints** | - The size of the uploaded PDF file should not exceed a specified limit (e.g., 50MB). |
| **Related UCs** | UC-01, UC-03, UC-04 |
| **Related NFRs** | NFR-005, NFR-011 |

### Acceptance Criteria (Gherkin Style)

```gherkin
Feature: Teacher Dashboard

  Scenario: Uploading a lecture PDF
    Given a teacher is on their dashboard
    When they upload a valid PDF file for a course
    Then the file should be visible in the course materials section

  Scenario: Generating a quiz from a PDF
    Given a lecture PDF has been uploaded
    When the teacher clicks the "Generate Quiz" button
    Then a new quiz with AI-generated questions should be created
    And the teacher should be able to review and edit the quiz
```

---

## 3. FR-010: Smart Student Planner

| | |
| :--- | :--- |
| **Purpose** | To provide students with a personalized study planner that includes references, video links, and learning suggestions based on the course materials. |
| **Inputs** | - Uploaded lecture materials (PDFs). |
| **Preconditions** | - The student is logged into the system.<br>- The teacher has uploaded lecture materials for the course. |
| **Normal Behavior** | 1. The student navigates to the Smart Student Planner for a specific course.<br>2. The system analyzes the content of the uploaded lecture materials.<br>3. It generates a list of relevant external resources, such as articles, tutorials, and video links (e.g., from YouTube or Khan Academy).<br>4. The planner may also suggest a study schedule or highlight key topics to focus on. |
| **Exceptions** | - **No materials uploaded:** If no lecture materials are available, the system displays a message indicating that the planner cannot be generated. |
| **Side Effects** | - None. The planner is generated on-demand and is not stored permanently. |
| **Postconditions** | - The student has access to a personalized set of study resources to supplement their learning. |
| **Constraints** | - The external resources should be from reputable and publicly accessible sources. |
| **Related UCs** | Related to UC-03 (as it depends on uploaded lectures) |
| **Related NFRs** | NFR-010, NFR-012 |

### Acceptance Criteria (Gherkin Style)

```gherkin
Feature: Smart Student Planner

  Scenario: Generating a study plan
    Given a student is viewing a course with uploaded lecture materials
    When they open the Smart Student Planner
    Then the system should display a list of relevant video links and articles
    And the suggested resources should be related to the topics in the lecture materials
```
