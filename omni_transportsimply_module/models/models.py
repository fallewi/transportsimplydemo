# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
from odoo.exceptions import UserError
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, AccessError


class SalesOrder(models.Model):
	_inherit = "sale.order"


	destination_address_id = fields.Many2one(
        'res.partner', string='Destination Address', readonly=True, required=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

	booker_id = fields.Many2one(
        'res.partner', string='Booker', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

	passengers_list = fields.Text(string='Passengers')

	to_date = fields.Datetime('To Date', help='Date of the signature.', copy=False)

	from_date = fields.Datetime('From Date', help='Date of the signature.', copy=False)