from odoo import fields, models


class IoTSystem(models.Model):
    _name = 'iot.system'
    _description = 'IoT System'

    name = fields.Char(required=True)
    device_ids = fields.One2many('iot.device', inverse_name='system_id')
    system_action_ids = fields.One2many(
        'iot.system.action', inverse_name='system_id'
    )
