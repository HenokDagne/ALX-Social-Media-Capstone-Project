# API Endpoints Documentation

## User Endpoints

### Signup
- **URL:** `/user/signup/`
- **Method:** POST
- **Body:**
  ```json
  {
    "first_name": "string",
    "last_name": "string",
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response:** User data + JWT tokens

### Login
- **URL:** `/user/login/`
- **Method:** POST
- **Body:**
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response:** User data + JWT tokens

### Delete Account
- **URL:** `/user/delete_account/`
- **Method:** DELETE
- **Auth:** Bearer token required
- **Response:** Success message

### Search User
- **URL:** `/user/search_user/?username=<username>`
- **Method:** GET
- **Auth:** Bearer token required
- **Response:** User data

### Profile Retrieve/Update
- **URL:** `/profile/<id>/`
- **Method:** GET, PATCH, PUT
- **Auth:** Bearer token required
- **Response:** Profile data

---

## Post Endpoints

### List/Create Post
- **URL:** `/post/`
- **Method:** GET, POST
- **Auth:** Bearer token required
- **Body (POST):**
  ```json
  {
    "title": "string",
    "content": "string",
    "image": "file (optional)"
  }
  ```
- **Response:** Post data

### Retrieve/Update/Delete Post
- **URL:** `/post/<id>/`
- **Method:** GET, PATCH, PUT, DELETE
- **Auth:** Bearer token required
- **Body (PATCH/PUT):**
  ```json
  {
    "title": "string",
    "content": "string",
    "image": "file (optional)"
  }
  ```
- **Response:** Post data

---

## Comment Endpoints

### List/Create Comment
- **URL:** `/comment/comments/`
- **Method:** GET, POST
- **Auth:** Bearer token required
- **Body (POST):**
  ```json
  {
    "post": <post_id>,
    "content": "string"
  }
  ```
- **Response:** Comment data

### Retrieve/Update/Delete Comment
- **URL:** `/comment/comments/<id>/`
- **Method:** GET, PATCH, PUT, DELETE
- **Auth:** Bearer token required
- **Body (PATCH/PUT):**
  ```json
  {
    "content": "string"
  }
  ```
- **Response:** Comment data

---

## Other Endpoints

### Google Logout
- **URL:** `/user/google_logout/`
- **Method:** GET
- **Auth:** Bearer token required
- **Response:** Redirects to home

### Home
- **URL:** `/user/home/`
- **Method:** GET
- **Response:** Renders home page

---

## Authentication
- All endpoints (except signup/login/home) require JWT Bearer token in the `Authorization` header.
- Example header:
  ```
  Authorization: Bearer <access_token>
  ```

---

## Notes
- Do not send `user` field in POST/PATCH/PUT requests for posts or comments; it is set automatically from the authenticated user.
- For file uploads (images), use `form-data` in Postman.

