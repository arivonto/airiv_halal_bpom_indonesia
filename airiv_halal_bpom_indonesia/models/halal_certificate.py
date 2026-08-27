# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HalalCertificate(models.Model):
    _name = 'halal.certificate'
    _description = 'Sertifikat Halal BPJPH / MUI'
    _rec_name = 'certificate_number'
    _order = 'validity_end desc, id desc'

    name = fields.Char(string="Nama Ketetapan Halal", required=True, default="Sertifikat Halal BPJPH")
    certificate_number = fields.Char(string="Nomor Sertifikat Halal (ID/SH)", required=True, index=True,
                                     help="Nomor ID Sertifikat Halal resmi dari BPJPH Kemenag (misal: ID31110000123450123)")
    
    company_id = fields.Many2one('res.company', string="Perusahaan / Pelaku Usaha", default=lambda self: self.env.company, required=True)
    issuing_authority = fields.Selection([
        ('bpjph', 'BPJPH Kemenag RI'),
        ('mui', 'LPPOM MUI'),
        ('foreign_lph', 'Lembaga Halal Luar Negeri Terakreditasi'),
    ], string="Lembaga Penerbit", default='bpjph', required=True)

    lph_name = fields.Char(string="Nama LPH (Lembaga Pemeriksa Halal)", default="LPH LPPOM MUI", help="LPH yang mengaudit (LPPOM MUI, Sucofindo, Surveyor Indonesia, dll.)")
    validity_start = fields.Date(string="Tanggal Terbit", default=fields.Date.today, required=True)
    validity_end = fields.Date(string="Berlaku Hingga", required=True)
    
    scope = fields.Selection([
        ('product', 'Produk Jadi (Makanan / Minuman / Kosmetik)'),
        ('raw_material', 'Bahan Baku / Tambahan Pangan'),
        ('facility', 'Fasilitas / Dapur / Rumah Potong Hewan'),
        ('service', 'Jasa Penyimpanan / Logistik / Distribusi'),
    ], string="Ruang Lingkup", default='product', required=True)

    state = fields.Selection([
        ('draft', 'Pengajuan / Audit LPH'),
        ('valid', 'Aktif & Bersertifikat'),
        ('expired', 'Kadaluarsa / Perlu Perpanjangan'),
    ], string="Status Sertifikasi", default='valid', compute="_compute_certificate_state", store=True)

    product_ids = fields.One2many('product.template', 'halal_certificate_id', string="Daftar Produk Bersertifikat")
    product_count = fields.Integer(string="Jumlah Produk", compute="_compute_product_count")

    @api.depends('validity_end')
    def _compute_certificate_state(self):
        today = fields.Date.today()
        for rec in self:
            if not rec.validity_end:
                rec.state = 'draft'
            elif rec.validity_end < today:
                rec.state = 'expired'
            else:
                rec.state = 'valid'

    def _compute_product_count(self):
        for rec in self:
            rec.product_count = len(rec.product_ids)
