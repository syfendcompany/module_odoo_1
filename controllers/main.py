# FILE: /woodworking_workshop/controllers/main.py
from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

class WoodworkingController(http.Controller):
    """
    Contrôleur pour le module Woodworking Workshop.
    Ce contrôleur expose des endpoints API REST pour interagir avec les produits, les projets et les tâches.
    """

    # Endpoint pour récupérer la liste des produits
    @http.route('/woodworking/api/v1/products', type='json', auth='user', methods=['GET'])
    def get_products(self):
        """
        Retourne la liste des produits disponibles dans l'atelier de menuiserie.
        Exemple de réponse :
        {
            "status": "success",
            "data": [
                {
                    "id": 1,
                    "name": "Table en chêne",
                    "is_assembly": true,
                    "parent_id": null,
                    "child_ids": [2, 3]
                }
            ]
        }
        """
        try:
            # Limiter les résultats pour des raisons de performance
            products = request.env['product.template'].search([], limit=100)
            return {
                'status': 'success',
                'data': [{
                    'id': product.id,
                    'name': product.name,
                    'is_assembly': product.is_assembly,
                    'parent_id': product.parent_id.id if product.parent_id else None,
                    'child_ids': [child.id for child in product.child_ids],
                } for product in products]
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred. Please contact the administrator.',
            }

    # Endpoint pour récupérer les détails d'un produit spécifique
    @http.route('/woodworking/api/v1/products/<int:product_id>', type='json', auth='user', methods=['GET'])
    def get_product(self, product_id):
        """
        Retourne les détails d'un produit spécifique.
        Exemple de réponse :
        {
            "status": "success",
            "data": {
                "id": 1,
                "name": "Table en chêne",
                "is_assembly": true,
                "parent_id": null,
                "child_ids": [2, 3],
                "technical_sheet_id": 5,
                "design_file_id": 6
            }
        }
        """
        try:
            # Validation de l'ID du produit
            if not isinstance(product_id, int) or product_id <= 0:
                return {
                    'status': 'error',
                    'message': 'Invalid product ID',
                }

            product = request.env['product.template'].browse(product_id)
            if not product.exists():
                return {
                    'status': 'error',
                    'message': 'Product not found',
                }

            return {
                'status': 'success',
                'data': {
                    'id': product.id,
                    'name': product.name,
                    'is_assembly': product.is_assembly,
                    'parent_id': product.parent_id.id if product.parent_id else None,
                    'child_ids': [child.id for child in product.child_ids],
                    'technical_sheet_id': product.technical_sheet_id.id if product.technical_sheet_id else None,
                    'design_file_id': product.design_file_id.id if product.design_file_id else None,
                }
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred. Please contact the administrator.',
            }

    # Endpoint pour récupérer la liste des projets
    @http.route('/woodworking/api/v1/projects', type='json', auth='user', methods=['GET'])
    def get_projects(self):
        """
        Retourne la liste des projets dans l'atelier de menuiserie.
        Exemple de réponse :
        {
            "status": "success",
            "data": [
                {
                    "id": 1,
                    "name": "Projet Table et Chaises",
                    "production_status": "draft",
                    "deadline": "2023-12-31",
                    "product_ids": [1, 2]
                }
            ]
        }
        """
        try:
            # Limiter les résultats pour des raisons de performance
            projects = request.env['project.project'].search([], limit=100)
            return {
                'status': 'success',
                'data': [{
                    'id': project.id,
                    'name': project.name,
                    'production_status': project.production_status,
                    'deadline': project.deadline,
                    'product_ids': [product.id for product in project.product_ids],
                } for project in projects]
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred. Please contact the administrator.',
            }

    # Endpoint pour récupérer les détails d'un projet spécifique
    @http.route('/woodworking/api/v1/projects/<int:project_id>', type='json', auth='user', methods=['GET'])
    def get_project(self, project_id):
        """
        Retourne les détails d'un projet spécifique.
        Exemple de réponse :
        {
            "status": "success",
            "data": {
                "id": 1,
                "name": "Projet Table et Chaises",
                "production_status": "draft",
                "deadline": "2023-12-31",
                "product_ids": [1, 2],
                "task_ids": [3, 4]
            }
        }
        """
        try:
            # Validation de l'ID du projet
            if not isinstance(project_id, int) or project_id <= 0:
                return {
                    'status': 'error',
                    'message': 'Invalid project ID',
                }

            project = request.env['project.project'].browse(project_id)
            if not project.exists():
                return {
                    'status': 'error',
                    'message': 'Project not found',
                }

            return {
                'status': 'success',
                'data': {
                    'id': project.id,
                    'name': project.name,
                    'production_status': project.production_status,
                    'deadline': project.deadline,
                    'product_ids': [product.id for product in project.product_ids],
                    'task_ids': [task.id for task in project.task_ids],
                }
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': 'An unexpected error occurred. Please contact the administrator.',
            }

