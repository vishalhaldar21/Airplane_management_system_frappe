# Copyright (c) 2024, Vishal Haldar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta 

class Contract(Document):

    def before_save(self):
       
        global_config = frappe.get_single("Global Configuration")
        
        
        if global_config.default_rent_amount:
            self.rent_amount = global_config.default_rent_amount

     
        if isinstance(self.start_date, str):
            self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()

        
        if self.start_date and self.payment_terms:
            if self.payment_terms == "Monthly":
               
                self.end_date = self.start_date + relativedelta(months=1)
               
                self.rent_amount = global_config.default_rent_amount
            elif self.payment_terms == "Quarterly":
               
                self.end_date = self.start_date + relativedelta(months=3)
              
                self.rent_amount = global_config.default_rent_amount * 3

      
        if isinstance(self.end_date, datetime):
            self.end_date = self.end_date.strftime('%Y-%m-%d')

        
        if self.shop:
            
            shop = frappe.get_doc("Airport Shop", self.shop)

            
            if not shop:
                frappe.throw(f"No Airport Shop found with ID: {self.shop}")

         
            current_date = datetime.now().date()

            
            if shop.shop_status == "Occupied":
                frappe.throw(f"This shop is already occupied. Please wait for availability or choose another shop.")

           
            if self.start_date <= current_date <= self.end_date:
               
                shop.select_qhzc = "Occupied"
                shop.is_available = 0
                shop.save()
            else:

                shop.select_qhzc = "Available"
                shop.is_available = 1
                shop.save()
        else:
            frappe.throw("No linked Airport Shop found for this contract!")
        