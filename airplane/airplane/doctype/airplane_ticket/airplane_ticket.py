from frappe.model.document import Document
import frappe
import random

class AirplaneTicket(Document):
    def before_insert(self):
        # Generate a random seat number
        number = random.randint(10, 99)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{number}{letter}"

    def validate(self):
        # Check for duplicate add-ons
        addon_items = []
        for addon in self.add_ons:
            if addon.item in addon_items:
                frappe.throw("Duplicate Add-ons are not allowed")
            addon_items.append(addon.item)

        # Calculate total amount
        addon_total = 0
        for addon in self.add_ons:
            addon_total += addon.amount
        self.total_amount = int(self.flight_price) + addon_total

    def before_submit(self):
        # Prevent saving if status is not "Boarded"
        if self.status != "Boarded":
            frappe.throw("Cannot save the ticket unless status is Boarded")
