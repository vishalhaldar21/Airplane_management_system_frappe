// Copyright (c) 2024, vishal haldar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Contract", {
    refresh(frm) {
        
    },
    onload(frm) {
        if (!frm.doc.rent_amount) {
            frappe.db.get_single_value('Global Configuration', 'default_rent_amount')
                .then((default_rent_amount) => {
                    frm.set_value('rent_amount', default_rent_amount);
                    
                });
        }
    }

});


