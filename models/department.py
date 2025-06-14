from odoo import models, fields, api

class HMSDepartment(models.Model):
    _name = "hms.department"
    _description = "Hospital Department"

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is Opened", default=True)
    patient_ids = fields.One2many("hms.patient", "department_id", string="Patients")
