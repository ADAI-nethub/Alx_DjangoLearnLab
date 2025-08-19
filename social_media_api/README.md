## Posts API Endpoints

### Get all posts
`GET /api/posts/`

### Create a post
`POST /api/posts/`
```json
{
    "title": "My First Post",
    "content": "This is my first post on the platform!"
}

{
    "content": "Great post!"
}

## Likes & Notifications

### Like a Post
`POST /api/posts/{id}/like/`
- Requires authentication
- Returns: `{"status": "post liked"}`

### View Notifications  
`GET /api/notifications/`
- Shows all user notifications
- Example response:
```json
[
    {
        "id": 1,
        "actor": "john_doe",
        "verb": "liked your post",
        "target": "1",
        "is_read": false,
        "created_at": "2023-10-01T12:00:00Z"
    }
]