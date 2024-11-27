// Copyright (c) 2024, ishika and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane', {
    refresh: function(frm) {
        // Check if user has the 'Airport Authority Personnel' role
        if (frappe.user.has_role('Airport Authority Personnel')) {
            // Make the field visible and editable
            frm.set_df_property('initial_audit_completed', 'hidden', 0);
            frm.set_df_property('initial_audit_completed', 'read_only', 0);
        } else {
            // Hide the field for users without the role
            frm.set_df_property('initial_audit_completed', 'hidden', 1);
        }
    }
});
