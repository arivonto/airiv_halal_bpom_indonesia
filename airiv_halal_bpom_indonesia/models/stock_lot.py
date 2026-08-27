# -*- coding: utf-8 -*-
import uuid
from odoo import models, fields, api, _

class StockLotTraceability(models.Model):
    _inherit = 'stock.lot'

    production_date = fields.Date(string="Tanggal Produksi", default=fields.Date.today, required=True)
    bpom_nie_number = fields.Char(related='product_id.bpom_nie', string="NIE BPOM Terdaftar", readonly=True)
    
    # Explicit Expiration Date fallback if product_expiry field is customized
    bpom_expiry_date = fields.Date(string="Tanggal Kedaluwarsa BPOM", default=fields.Date.today)
    
    # 2D Barcode Serial Payload
    bpom_qr_payload = fields.Char(string="2D QR Payload BPOM", compute="_compute_bpom_qr_payload", store=True,
                                  help="String payload terstandar untuk pencetakan 2D Barcode QR BPOM")
    
    serial_unique_code = fields.Char(string="Unique Serial / Batch Token", default=lambda self: uuid.uuid4().hex[:8].upper(), copy=False)
    
    # Quality & Recall Status
    traceability_status = fields.Selection([
        ('released', 'Lolos QC & Siap Distribusi (Released)'),
        ('quarantine', 'Karantina / Uji Laboratorium'),
        ('recalled', 'DITARIK DARI PASAR (RECALLED)'),
    ], string="Status Traceability", default='released', required=True)

    halal_batch_verified = fields.Boolean(string="Lolos Verifikasi Titik Kritis Halal", default=True)
    recall_reason = fields.Text(string="Alasan Penarikan / Investigasi Batch")

    @api.depends('name', 'product_id.bpom_nie', 'production_date', 'bpom_expiry_date', 'serial_unique_code')
    def _compute_bpom_qr_payload(self):
        for lot in self:
            nie = lot.product_id.bpom_nie or 'NO-NIE'
            batch_name = lot.name or 'NO-BATCH'
            
            # Check native product_expiry field or fallback to bpom_expiry_date
            exp_val = getattr(lot, 'expiration_date', None) or lot.bpom_expiry_date
            if exp_val:
                exp = exp_val.strftime('%Y%m%d') if hasattr(exp_val, 'strftime') else str(exp_val).replace('-', '')
            else:
                exp = 'NOEXP'
                
            serial = lot.serial_unique_code or '0000'
            # Format: BPOM|NIE|BATCH|EXP|SERIAL (Standar 2D Barcode BPOM RI)
            lot.bpom_qr_payload = f"BPOM|{nie}|{batch_name}|{exp}|{serial}"

    def action_quarantine_batch(self):
        self.write({'traceability_status': 'quarantine'})

    def action_release_batch(self):
        self.write({'traceability_status': 'released'})

    def action_emergency_recall_batch(self):
        self.write({'traceability_status': 'recalled'})
