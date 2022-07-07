
from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description ="Estate property"

    name = fields.Char("Title",required="True")
    description= fields.Text('description')
    date_availability = fields.Date('date_availability' )
    expected_price = fields.Float('expected_price', null = False ,required=True)
    selling_price = fields.Float('selling_price')
    bedrooms = fields.Integer("bedrooms")
    living_area = fields.Integer("living_area")
    facades = fields.Integer("facades")
    garage = fields.Boolean("garage")
    garden = fields.Boolean("garden")
    garden_area = fields.Integer("garden_area")
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('North', 'North'), ('South', 'South'), ('East','East'),('West','West')],)
garden_area = fields.Integer("garden_area")
