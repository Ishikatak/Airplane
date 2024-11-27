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
    def calculate_total_amount(self):
        total_addon_amount = sum(item.amount for item in self.add_ons) if self.add_ons else 0
        self.total_amount = int(self.flight_price) + total_addon_amount

    def before_submit(self):
        
        if self.status != "Boarded":
            frappe.throw("Cannot save the ticket unless status is Boarded")
  
    def validate(self):
        self.calculate_total_amount()
    
        airplane_flight = frappe.get_doc('Airplane Flight', self.flight)
        
     
        airplane = frappe.get_doc('Airplane', airplane_flight.airplane)
        
        
        airplane_capacity = airplane.capacity

      
        booked_tickets = frappe.db.count('Airplane Ticket', {
            'flight': self.flight
        })

       
        if booked_tickets >= airplane_capacity:
            frappe.throw(f"No more tickets can be booked for this flight. The airplane has only {airplane_capacity} seats.")