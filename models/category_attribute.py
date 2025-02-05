# FILE: models/category_attribute.py
from odoo import models, fields

class ProductCategoryAttribute(models.Model):
    _name = 'product.category.attribute'
    _description = "Attribut de Catégorie de Produit"

    # Nom de l'attribut
    name = fields.Char(
        string="Nom",
        required=True
    )

    # Type de valeur (dimension, matériau, finition)
    value_type = fields.Selection(
        selection=[
            ('dimension', 'Dimension'),
            ('material', 'Matériau'),
            ('finish', 'Finition'),
        ],
        string="Type de Valeur",
        default='dimension'
    )

    # Add inverse field
    product_tmpl_id = fields.Many2one(
        'product.template',
        string='Product Template',
        required=True,
        ondelete='cascade'
    )

    value = fields.Char(
        string="Valeur",
        required=True
    )