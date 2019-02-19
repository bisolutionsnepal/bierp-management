# -*- coding: utf-8 -*-

# Copyright (C) 2019 BI Solutions (https://bisolutions.com.np).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SWOT_Attributes(models.Model):
    _name = 'swot.common_attributes'

    name = fields.Char(required=True, string='Name')
    importance = fields.Selection([(1, 'Important'),(2, 'More Important'), (3, 'Most Important')], string='Importance')


class Strength(models.Model):
    _name = 'swot.strength'
    _rec_name = 'name'
    _inherit = 'swot.common_attributes'

    rating = fields.Selection([(1, 1), (2, 2), (3, 3)], string='Rating')
    score = fields.Float(compute='compute_score')
    swot_id = fields.Many2one(comodel_name='swot.swot')

    @api.depends('importance', 'rating')
    def compute_score(self):
        for record in self:
            record.score = record.importance * record.rating


class Weakness(SWOT_Attributes):
    _name = 'swot.weakness'
    _rec_name = 'name'
    _inherit = 'swot.common_attributes'

    rating = fields.Selection([(1, 1), (2, 2), (3, 3)], string='Rating')
    score = fields.Float(compute='compute_score')
    swot_id = fields.Many2one(comodel_name="swot.swot")

    @api.depends('importance', 'rating')
    def compute_score(self):
        for record in self:
            record.score = record.importance * record.rating


class Opportunity(SWOT_Attributes):
    _name = 'swot.opportunity'
    _rec_name = 'name'
    _inherit = 'swot.common_attributes'

    probability = fields.Selection([(1,'Low'), (2, 'Medium'), (3, 'High')], string='Probability')
    score = fields.Float(compute='compute_score')
    swot_id = fields.Many2one(comodel_name='swot.swot')


    @api.depends('importance', 'probability')
    def compute_score(self):
        for record in self:
            record.score = record.importance * record.probability


class Threat(SWOT_Attributes):
    _name = 'swot.threat'
    _rec_name = 'name'
    _inherit = 'swot.common_attributes'

    probability = fields.Selection([(1,'Low'), (2, 'Medium'), (3, 'High')], string='Probability')
    score = fields.Float(compute='compute_score')
    swot_id = fields.Many2one(comodel_name="swot.swot")

    @api.depends('importance', 'probability')
    def compute_score(self):
        for record in self:
            record.score = record.importance * record.probability


class SWOT(models.Model):
    _name = 'swot.swot'
    _rec_name = 'swot_name'

    swot_name = fields.Char(string='Name')
    swot_date = fields.Date(required=True, string='Date')
    swot_version = fields.Float()
    swot_of = fields.Selection(
    [('individual','Individual'),('department','Department'),('company','Company')],string='SWOT Of',
    default='individual')
    individual_id = fields.Many2one('hr.employee', ondelete='cascade', string="Person's Name")
    department_id = fields.Many2one('hr.department', ondelete='cascade', string='Department')
    company_id = fields.Many2one('res.company', ondelete='cascade', string='Company')
    strength_ids = fields.One2many(comodel_name='swot.strength', inverse_name='swot_id', string='Strengths')
    weakness_ids = fields.One2many(comodel_name='swot.weakness', inverse_name='swot_id', string='Weaknesses')
    opportunity_ids = fields.One2many(comodel_name='swot.opportunity', inverse_name='swot_id', string='Opportunities')
    threat_ids = fields.One2many(comodel_name='swot.threat', inverse_name='swot_id', string='Threats')
