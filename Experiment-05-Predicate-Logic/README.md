# Experiment 05 - Predicate Logic

## Decision Support Systems Lab

### Experiment Title

Implement Predicate Logic Using Python for Knowledge Representation

### Aim

To implement Predicate Logic using Python for knowledge representation and decision-making in a student academic Decision Support System.

### Problem Statement

A student academic Decision Support System is developed using Predicate Logic.

The system stores student information related to attendance and academic performance and applies logical inference rules to determine:

- Students requiring academic support
- Students eligible for progression
- Students not recommended for immediate progression

### Knowledge Base

The main predicates used in the experiment are:

- Student(x)
- HighAttendance(x)
- LowAttendance(x)
- GoodPerformance(x)
- LowPerformance(x)

### Inference Rules

1. LowAttendance(x) → NeedsSupport(x)
2. LowPerformance(x) → NeedsSupport(x)
3. HighAttendance(x) AND GoodPerformance(x) → Eligible(x)
4. NeedsSupport(x) → NotRecommended(x)

### Algorithm

1. Define students as constants.
2. Define predicates for attendance and performance.
3. Store known facts in the knowledge base.
4. Define logical inference rules.
5. Check each student's attendance.
6. Check each student's academic performance.
7. Infer NeedsSupport() when low attendance or low performance is detected.
8. Infer Eligible() when both attendance and performance are satisfactory.
9. Infer NotRecommended() for students requiring support.
10. Display the inferred decisions.

### Assignment

The student academic DSS is extended by introducing the following predicates:

- CompletedCourses(x)
- AttendanceAbove75(x)
- HasBacklog(x)
- GoodPerformance(x)
- EligibleForScholarship(x)

The assignment develops Predicate Logic rules to determine scholarship eligibility.

The system should:

1. Add at least 10 students to the knowledge base.
2. Define at least five predicates.
3. Define at least four inference rules.
4. Implement the rules using Python.
5. Query the system for scholarship eligibility.
6. Display the inferred results.
7. Explain how Predicate Logic can be used to develop a knowledge-based DSS.

### Files

- `predicate_logic.py` - Main Experiment 5 program.
- `student_academic_dss.py` - Assignment implementation.

### Technologies Used

- Python
- Predicate Logic
- Knowledge Representation

### Result

The Predicate Logic-based knowledge representation system was successfully implemented using Python. The system stores student facts, applies inference rules, and produces academic decision results.