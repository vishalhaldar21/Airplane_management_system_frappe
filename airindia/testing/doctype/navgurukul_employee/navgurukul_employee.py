# Copyright (c) 2024, vishal haldar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class NavgurukulEmployee(Document):
	
   def before_save(self):
      
      a = ""
      b = self.location[:3]
      
      if self.employee_type == "Full Time":
         a = "FT"
      elif self.employee_type == "Part Time":
         a = "PT"
      else:
         a = "IT"
         
      self.name = f"{self.name} - {a} - {b}"
