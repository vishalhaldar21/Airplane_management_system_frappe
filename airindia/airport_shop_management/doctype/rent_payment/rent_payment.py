# Copyright (c) 2024, vishal haldar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RentPayment(Document):
    
    def before_save(self):
       
        if self.contract_id:
            
            contract = frappe.get_doc('Contract', self.contract_id)
            
            if contract:
                
                contract.payment_status = self.payment_status
                contract.save()