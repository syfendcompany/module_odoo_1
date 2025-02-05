# FILE: models/product.py
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Documents techniques associés
    technical_sheet_id = fields.Many2one(
        'ir.attachment',
        string="Fiche Technique"
    )
    design_file_id = fields.Many2one(
        'ir.attachment',
        string="Fichier de Conception"
    )

    # Gestion des assemblages multi-niveaux
    is_assembly = fields.Boolean(
        string="Est un Assemblage",
        default=False
    )
    parent_id = fields.Many2one(
        'product.template',
        string="Assemblage Parent"
    )
    child_ids = fields.One2many(
        'product.template',
        'parent_id',
        string="Composants Enfants"
    )
     # Relation avec les attributs de catégorie
    category_attribute_ids = fields.One2many(
        'product.category.attribute',
        'product_tmpl_id',
        string='Attributs de catégorie'
    )