from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on Imprest Surrender'),
		'fieldname': 'imprest_application',
		'transactions': [
			{
				'label': _('Imprest'),
				'items': ['Imprest Surrender','Journal']
			},
		]
	}
