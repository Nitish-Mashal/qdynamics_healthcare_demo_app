def get_website_user_home_page(user):
	"""Serve the public Healthcare landing page to guests only."""
	if user == "Guest":
		return "index"
	return None
