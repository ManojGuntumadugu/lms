import frappe

@frappe.whitelist()
def update_staff(firstname,lastname,gender,profile_img):
    print(first_name,last_name,gender,profile_img)
    doc = frappe.get_doc({
    'doctype': 'Staff',
    'first_name': firstname,
    'last_name' : lastname,
    'gender' : gender,
    'profile_img' : profile_img
    })
    doc.insert()
    return "Staff Successfully Updated"