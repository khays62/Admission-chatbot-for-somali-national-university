# API Contract V1

Ujeeddo: Qeexitaanka endpoint-yada chatbot-ka, request/response format, iyo session lifecycle.

## Base URL
```
http://localhost:5000/api/chat
```

## Endpoint 1: POST /api/chat/message

Ujeeddo: Qofka user-ka u soo gudbiya message, chatbot-ku u soo celiya jawaab.

### Request
```json
{
  "user_id": "string (session-based)",
  "message": "string (user input)",
  "session_token": "string (optional, for resuming session)"
}
```

### Response (200 OK)
```json
{
  "success": true,
  "chatbot_response": "string (Somali)",
  "intent": "string (intent detected)",
  "response_type": "faq_response|redirect|out_of_scope|greeting",
  "session_token": "string (new or existing)",
  "next_actions": ["suggested_buttons"]
}
```

### Response (400 Bad Request)
```json
{
  "success": false,
  "error": "Message required or empty"
}
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "message": "Sideen isku diiwaan gelin karaa?"
  }'
```

## Endpoint 2: POST /api/chat/session/start

Ujeeddo: Dhaladhaa session cusub haddii kuma jiro.

### Request
```json
{
  "user_id": "string"
}
```

### Response (200 OK)
```json
{
  "success": true,
  "session_token": "string",
  "session_created_at": "ISO 8601 timestamp",
  "session_expires_at": "ISO 8601 timestamp (24 hours from now)"
}
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/chat/session/start \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user123"}'
```

## Endpoint 3: GET /api/chat/session/state

Ujeeddo: Hel xaaladda session-ka hadda.

### Request
```
GET /api/chat/session/state?session_token=abc123
```

### Response (200 OK)
```json
{
  "success": true,
  "session_token": "string",
  "user_id": "string",
  "session_state": {
    "started_at": "ISO 8601 timestamp",
    "last_message_at": "ISO 8601 timestamp",
    "message_count": 5,
    "is_active": true
  },
  "expires_at": "ISO 8601 timestamp"
}
```

## Endpoint 4: POST /api/chat/session/reset

Ujeeddo: Dib u dhig session (clear chat history).

### Request
```json
{
  "session_token": "string"
}
```

### Response (200 OK)
```json
{
  "success": true,
  "message": "Session cleared. New session token issued.",
  "session_token": "string (new)"
}
```

## Endpoint 5: GET /api/knowledge

Ujeedpo: Hel full knowledge base (admin ama frontend debug).

### Request
```
GET /api/knowledge?format=json
```

### Response (200 OK)
```json
{
  "success": true,
  "version": "v1",
  "knowledge_items": [...],
  "faq_count": 22,
  "intents_count": 11
}
```

## Session Lifecycle

1. User wuxuu ka billaabaa: chatbot home page
2. Backend-ku waxa uu sameeyaa: session cusub + token
3. User waxa uu gadaysaa: message
4. Backend-ku waxa uu sameeyaa: detect intent, match FAQ, generate response
5. User waxa uu helay: jawaab + suggestions
6. Haddii session expire: user waa in uu dhaladhaa cusub

## Error Handling

Midka kasta oo errors:

### 400 Bad Request
```json
{
  "success": false,
  "error": "Message required or too long",
  "code": "INVALID_MESSAGE"
}
```

### 401 Unauthorized
```json
{
  "success": false,
  "error": "Session token expired or invalid",
  "code": "SESSION_EXPIRED"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Internal server error",
  "code": "SERVER_ERROR"
}
```

## Data Types

- `user_id`: string (min 3, max 50 characters)
- `message`: string (min 1, max 1000 characters)
- `session_token`: string (UUID or similar)
- `timestamp`: ISO 8601 format
- `intent`: one of [salaam, codsi_isdiiwaan_gelin, shuruudo_gelitaan, ...]

## Rate Limiting

- 100 requests / minute per user_id
- 429 Too Many Requests haddii uu dhaafay

## CORS

- Allow frontend origin (will be configured in Flask)

