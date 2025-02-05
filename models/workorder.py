from odoo import models, fields

class WorkOrder(models.Model):
    _name = 'woodworking.workshop.workorder'
    _description = 'Work Order'

    name = fields.Char(string='Name', required=True)
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        required=True,
        ondelete='cascade'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True)