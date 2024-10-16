# Copyright (c) 2024, ishika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class voters(Document):
    def validate(self):
        if self.age < 18:
            frappe.throw("Person's age must be at least 18")
        else:
            frappe.msgprint("Person is eligible to vote")
