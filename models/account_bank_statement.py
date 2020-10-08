# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class AccountBankStatementLine(models.Model):

    _inherit = 'account.bank.statement.line'

    invoice_id = fields.Many2one(comodel_name='account.invoice',
                                 string='Invoice',
                                 domain=[('state', 'in', ('open', 'paid'))])
    
    residual = fields.Monetary(string='Amount Due',
                               related='invoice_id.residual_signed')

    @api.onchange('invoice_id')
    def _onchange_invoice(self):
        if self.invoice_id:
            self.name = self.invoice_id.name or self.invoice_id.number
            self.ref = self.invoice_id.number
            self.partner_id = self.invoice_id.commercial_partner_id
            self.residual = self.invoice_id.residual_signed
            if self.invoice_id.type in ('out_invoice', 'in_refund'):
                self.amount = self.invoice_id.amount_total
            else:
                self.amount = - self.invoice_id.amount_total






