from odoo import api, fields, models
from datetime import date
class UserProducts(models.Model):
    _name = "user.products"
    _description = "Products"

    name = fields.Char(string="Name")
    price = fields.Float(string="Price:")
    exp_date=fields.Date(string="Expiry Date")