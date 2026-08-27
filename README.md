# Indonesia Halal BPJPH Assurance & BPOM 2D QR Compliance

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Regulatory: BPJPH & BPOM RI](https://img.shields.io/badge/Regulatory-BPJPH%20%26%20BPOM%20RI-emerald.svg)](https://airiv.id)

A specialized regulatory compliance and batch serialization suite built specifically for **Odoo 18.0 Community Edition**. Designed for Indonesian Food & Beverage (F&B), Cosmetics, Herbal/Traditional Medicine (*Jamu*), and Pharmaceutical businesses facing mandatory **BPJPH Halal (UU No. 33/2014 & PP No. 39/2021)** and **Badan POM RI 2D Barcode Serialization** audits.

---

## Detailed Capabilities

### 1. Halal Assurance System (SJPH / BPJPH Kemenag)
* **BPJPH Halal Certificate Management**: Tracks official Halal ID numbers (`ID31110000123450123`), validity dates, and accredited auditing agencies (*LPH LPPOM MUI, Sucofindo, Surveyor Indonesia*).
* **Critical Control Points (Titik Kritis Halal)**: Categorizes materials into Low (Positive List), Medium, and High (Animal derivative/fermentation) critical risk levels.
* **Master Product Linkage**: Real-time validation badges showing active Halal certification status across product variants.

### 2. BPOM 2D Barcode Serialization & NIE Management
* **Multi-Category NIE Validation**: Supports BPOM RI MD (Domestic Food), ML (Imported Food), NA (Cosmetics & Skincare), TR (Herbal/Traditional), SD (Supplements), and DKL (Pharmaceuticals).
* **Standard 2D QR Payload Generator**: Automatically compiles regulatory 2D serialization strings:
  `BPOM|<NIE>|<BATCH_NUMBER>|<EXPIRY_DATE_YYYYMMDD>|<SERIAL_TOKEN>`
* **Lot Expiry & FEFO Integration**: Direct link to native Odoo stock tracking and First Expired, First Out dispatching.

### 3. Quality Assurance, Quarantine & Emergency Batch Recall
* **3-Stage Traceability Status**: `Released` (Lolos QC), `Quarantine` (Uji Lab), and `Recalled` (Ditarik dari Pasar).
* **Automated Audit Trail**: Captures recall reasons, lab contamination notes, and blocks outbound deliveries for flagged batches.

---

## Validated Commercial Benchmark (End-to-End Audit)

The compliance workflow was verified under live Odoo 18.0 Community conditions:

1. **Halal Certificate Registration**: Registered Halal Certificate `ID31110000123450123` issued by BPJPH / LPH LPPOM MUI (valid through 2030).
2. **Product NIE Association**: Linked product `Kopi Susu Gula Aren 250ml` with BPOM NIE `MD 268831001001` and active Halal status.
3. **BPOM 2D Barcode Serialization**: Generated standard 2D QR payload `BPOM|MD 268831001001|LOT-202608-001|20261231|2AD6E3D9` with unique serial batch token.
4. **Emergency Recall Quarantine**: Successfully transitioned batch status from `Released` to `Quarantine` and locked to `Recalled` with lab investigation logging.

---

## Installation & Odoo Configuration Guide

1. **Deploy Module**:
   Place `airiv_halal_bpom_indonesia` inside your Odoo `custom_addons` directory.

2. **Activate Module**:
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia Halal BPJPH Assurance & BPOM 2D QR Compliance` and click **Activate**.

3. **Configure Halal Certificates & NIE**:
   * Open **Halal & BPOM > Sertifikat Halal BPJPH** to register company Halal IDs.
   * Enter BPOM NIE numbers on the product template under the **Halal & BPOM RI** tab.
   * Generate 2D QR serialization codes directly from **Serialisasi Lot & 2D QR**.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL & App Drawer compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `base`, `product`, `stock`, `product_expiry`, `account` |
| **Regulatory Standards** | UU No. 33/2014, PP No. 39/2021, Peraturan BPOM No. 22/2022 |
| **Server Overhead** | Zero (Native ORM, direct SQL aggregation) |
