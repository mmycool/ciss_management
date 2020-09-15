from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
                        "label": _("Operations"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Work Plan",
                                        "description": _("Submit Workplans."),
                                },
                                {
                                        "type":"doctype",
                                        "name":"Project Report",
                                        "description":_("Project Reports"),
                                }
                        ]
                },
				{
                        "label": _("Imprest"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Imprest Application",
                                        "description": _("Description of imprest status."),
                                },
								{
										"type": "doctype",
										"name": "Imprest Surrender",
										"description": _("Description of Imprest Surrender"),
								}
                        ]
                },
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
				},
                                {
                                        "type": "doctype",
                                        "name": "Project Areas",
                                        "description": _("Project Areas and their Corps."),
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
				},	
				{
					"type": "doctype",
					"name": "CISS Group Membership",
					"description": _("Membership information."),
				},
                                {
                                        "type": "doctype",
                                        "name": "Learning Institutions",
                                        "description": _("Learning Institution Groups."),
                                },
				{
					"type": "doctype",
					"name": "Activity Master",
					"description": _("Activities."),
				}
			]
		}
	]
