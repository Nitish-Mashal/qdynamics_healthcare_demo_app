app_name = "qdynamics_healthcare_demo_app"
app_title = "Qdynamics Healthcare Demo App"
app_publisher = "Nitish"
app_description = "Demo landing and login page for healthcare modulke"
app_email = "nitish.m@quantumberg.com"
app_license = "mit"

# Guests see the Vue landing page at `/`; logged-in users retain Frappe's
# normal home-page resolution.
get_website_user_home_page = ["qdynamics_healthcare_demo_app.website.get_website_user_home_page"]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "qdynamics_healthcare_demo_app",
# 		"logo": "/assets/qdynamics_healthcare_demo_app/logo.png",
# 		"title": "Qdynamics Healthcare Demo App",
# 		"route": "/qdynamics_healthcare_demo_app",
# 		"has_permission": "qdynamics_healthcare_demo_app.api.permission.has_app_permission",
# 	}
# ]

# The dock, the rail down the left of the desk, is a document rather than a hook. Author it in
# Manage Dock on a developer-mode site and press Export to App, and it is written to
# `qdynamics_healthcare_demo_app/dock/qdynamics_healthcare_demo_app/qdynamics_healthcare_demo_app.json` for git to carry. An app that ships none has no
# rail: its sidebar gets a switcher in the header instead.
#
# A companion app, one that extends a host app rather than standing on its own, says so with
# `mount_on` on that same record, and its entries are appended to the host's rail. Mounting keeps
# the companion off the apps screen, so it takes precedence over any add_to_apps_screen above.

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qdynamics_healthcare_demo_app/css/qdynamics_healthcare_demo_app.css"
# app_include_js = "/assets/qdynamics_healthcare_demo_app/js/qdynamics_healthcare_demo_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/qdynamics_healthcare_demo_app/css/qdynamics_healthcare_demo_app.css"
# web_include_js = "/assets/qdynamics_healthcare_demo_app/js/qdynamics_healthcare_demo_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qdynamics_healthcare_demo_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_kanban_js = {"doctype" : "public/js/doctype_kanban.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "qdynamics_healthcare_demo_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "qdynamics_healthcare_demo_app.utils.jinja_methods",
# 	"filters": "qdynamics_healthcare_demo_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qdynamics_healthcare_demo_app.install.before_install"
# after_install = "qdynamics_healthcare_demo_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qdynamics_healthcare_demo_app.uninstall.before_uninstall"
# after_uninstall = "qdynamics_healthcare_demo_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qdynamics_healthcare_demo_app.utils.before_app_install"
# after_app_install = "qdynamics_healthcare_demo_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qdynamics_healthcare_demo_app.utils.before_app_uninstall"
# after_app_uninstall = "qdynamics_healthcare_demo_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "qdynamics_healthcare_demo_app.build.after_build"

# To hook into the build process of other apps
# The list of apps being built is passed as an argument

# after_app_build = "qdynamics_healthcare_demo_app.build.after_app_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qdynamics_healthcare_demo_app.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["qdynamics_healthcare_demo_app.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qdynamics_healthcare_demo_app.tasks.all"
# 	],
# 	"daily": [
# 		"qdynamics_healthcare_demo_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"qdynamics_healthcare_demo_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qdynamics_healthcare_demo_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"qdynamics_healthcare_demo_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "qdynamics_healthcare_demo_app.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "qdynamics_healthcare_demo_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qdynamics_healthcare_demo_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qdynamics_healthcare_demo_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qdynamics_healthcare_demo_app.utils.before_request"]
# after_request = ["qdynamics_healthcare_demo_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["qdynamics_healthcare_demo_app.utils.before_job"]
# after_job = ["qdynamics_healthcare_demo_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"qdynamics_healthcare_demo_app.auth.validate"
# ]

# on_social_login = "qdynamics_healthcare_demo_app.auth.on_social_login"

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

