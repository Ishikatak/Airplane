# Copyright (c) 2024, ishika and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class FlightPassenger(Document):
# 	def before_save(self):
# 		if self.first_name and self.last_name:
# 			self.full_name=f"{self.first_name} {self.last_name}"
		
from frappe.model.document import Document


class FlightPassenger(Document):
    def before_save(self):
        # Handle cases where only first name or last name is set
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:  # Only first name is provided
            self.full_name = self.first_name
        elif self.last_name:  # Only last name is provided
            self.full_name = self.last_name
        else:
            self.full_name = None  # Both are missing
