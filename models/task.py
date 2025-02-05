from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit = 'project.task'

    material_ids = fields.Many2many('woodwork.material', string="Matériaux Utilisés")
    time_estimated = fields.Float(string="Temps Estimé (heures)", required=True)
    time_actual = fields.Float(string="Temps Réel (heures)")
    state = fields.Selection(
        selection_add=[
            ('draft', 'Brouillon'),
            ('in_progress', 'En Cours'), 
            ('done', 'Terminé'),
            ('cancelled', 'Annulé')
        ],
        ondelete={
            'draft': 'set default',
            'in_progress': 'set default',
            'done': 'set default',
            'cancelled': 'set default'
        }
    )

    @api.constrains('time_estimated')
    def _check_time_estimated(self):
        for task in self:
            if task.time_estimated <= 0:
                raise ValidationError("Le temps estimé doit être supérieur à zéro.")