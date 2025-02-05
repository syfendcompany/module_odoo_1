from odoo.tests import TransactionCase
from odoo.exceptions import ValidationError
from datetime import date, timedelta

class TestProject(TransactionCase):
    def setUp(self):
        super(TestProject, self).setUp()
        # Créer un produit pour les tests
        self.product = self.env['product.template'].create({
            'name': 'Test Product',
            'is_assembly': True,
        })

    def test_create_project(self):
        # Test de création d'un projet simple
        project = self.env['project.project'].create({
            'name': 'Test Project',
            'production_status': 'draft',
        })
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.production_status, 'draft')

    def test_project_product_relations(self):
        # Test des relations entre les projets et les produits
        project = self.env['project.project'].create({
            'name': 'Project with Products',
            'production_status': 'draft',
            'product_ids': [(4, self.product.id)],
        })
        self.assertIn(self.product, project.product_ids)

    def test_project_deadline(self):
 