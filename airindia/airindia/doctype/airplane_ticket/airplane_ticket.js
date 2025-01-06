// Copyright (c) 2024, vishal haldar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {

		

		if ((frm.doc.status == "Boarded")){

			frm.add_custom_button("Assign Seat", function(){

				frappe.prompt({
					label: "Seat Number",
					fieldname: "seat_number",
					fieldtype: "Data"
	
				},(values)=>{
	
					frm.set_value("seat",values.seat_number);
				},"Select Seat","Assign");
	
			},"Actions");


		}
		   

	},


});

