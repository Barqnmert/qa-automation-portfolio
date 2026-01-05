# 🐞 BUG-API-02 – API allows content creation when required field `title` is missing

## Summary
API allows content creation even when the required field `title` is missing.
The request should be rejected with 400 Bad Request, but the API returns 201 Created.

## Environment
- API Type: Demo / Mock API
- Tool: Postman
- Endpoint: POST /posts
- API Provider: JSONPlaceholder
- Environment Type: Staging / Demo

## Preconditions
- API endpoint is accessible
- Postman is configured
- No authentication required

## Steps to Reproduce
1. Send a POST request to `/posts`
2. Use the following request body without the required `title` field:
```json
{
  "userId": 1,
  "body": "Test content without title"
}
```
3. Send the request

## Expected Result
- API should reject the request
- Status code should be 400 Bad Request
- Response should indicate missing required field: title
- No content should be created

## Actual Result:
- API returns 201 Created
- Response includes an auto-generated id
- Content is created even though title is missing

## Impact:
- Required field validation is missing
- Invalid or incomplete data can be stored
- Data integrity risk for downstream systems
- Can negatively affect analytics and content moderation workflows

## Priority:
- High

## Status:
- Open

## Regression Test:
- Regression test executed by resending the same request after defect identification.

## Regression Result:
- Fail

## Notes:
- This issue indicates missing server-side validation for required fields.
- The API should enforce schema validation before creating resources.

## Linked Test Case:

- API-TC-06 – Validate content creation with missing required field (title)
