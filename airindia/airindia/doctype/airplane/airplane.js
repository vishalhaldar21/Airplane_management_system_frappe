// Copyright (c) 2024, vishal haldar and contributors
// For license information, please see license.txt


frappe.ui.form.on('Airplane', {

    refresh(frm) {

    },

    onload: function(frm) {
       
        if (frappe.user.has_role('Airport Authority Personnel')) {
          
            frm.set_df_property('initial_audit_completed', 'read_only', 0);
            frm.set_df_property('initial_audit_completed', 'hidden', 0);
            
        } else {
           
            frm.set_df_property('initial_audit_completed', 'hidden', 1);
        }
    }
});
