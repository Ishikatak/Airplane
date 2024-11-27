import frappe

def get_context(context):
    # Fetch shops data from the "Airport shops information" table/doctype
    context.airport_shops = frappe.get_all(
        "Airport shops information",  # Replace with the correct table/doctype name
        fields=["shop_number", "shop_name", "area", "airport"],
        filters={"status": "Available"}  # Example filter for available shops
    )
    return context
