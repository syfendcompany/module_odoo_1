from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError

class TestProductTemplate(TransactionCase):
    def setUp(self):
        super(TestProductTemplate, self).setUp()
        # Créer un produit parent pour les tests
        self.parent_product = self.env['product.template'].create({
            'name': 'Parent Product',
            'is_assembly': True,
        })

    def test_create_product_template(self):
        # Test de création d'un produit simple
        product = self.env['product.template'].create({
            'name': 'Test Product',
            'is_assembly': True,
        })
        self.assertEqual(product.name, 'Test Product')
        self.assertTrue(product.is_assembly)

    def test_product_assembly_relations(self):
        # Test des relations parent-enfant entre les produits
        child_product = self.env['product.template'].create({
            'name': 'Child Product',
            'is_assembly': False,
            'parent_id': self.parent_product.id,
        })
        self.assertEqual(child_product.parent_id, self.parent_product)
        self.assertIn(child_product, self.parent_product.child_ids)

    def test_product_technical_details(self):
        # Test des champs techniques (technical_sheet_id et design_file_id)
        product = self.env['product.template'].create({
            'name': 'Product with Technical Details',
            'technical_sheet_id': self.env['ir.attachment'].create({
                'name': 'Technical Sheet',
                'datas': 'JVBERi0xLjQK