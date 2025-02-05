from odoo import models, fields, api

class Material(models.Model):
    _name = 'woodwork.material'
    _description = "Matériau de Menuiserie"

    name = fields.Char(string="Nom du Matériau", required=True)
    type = fields.Selection([
        ('wood', 'Bois'),
        ('metal', 'Métal'),
        ('plastic', 'Plastique'),
    ], string="Type de Matériau", required=True)
    supplier_id = fields.Many2one('res.partner', string="Fournisseur")
    cost = fields.Float(string="Coût par Unité")
    quantity_available = fields.Float(string="Quantité Disponible")
    uom_id = fields.Many2one('uom.uom', string="Unité de Mesure", required=True)
    