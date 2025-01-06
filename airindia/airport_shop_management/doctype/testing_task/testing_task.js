// Copyright (c) 2024, vishal haldar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Testing Task", {
	refresh(frm) {

	},

    task_priority(frm) {

        if (frm.doc.task_priority == "Low") {

            frm.set_df_property('assign_to', 'hidden', 1); 

        }
        else if (frm.coc.task_priority == "Medium"){

            frm.set_df_property('assign_to', 'hidden', 1);

        }
        else {

            frm.set_df_property('assign_to', 'hidden', 0); 

        }
    }
});
