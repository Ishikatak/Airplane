// Copyright (c) 2024, ishika and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button('Action', () => {
            let d = new frappe.ui.Dialog({
                title: 'Seat Number',
                fields: [
                    {label: 'Seat Number', fieldname: 'seat_number', fieldtype: 'Data'}
                ],
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
