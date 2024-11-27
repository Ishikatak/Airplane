# Copyright (c) 2024, ishika and contributors
# For license information, please see license.txt

# import frappe
# from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]


import frappe
import frappe

def execute(filters=None):
    # Define the columns for the report
    columns = [{
        "fieldname": "airline",
        "label": "Airline",
        "fieldtype": "Link",
        "options": "Airline"  # Link to Airline DocType
    }, {
        "fieldname": "revenue",
        "label": "Revenue",
        "fieldtype": "Currency",
        "options": "INR"
    }]

    # Fetch airplane tickets
    tickets = frappe.get_all("Airplane Ticket", fields=["total_amount", "flight"], filters={})
    
    # Initialize a dictionary to hold aggregated revenue by airline
    aggregated_data = {}
    airlines = frappe.get_all("Airline", fields=["name"])  # Fetch all airlines

    for airline in airlines:
        aggregated_data[airline['name']] = 0  # Initialize all airlines with 0 revenue

    # Loop through the tickets and aggregate the revenue
    for ticket in tickets:
        flight = frappe.get_value("Airplane Flight", ticket.flight, "airplane")
        if flight:
            airline = frappe.get_value("Airplane", flight, "airline")
            if airline:
                aggregated_data[airline] += ticket.total_amount  # Aggregate revenue

    # Prepare final data for the report
    final_data = [{"airline": airline, "revenue": revenue} for airline, revenue in aggregated_data.items()]

    # Calculate total revenue
    total_revenue = sum(item['revenue'] for item in final_data)

    # Prepare donut chart data
    chart = {
        "data": {
            "labels": [item["airline"] for item in final_data],
            "datasets": [
                {
                    "values": [item["revenue"] for item in final_data]
                }
            ],
        },
        "type": "donut"  # Use 'donut' for the donut chart
    }

    return columns, final_data, f"Total Revenue: {total_revenue}", chart
