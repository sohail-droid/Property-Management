from odoo import api, fields, models

class PropertyManagement(models.Model):
    _name = "property.management"  # Model Name
    _description = "Click me to know more about the Property Management."
    _inherit = ['mail.thread', 'mail.activity.mixin']  # using for the chatter

    name = fields.Char(string="Property Name", required=True)
    address = fields.Char(string="Property Address", help="Type Your Address.")
    type = fields.Selection(
        [('rstl', 'Residential'), ('cmrcl', 'Commercial'), ('land', 'Land'), ('invst', 'Investment'),
         ('mscs', 'Miscellaneous'), ('other', 'Other')], required=True, default='other')

    furnishing = fields.Selection([('fullf', 'Full Furnished'), ('notf', 'Not Furnished')], required=True,
                                  default='fullf')
    manager = fields.Char(string="Property Manager", required=True)
    owner = fields.Char(string="Owner", required=True)
    currency = fields.Selection([('india', 'INR'), ('usa', 'USD'), ('Euro', 'EUR'), ('Japanese ', 'JPY'),
                                 ('Australian', 'AUD')], required=True, default='india')

    sqft = fields.Float(string="GFA(sqft)", help=" ")
    mtrs = fields.Float(string="GFA(m)", help=" ")

    property_contact = fields.Char(string="Contact", required=True)
    property_mail = fields.Char(string="Mail", required=True)
    photo = fields.Binary(attachment=True, help="Looking Good.")
    relation = fields.Integer(string="Relation")

    apartments_count = fields.Integer(string="Apartment Count", compute="_compute_apartment_count")
    apartments_ids = fields.One2many('apartments.management','prop_ap_id',string = 'Apartments')


    # creating a smart button to show apartments linked with a particular property

    def action_property_management(self):
        self.ensure_one()
        return {
            'name': 'Property Details',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form,kanban',
            'res_model': 'apartments.management',  #linking with other model
            'domain': [('prop_ap_id','=', self.id)],
            'context': {},  # Optionally, provide additional context
            'target': 'New',  # Open the action in the current window
            'res_id': self.id,
        }

    def _compute_apartment_count(self):
        for records in self:
            apartments_count = self.env['apartments.management'].search_count([('prop_ap_id','=', self.id)])
            records.apartments_count = apartments_count

