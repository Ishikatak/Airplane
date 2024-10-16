# Copyright (c) 2024, ishika and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator



class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        print(self.status,"status")
        if self.status != 'Completed':
            self.status = 'Completed'
        





