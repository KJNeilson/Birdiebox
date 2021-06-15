# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class CustomProductTemplate(models.Model):
    _inherit = ['product.template']

    attachment_count = fields.Integer(compute='_compute_attachment_count',
                                      string="File")

    @api.model
    def create(self, vals):
        if 'default_code' in vals:
            vals['barcode'] = vals['default_code']

        return super(CustomProductTemplate, self).create(vals)

    def write(self, vals):
        if 'default_code' in vals:
            vals['barcode'] = vals['default_code']

        return super(CustomProductTemplate, self).write(vals)

    def _compute_attachment_count(self):
        attachment_data = self.env['ir.attachment'].read_group(
            [('res_model', '=', self._name),
             ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        mapped_data = dict([(data['res_id'], data['res_id_count'])
                            for data in attachment_data])
        for product_template in self:
            product_template.attachment_count = mapped_data.get(
                product_template.id, 0)

    def action_open_attachments(self):
        self.ensure_one()

        return {
            'name':
            _('Digital Attachments'),
            'domain': [('res_model', '=', self._name),
                       ('res_id', '=', self.id)],
            'res_model':
            'ir.attachment',
            'type':
            'ir.actions.act_window',
            'view_mode':
            'tree,form',
            'context':
            "{'default_res_model': '%s','default_res_id': %d}" %
            (self._name, self.id),
            'help':
            """
                <p class="o_view_nocontent_smiling_face">Add attachments for this digital product</p>
                <p>The attached files are the ones that will be purchased and sent to the customer.</p>
                """,
        }
