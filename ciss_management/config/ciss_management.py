from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		
		{
			"label": _("Regional Information"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Counties",
					"description": _("Counties information."),
				},
				{
					"type": "doctype",
					"name": "Sub_Counties",
					"description": _("Sub-Counties information."),
				},				
				{
					"type": "doctype",
					"name": "Ward",
					"description": _("Wards information."),
				}
			]
		},
		{
			"label": _("Group Information"),
			"items": [
				{
					"type": "doctype",
					"name": "CISS Group",
					"description": _("Groups information."),
				}
			]
		}
	]
