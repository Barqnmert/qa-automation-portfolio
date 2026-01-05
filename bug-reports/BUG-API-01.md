# BUG-API-01 – API allows content creation with empty request body

## Environment
- API: JSONPlaceholder (Demo API)
- Tool: Postman
- Endpoint: POST /posts

## Preconditions
- API endpoint is accessible
- Postman is configured

## Steps to Reproduce
1. Send POST request to `/posts`
2. Use empty JSON body: `{ }`
3. Send the request

## Expected Result
- API should reject the request
- Status code should be **400 Bad Request**
- Content should not be created

## Actual Result
- API returns **201 Created**
- Content is created even though request body is empty

## Impact
- Missing backend validation
- Invalid data can be persisted

## Priority
- High

## Status
- Open
## Regression Test

Regression test was executed after identifying the defect.

- Same request was re-sent using Postman
- API behavior remained unchanged
- Validation issue still persists

## Regression Result
- ❌ Fail

## Status
- Open


