# -*- coding: utf-8 -*-
from odoo import fields, models


class ContactUs(models.Model):
    _name = 'contact.us'
    _description = 'Contact Us'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    message = fields.Text(string='Message')
    
