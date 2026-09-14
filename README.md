# Indonesia Halal BPJPH Assurance & BPOM 2D QR Compliance

Halal Assurance System (SJPH/BPJPH), BPOM 2D Barcode Serialization, NIE Management, and Batch Recall for Odoo 18

## Odoo Apps Store

This repository contains the Odoo 18 module package for `airiv_halal_bpom_indonesia`.

Required store assets are maintained in:

```text
airiv_halal_bpom_indonesia/static/description/
  icon.png
  banner.png
  index.html
```

## Technical

- Odoo version: `18.0.1.0.0`
- License: `LGPL-3`
- Author: `AIRIV`
- Website: `https://airiv.id`

## Quality Gate

GitHub Actions runs the AIRIV Odoo Apps Store CI audit on branch `18.0`.

## Core Capabilities & Architecture

- Halal status, BPOM registration, certificate number, validity, and owner tracking.
- Ingredient, supplier, composition, and evidence traceability.
- Missing-document, expiry, approval, and renewal readiness review.

The module connects product and supplier context to an AIRIV compliance registry and release-readiness workflow.

## Feature & Workflow Automation

1. Configure compliance categories, document types, owners, and review cadence.
2. Register products, ingredients, suppliers, halal data, and BPOM references.
3. Attach certificates and supporting evidence.
4. Resolve action-required items and monitor renewal readiness.

## Installation Guidance

Clone branch `18.0` into the Odoo addons path, restart Odoo, update the Apps list, and install the module. Configure compliance context before product review.

## Configuration Checklist

- Confirm product composition, supplier, and registration references.
- Attach current halal, BPOM, ingredient, and supplier evidence.
- Review certificate and registration expiry dates.
- Assign owners and resolve release-blocking actions.

## Repository Layout

```text
airiv_halal_bpom_indonesia/
  models/                 Compliance and traceability models
  views/                  Review and registry views
  security/               Access rules
  static/description/     Apps Store assets
  __manifest__.py         Odoo metadata
```

## Contact Info

- Author: AIRIV
- Website: https://airiv.id
- GitHub: https://github.com/arivonto
- Repository: https://github.com/arivonto/airiv_halal_bpom_indonesia
- Odoo series: `18.0`
