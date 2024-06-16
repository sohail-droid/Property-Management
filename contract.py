from odoo import api, fields, models


class ContractManagement(models.Model):
    _name = "contract.management"  # Model Name
    _description = "Click to know more about the contract Management."
    _inherit = ['mail.thread', 'mail.activity.mixin']

    contract_start_date = fields.Date(string='Contract Start Date')
    contract_end_date = fields.Date(string='Contract End Date')
    photo = fields.Binary(attachment=True, help="Looking Good.")
    note = fields.Text(string='Notes')
    cost = fields.Integer(string='Cost Info')
    property_id = fields.Many2one('property.management', string="Property")

    check_list_ids = fields.Many2many('check.list')

    # Creating a Status Bar.
    state = fields.Selection([('draft', 'Draft'), ('running', 'Running'), ('expired', 'Expired'),
                              ('cancel', 'Cancelled')], default="draft", string="Status", tracking=True)

    email_from = fields.Char(string="Manager Mail")
    email_to = fields.Char(string="Resident's Mail")

    # @Api.model /depend/onchange

    def action_draft_button(self):
        self.state = 'draft'

    def action_confirm_button(self):
        self.state = 'running'

    def action_expired_button(self):
        self.state = 'expired'

    def action_cancel_button(self):
        self.state = 'cancel'


    @api.model
    def update_contract_states(self):
        today = fields.Date.today()
        contract_records = self.env['contract.management'].search([])

        for record in contract_records:
            if record.contract_end_date:
                if record.contract_end_date < today:
                    if record.state == 'running':
                        record.state = 'expired'
                elif record.contract_end_date >= today:
                    if record.state in ('draft', 'expired'):
                        record.state = 'running'
            else:
                if record.state != 'draft':
                    record.state = 'draft'

    def action_renew_button(self):
        new_contract = self.copy({
            'state': 'draft',
            'contract_start_date': False,
            'contract_end_date': False,
        })
        view_id = self.env.ref('property_management_newupdates.view_contract_form').id
        return {
            'type': 'ir.actions.act_window',
            'name': 'Renew Contract',
            'res_model': 'contract.management',
            'res_id': new_contract.id,
            'view_mode': 'form',
            'view_id': view_id,
            'target': 'current',
        }

    def action_send_email(self):
        # Load email template
        template_id = self.env.ref('property_management_newupdates.hello_world').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


class CheckList(models.Model):
    _name = 'check.list'
    name = fields.Char()


