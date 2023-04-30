from odoo.tests.common import SavepointCase, Form


class TestCommon(SavepointCase):

    def _create_data(self):
        form = Form(self.env['material.data'])
        form.name = 'celana'
        form.material_code = 'CLN'
        form.material_type = 'jeans'
        form.material_buy_price = 100
        form.partner_id = self.env.ref('base.res_partner_12')
        return form.save()
