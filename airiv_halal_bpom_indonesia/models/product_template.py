# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplateTraceability(models.Model):
    _inherit = 'product.template'

    # Halal BPJPH Fields
    is_halal_certified = fields.Boolean(string="Bersertifikat Halal BPJPH", default=True)
    halal_certificate_id = fields.Many2one('halal.certificate', string="Sertifikat Halal BPJPH")
    halal_cert_number = fields.Char(related='halal_certificate_id.certificate_number', string="No. SH Halal", readonly=True)
    halal_critical_level = fields.Selection([
        ('low', 'Risiko Rendah (Bahan Alami Positif List)'),
        ('medium', 'Risiko Sedang (Bahan Olahan Terverifikasi)'),
        ('high', 'Risiko Kritis (Turunan Hewani / Fermentasi)'),
    ], string="Tingkat Titik Kritis Halal (SJPH)", default='low')

    # BPOM Serialization Fields
    requires_bpom = fields.Boolean(string="Wajib Izin BPOM", default=True)
    bpom_category = fields.Selection([
        ('md', 'Pangan Olahan Dalam Negeri (BPOM RI MD)'),
        ('ml', 'Pangan Olahan Impor (BPOM RI ML)'),
        ('pirt', 'Industri Rumah Tangga (P-IRT Dinas Kesehatan)'),
        ('na', 'Kosmetik & Perawatan (BPOM RI NA)'),
        ('tr', 'Obat Tradisional / Herbal / Jamu (BPOM RI TR)'),
        ('sd', 'Suplemen Kesehatan (BPOM RI SD)'),
        ('dkl', 'Obat Keras / Farmasi (BPOM RI DKL/GKL)'),
    ], string="Kategori Izin Edar", default='md')

    bpom_nie = fields.Char(string="Nomor Izin Edar (NIE BPOM)", index=True,
                           help="Nomor izin edar resmi dari Badan POM RI (misal: MD 268831001001 atau NA 18210100001)")
    bpom_nie_expiry = fields.Date(string="Masa Berlaku NIE BPOM")
