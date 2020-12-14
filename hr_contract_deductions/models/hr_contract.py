# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo import tools, _


class Allowance(models.Model):
    _name = 'hr.deduction'
    _rec_name = 'name'
    _description = 'Deduction'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Deduction Name", required=True)
    active = fields.Boolean(string="Active", default=True)


class ContractAllowanceLine(models.Model):
    _name = 'hr.contract.deduction.line'
    _rec_name = 'deduction_id'
    _description = 'Contract Allowance/Deduction Line'

    deduction_id = fields.Many2one(comodel_name="hr.deduction", string="Deduction")
    contract_id = fields.Many2one(comodel_name="hr.contract", string="Contract")
    amount = fields.Float(string="Amount")


class Contract(models.Model):
    _name = "hr.contract"
    _inherit = 'hr.contract'

    @api.multi
    @api.constrains('state')
    def _check_state(self):
        for record in self:
            if record.state == 'open':
                contract_ids = self.env['hr.contract'].search(
                    [('employee_id', '=', record.employee_id.id), ('state', '=', 'open')])
                if len(contract_ids) > 1:
                    raise exceptions.ValidationError(_('Employee Must Have Only One Running Contract'))

    deduction_ids = fields.One2many(comodel_name="hr.contract.deduction.line", inverse_name="contract_id")

#    @api.multi
#    def get_all_allowances(self):
#        return sum(self.allowances_ids.mapped('amount'))
    
    @api.multi
    def get_all_deduction(self):
        return sum(self.deduction_ids.mapped('amount'))
