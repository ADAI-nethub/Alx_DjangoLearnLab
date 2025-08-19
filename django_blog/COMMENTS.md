# Comment System Documentation

## Features
- Authenticated users can post comments on blog posts
- Comment authors can edit or delete their comments
- Comments are displayed with the post they belong to

## Implementation Details

### Models
- `Comment` model with relations to `Post` and `User`
- Timestamps for creation and updates

### Views
- `post_detail`: Shows post and handles comment creation
- `comment_edit`: Handles comment editing (author only)
- `comment_delete`: Handles comment deletion (author only)

### Templates
- Integrated with existing post detail view
- Separate templates for edit/delete confirmation

### URLs
- Nested under post URLs for logical structure