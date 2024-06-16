from odoo import api, fields, models


class ApartmentsManagement(models.Model):
    _name = "apartments.management"
    _description = "Click me to know more about the Apartments Management."
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Apartment Name", required=True)

    address = fields.Text(string="Apartment Address", help="Type Your Address.")

    type = fields.Selection([('owner', 'Owner'), ('tenant', 'Tenant'), ('other', 'Other')], required=True,
                            default='other')

    furnishing = fields.Selection([('fullf', 'Full Furnished'), ('notf', 'Not Furnished')], required=True,
                                  default='fullf')

    bhk = fields.Selection([('3_bhk', '3 BHK'), ('2_bhk', '2 BHK'), ('1_bhk', '1 BHK')], required=True,
                           default='3_bhk', string="Bed/Hall/Kitchen")
    status = fields.Selection([('available', 'Available'), ('not_available', 'Not Available')], required=True)

    floors = fields.Selection([('1_floor', '1 Floor'),
                               ('2_floor', '2 Floor'),
                               ('3_floor', '3 Floor'),
                               ('4_floor', '4 Floor'),
                               ('5_floor', '5 Floor'),
                               ('6_floor', '6 Floor'),
                               ('7_floor', '7 Floor'),
                               ('8_floor', '8 Floor'), ('ground', 'Ground Floor')], required=True, default='ground',
                              string="Floor No")

    rooms = fields.Selection([
        ('room_1', 'A-01'),
        ('room_2', 'B-02'),
        ('room_3', 'C-03'),
        ('room_4', 'D-04'),
        ('room_5', 'E-05'),
        ('room_6', 'F-06'),
        ('room_7', 'H-07'),
        ('room_8', 'I-08'),
        ('room_0', 'G-00')], required=True, default='room_0', string="Room No")

    rent = fields.Integer(string="Rental Price", help=" ")

    facing = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Facing", required=True)

    currency = fields.Selection([('india', 'INR'), ('usa', 'USD'), ('Euro', 'EUR'), ('Japanese ', 'JPY'),
                                 ('Australian', 'AUD')], required=True, default='india', string="Currency")
    rent_type = fields.Selection([('1m', '1 Monthly'), ('6m', '6 Monthly')], required=True,
                                 default='1m', string="Rent Type")
    photo = fields.Binary(string="Image", required=True)

    prop_ap_id = fields.Many2one('property.management',string = "Property")







