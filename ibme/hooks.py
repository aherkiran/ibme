# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ibme"
app_title = "IBME"
app_publisher = "IBME"
app_description = "Language Expert"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "aherkiran765@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ['Website Settings','Web Page','Website Script']
#fixtures = ['Custom Field', 'Property Setter', "Custom Script","Print Format"]
# include js, css files in header of desk.html
# app_include_css = "/assets/ibme/css/ibme.css"
# app_include_js = "/assets/ibme/js/ibme.js"

# include js, css files in header of web template
# web_include_css = "/assets/ibme/css/ibme.css"
# web_include_js = "/assets/ibme/js/ibme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ibme.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ibme.install.before_install"
# after_install = "ibme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ibme.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ibme.tasks.all"
# 	],
# 	"daily": [
# 		"ibme.tasks.daily"
# 	],
# 	"hourly": [
# 		"ibme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ibme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ibme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ibme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ibme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ibme.task.get_dashboard_data"
# }

