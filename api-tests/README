# API Tests (Postman) – Mini QA Project: Content Review

## Scope
This folder contains Postman API tests simulating a Content Review system validation mindset.

## Tools
- Postman (collections + assertions)
- Jira (defects & traceability)

## How to Run
1. Import the collection:
   `api-tests/postman/Mini_QA_Project_Content_Review.postman_collection.json`
2. Run requests individually or via Collection Runner.

## Test Cases
### API-TC-06 Validate content creation with missing required field (title)
**Goal:** Verify API rejects requests missing required fields.  
**Expected:** 400 Bad Request + validation message  
**Actual (JSONPlaceholder):** 201 Created → indicates missing validation

## Defects
- **BUG-API-01**: API allows content creation when required field (title) is missing (should reject with 400)
