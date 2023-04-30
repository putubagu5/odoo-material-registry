from odoo import api, fields, models
from odoo.exceptions import Warning


class MaterialData(models.Model):
    _name = 'material.data'
    _description = 'Material Data'

    name = fields.Char('Material Name', required=True)
    material_code = fields.Char('Material Code', required=True)
    material_type = fields.Selection([
        ('fabric', "Fabric"),
        ('jeans', "Jeans"),
        ('cotton', "Cotton"),
    ], 'Material Type', required=True)
    material_buy_price = fields.Float('Material Buy Price', required=True)
    partner_id = fields.Many2one(
        'res.partner', 'Related Partner', required=True)

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        """ constrains function to check material buy price """
        domain = [
            ('material_buy_price', '<', 100),
            ('id', '=', self.id),
        ]
        rec = self.search(domain)
        if rec:
            raise Warning('Material buy price is lower than 100!')
