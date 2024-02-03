import frappe

@frappe.whitelist()
def create_staff(firstname,lastname,gender,profile_img):
    doc = frappe.get_doc({
    'doctype': 'Staff',
    'first_name': firstname,
    'last_name' : lastname,
    'gender' : gender,
    'profile_img' : profile_img
    })
    doc.insert()
    return "Staff Successfully added"

@frappe.whitelist()
def get_staff(staff_id):
    staff = frappe.db.get_value("Staff", filters={"name": staff_id}, fieldname=["first_name", "last_name", "gender", "profile_img"])

    if staff:
        return {
            "firstname": staff[0],
            "lastname": staff[1],
            "gender": staff[2],
            "profile_img": staff[3]
        }
    else:
        return None
    
@frappe.whitelist()
def update_staff(staff_id,firstname,lastname,gender,profile_img):
    
    doc = frappe.get_doc("Staff", staff_id)
    doc.first_name = firstname
    doc.last_name = lastname
    doc.gender = gender
    doc.profile_img = profile_img
    doc.save()
    return "Successfully updated staff"

@frappe.whitelist()
def delete_staff(staff_id,firstname,lastname,gender,profile_img):
    
    doc = frappe.delete_doc("Staff", staff_id)
    doc.first_name = firstname
    doc.last_name = lastname
    doc.gender = gender
    doc.profile_img = profile_img
    doc.save()
    return "Successfully deleted staff"