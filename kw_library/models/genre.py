import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Genre(models.Model):
    _name = 'kw.lib.genre'
    _description = 'Genre'

    name = fields.Char()
    active = fields.Boolean(default=True)
