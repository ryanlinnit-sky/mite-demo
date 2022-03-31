# Endpoints are formatted in a tuple with the following values:
# (url, response, status_code, methods, headers)

ENDPOINTS = [
    ("/url1", "Response from /url1", 200, ("GET", "DELETE")),
    ("/url2", "Response from /url2", 201),
    ("/url3", "Response from /url3", 202),
    ("/url4", "Response from /url4", 203),
    ("/url5", "Response from /url5", 204, ("GET", "POST")),
    ("/get_profile/<user_id>", {"id": "{user_id}", "username": "django"}, 200),
    ("/test/<test_var>", "Test", 200),
    ("/test_headers", "Test", 200, ("GET",), {"x-header": "true"}),
    ("/404", "not found", 404),
]
