from odoo import models, fields

class TechnicalDocument(models.Model):
    _name = 'woodwork.technical.document'
    _description = "Document Technique"

    name = fields.Char(string="Nom du Document", required=True)
    product_id = fields.Many2one('product.template', string="Produit Associé", ondelete='cascade')
    file = fields.Binary(string="Fichier", attachment=True, required=True)
    filename = fields.Char(string="Nom du Fichier")
    version = fields.Char(string="Version", default="1.0")
    create_date = fields.Date(string="Date de Création", default=fields.Date.today)