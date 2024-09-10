from odoo import models, fields, api

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def send_receipt_email(self, order_data):
        """
        Method to send the POS receipt via email to the customer.
        """
        partner_id = self.env['res.partner'].browse(order_data.get('partner_id'))
        if partner_id.email:
            template_id = self.env.ref('your_module_name.email_template_pos_receipt').id
            self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        return True
