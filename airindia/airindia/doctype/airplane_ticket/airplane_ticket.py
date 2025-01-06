# Copyright (c) 2024, vishal haldar and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	
    def validate(self):
        
        new_add_ons = []
        seen = set()
        
        for add_on in self.add_ons:
            
            if add_on.item not in seen:
                
                seen.add(add_on.item)
                new_add_ons.append(add_on)
        
        self.add_ons = new_add_ons
        
        a_mount = 0
        
        for add_on in self.add_ons:
            
            a_mount += add_on.amount
                   
        self.total_amount = self.flight_price + a_mount 
    
    
    def before_submit(self):
        
        if self.status != "Boarded":
            frappe.throw("please make the status to Boarded then submit")
    
    def before_insert(self):
        
        random_integer = random.randint(1, 100) 
        random_letter = chr(random.randint(65, 69))  
        self.seat = f"{random_integer}{random_letter}"
        

  
    def on_update(self):
        self.airplane_capacity()

    def airplane_capacity(self):
        if self.flight:
            ticket_count = frappe.db.count(
                'Airplane Ticket',
                filters={
                    'flight': self.flight,
                    'name':('!=',self.name)
                }
            )

            flight = frappe.get_doc('Airplane Flight', self.flight)
            if flight:
                airplane = frappe.get_doc('Airplane', flight.airplane)

                if ticket_count >= airplane.capacity:
                    frappe.throw(f'Number of tickets exceeds airplane capacity of {airplane.capacity}. Cannot create more Airplane Tickets.')