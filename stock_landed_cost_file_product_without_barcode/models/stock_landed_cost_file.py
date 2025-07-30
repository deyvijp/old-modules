from odoo import models, fields, api

class StockLandedCostFile(models.Model):
    product_no_barcode_count = fields.Integer(
        string='Productos sin código de barra',
        compute='_compute_products_no_barcode_count',
        store=False
    )

    def _compute_products_no_barcode_count(self):
        for record in self:
            record.product_no_barcode_count = len(record.product_ids_no_barcode)
    def action_open_products_without_barcode_tree(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Productos sin código de barra',
            'res_model': 'product.product',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.product_ids_no_barcode.ids)],
            'context': {'default_barcode': ''},
        }
    # Método del smart button, sin wizard
    _inherit = 'stock.landed.cost.file'

    product_ids_no_barcode = fields.Many2many(
        'product.product',
        string='Productos sin código de barra',
        compute='_compute_products_no_barcode',
        store=False
    )

    @api.depends()
    def _compute_products_no_barcode(self):
        for record in self:
            products = self.env['product.product']
            for picking in record._get_file_related_pickings():
                if picking.state != 'cancel':
                    for move in picking.move_lines:
                        product = move.product_id
                        if not product.barcode:
                            products |= product
            record.product_ids_no_barcode = products
