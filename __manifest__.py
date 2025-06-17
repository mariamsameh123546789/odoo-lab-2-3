{
    "name": "HMS - Hospital Management System",
    "summary": "Comprehensive hospital management for patients, records, and staff",
     "description": """
        HMS module to efficiently manage:
        - Patients
        - Medical Records
        - Medical History
        - Departments
        - Doctors
    """,
    "author": "Mariam Sameh",
    "category": "Healthcare",
    "version": "1.0",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/hms_menus.xml",
        "views/patient_views.xml",
        "views/department_views.xml",
        "views/doctors_views.xml",
        "views/patient_log_views.xml",
        "views/res_partner_views.xml",
    ],
    "application": True,
    "installable": True,
}
