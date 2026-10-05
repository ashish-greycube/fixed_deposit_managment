app_name = "fixed_deposit_managment"
app_title = "FD Manager"
app_publisher = "GreyCube Technologies"
app_description = "Customization for FD Manager"
app_email = "admin@greycube.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "fixed_deposit_managment",
# 		"logo": "/assets/fixed_deposit_managment/logo.png",
# 		"title": "FD Manager",
# 		"route": "/fixed_deposit_managment",
# 		"has_permission": "fixed_deposit_managment.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fixed_deposit_managment/css/fixed_deposit_managment.css"
# app_include_js = "/assets/fixed_deposit_managment/js/fixed_deposit_managment.js"

# include js, css files in header of web template
# web_include_css = "/assets/fixed_deposit_managment/css/fixed_deposit_managment.css"
# web_include_js = "/assets/fixed_deposit_managment/js/fixed_deposit_managment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fixed_deposit_managment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_list_js = {"Fixed Deposit": "fd_manager/doctype/fixed_deposit/fixed_deposit_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "fixed_deposit_managment/public/icons.svg"

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
# 	"methods": "fixed_deposit_managment.utils.jinja_methods",
# 	"filters": "fixed_deposit_managment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fixed_deposit_managment.install.before_install"
# after_install = "fixed_deposit_managment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fixed_deposit_managment.uninstall.before_uninstall"
# after_uninstall = "fixed_deposit_managment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "fixed_deposit_managment.utils.before_app_install"
# after_app_install = "fixed_deposit_managment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "fixed_deposit_managment.utils.before_app_uninstall"
# after_app_uninstall = "fixed_deposit_managment.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "fixed_deposit_managment.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fixed_deposit_managment.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["fixed_deposit_managment.search.awesomebar_results"]

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

doc_events = {
	"Journal Entry": {
		"on_cancel": "fixed_deposit_managment.fd_manager.doctype.journal_entry.on_cancel"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fixed_deposit_managment.tasks.all"
# 	],
# 	"daily": [
# 		"fixed_deposit_managment.tasks.daily"
# 	],
# 	"hourly": [
# 		"fixed_deposit_managment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fixed_deposit_managment.tasks.weekly"
# 	],
# 	"monthly": [
# 		"fixed_deposit_managment.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "fixed_deposit_managment.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "fixed_deposit_managment.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fixed_deposit_managment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "fixed_deposit_managment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["fixed_deposit_managment.utils.before_request"]
# after_request = ["fixed_deposit_managment.utils.after_request"]

# Job Events
# ----------
# before_job = ["fixed_deposit_managment.utils.before_job"]
# after_job = ["fixed_deposit_managment.utils.after_job"]

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
# 	"fixed_deposit_managment.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

