from odoo import models, api, fields

import logging
_logger = logging.getLogger(__name__)

class AccountAccountTag(models.Model):
    _name = "account.account.tag"
    _inherit = "account.account.tag"

    company_ids = fields.Many2many(
        comodel_name="res.company", 
        string="Companies", 
        required=True, 
        store=True, 
        copy=True, 
        index=False
    )
    code = fields.Char(
        string="Code", 
        required=True
    )
    parent_id = fields.Many2one(
        comodel_name="account.account.tag", 
        string="Parent Tag", 
        ondelete="cascade"
    )
    child_ids = fields.One2many(
        comodel_name="account.account.tag", 
        inverse_name="parent_id", 
        string="Child Tags"
    )
    