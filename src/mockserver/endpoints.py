
ENDPOINTS = [
    ("/url1", "Response from /url1", 200),
    ("/url2", "Response from /url2", 201),
    ("/url3", "Response from /url3", 202),
    ("/url4", "Response from /url4", 203),
    ("/url5", "Response from /url5", 204, ("GET", "POST")),
    ("/get_profile", {"id": 123, "username": "django"}, 200),
    ("/test/<test_var>", "Test", 200),
    ("/test_headers", "Test", 200, ("GET",), {"x-header": "true"}),
    ("/404", "not found", 404),
]
