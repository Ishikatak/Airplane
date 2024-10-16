frappe.ready(function() {
	// bind events here
	// frappe.ui.form.on('Book Flight Ticket', {
    //     onload: function(frm) {
    //         // Check if the flight field is already set
    //         if (frm.doc.flight) {
    //             // Fetch the flight price based on the selected flight
    //             frappe.db.get_value('Flight', frm.doc.flight, 'price', function(value) {
    //                 if (value && value.price) {
    //                     // Set the flight price field and make it read-only
    //                     frm.set_value('flight_price', value.price);
    //                     frm.set_df_property('flight_price', 'read_only', 1); // Making the field read-only
    //                 } else {
    //                     // Default value if not found
    //                     frm.set_value('flight_price', 0);
    //                 }
    //             });
    //         } else {
    //             // Optional: Set flight price to 0 if no flight is selected
    //             frm.set_value('flight_price', 0);
    //         }
    //     }
    // });

})