from odoo import api, fields, models


class MaintenanceTeam(models.Model):
    _inherit = ['maintenance.request']  # inheriting other model
    _description = "Click me to know more about the Maintenance."


    apartment_issue_id = fields.Many2one(comodel_name='apartments.management', string='Apartments')
    apartment_address_is = fields.Char(string="Property Address", help="Type Your Address.",related='apartment_issue_id.name')

    cost = fields.Float(string="Cost", required=True)
    renters_fault = fields.Boolean(string='Renters Fault')

    # report_name1 = 'property_management_newupdates.maintenance_user_report_service_details'
    # report_file1 = 'property_management_newupdates.maintenance_user_report_service_details'

    # rxl = 'property_management_newupdates.maintenance_xlsx'
    # rxl_f = 'property_management_newupdates.maintenance_xlsx'
