from odoo import models, fields

class ExampleWizard(models.TransientModel):
    _name = 'woodworking_workshop.example_wizard'
    _description = 'Example Wizard'

    name = fields.Char(string="Name")
