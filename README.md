# QA Automation Portfolio

This repository showcases my hands-on QA experience covering **manual testing, API testing, and web automation**, structured as a real-life QA workflow.

The portfolio demonstrates how test cases, defects, and automation are connected across tools such as **Postman, Jira, Selenium, and GitHub**.

---

## 🔹 Mini QA Project – Content Review System

**Domain:** Social Media / Content Moderation  
**Goal:** Validate content review logic, KPI accuracy, and API-level validations using a QA mindset.

This project simulates a real content review platform where reviewers classify content based on guidelines and track performance metrics.

---

## 🧪 Testing Scope

### Manual QA
- Test case design for guideline compliance
- KPI accuracy and regression scenarios
- Improvement vs bug analysis
- Jira-based defect reporting and traceability

### API Testing (Postman)
- Positive & negative API scenarios
- Validation of required fields
- Status code and response body assertions
- Bug identification via failing assertions

📁 See: `api-tests/`

---

### Web Automation (Selenium + Pytest)
- Login positive & negative scenarios
- Suite-based execution
- Pytest framework usage
- Basic automation structure and reporting

📁 See: `selenium/`

---

## 🐞 Bug Tracking & QA Workflow

- Bugs documented using Jira-style format
- Clear separation of:
  - Test Case (Task)
  - Defect (Bug)
  - Improvement suggestions
- Regression test logic applied after bug identification

📁 See: `bug-reports/`

---

## 🛠️ Tools & Technologies

- **Postman** – API testing & assertions  
- **Jira** – Bug tracking & test traceability  
- **Selenium (Python)** – Web automation  
- **Pytest** – Test execution framework  
- **GitHub** – Version control & documentation  

---

## 🎯 Key Learnings

- Writing effective negative and regression test cases
- Understanding when an issue is a bug vs an improvement
- Connecting API test failures to Jira defects
- Building a structured QA portfolio suitable for real-world projects

---

## 🔗 Jira Integration & QA Traceability

This repository follows a **real-world QA workflow** using **Jira** for test case management, defect tracking, regression testing, and improvement proposals.

The project demonstrates how **manual testing, API testing, and defect lifecycle management** are handled together in a professional QA process.

---

### 🧪 Jira Project Overview

- **Project Name:** Mini QA Project – Content Review
- **Tool:** Jira (Atlassian)
- **Testing Types Covered:**
  - Manual Testing
  - API Testing (Postman)
  - Negative & Positive Scenarios
  - Regression Testing
  - Improvement Analysis

---

### 📋 Test Cases Implemented

#### Manual Test Cases
- **TC-01** – Validate guideline compliance classification  
- **TC-02** – Validate KPI accuracy calculation  
- **TC-03** – Validate guideline update regression behavior  

#### API Test Cases (Postman)
- **API-TC-04** – Validate content creation with empty request body (negative)
- **API-TC-06** – Validate content creation when required field (title) is missing

---

### 🐞 Bug Reports

The following defects were identified during testing and logged in Jira:

- **BUG-01** – Incorrect content classification after guideline update
- **BUG-API-01** – API allows content creation with empty request body
- **BUG-API-02** – API allows content creation when required field (title) is missing

Each bug includes:
- Clear reproduction steps
- Expected vs Actual results
- Impact analysis
- Priority & severity assessment

---

### 🔄 Regression Testing

Regression tests were executed after identifying defects to verify system stability.

- Manual and API regression tests confirm that validation issues still persist.
- Failed regression results indicate **missing backend validation logic**.

---

### 💡 Improvement Proposals

Not all findings were classified as bugs. The following improvements were proposed:

- **IM-01** – Improve guideline version visibility during content review
- **IM-02** – Improve KPI dashboard loading speed and add loading indicator

---

### 🔁 QA Traceability Flow


