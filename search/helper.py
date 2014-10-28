def business_search(tag_name):
	""" checks if the tag is business related or not """
	fields = ["business", "sales", "marketing", "manage", "advertising"]
	for field in fields:
		if field in tag_name:
			print field
			return True
	return False

def location_search(location, tag_name):
	location = location.lower()
	tag_name = tag_name.lower()
	return location in tag_name

def resume_parser(resume_file):
	pass
