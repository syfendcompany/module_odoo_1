from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Project(models.Model):
    _inherit = 'project.project'

    woodwork_project_id = fields.Many2one('woodwork.project', string="Projet de Menuiserie")
    product_ids = fields.Many2many('product.template', string="Produits Associés")
    production_status = fields.Selection([
        ('draft', 'Brouillon'),
        ('in_progress', 'En Cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ], string="État de Production", default='draft')
    deadline = fields.Date(string="Échéance")
    notes = fields.Text(string="Remarques")

    @api.constrains('deadline')
    def _check_deadline(self):
        for record in self:
            if record.deadline and record.deadline < date.today():
                raise ValidationError("La date d'échéance ne peut pas être antérieure à aujourd'hui.")

    def start_production(self):
        for project in self:
            if project.production_status == 'draft':
                project.production_status = 'in_progress'