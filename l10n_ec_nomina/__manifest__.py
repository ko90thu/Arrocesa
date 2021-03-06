{
    'name': 'Nómina for Ecuador',
    'version': '12.0',
    'author': 'OPA Consulting',
    'category': 'Localization',
    'complexity': 'normal',
    'license': 'AGPL-3',
    'website': 'http://wwww.opa-consulting.com',
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/comision.xml",
        "views/rama.xml",
        "views/cargo.xml",
        "views/employee.xml",
        "views/gastos_personales_empl.xml",
        "views/employee_bank.xml",
        "views/imp_renta_pernat.xml",
        "views/employee_pay_fortnight.xml",
        "views/generate_pay_fortnight.xml",
        "views/employees_payfortnight.xml",
        "views/hr_payslip_run.xml",
        "views/account_payment_payroll.xml",
        "views/res_config_settings.xml",
        "wizard/vacation_report_template.xml",
        "wizard/vacation_report.xml",
        "views/hr_settlement_type_view.xml",
        "wizard/settlement_report_template.xml",
        "wizard/settlement_report_view.xml",
        "wizard/tenths_report_template.xml",
        "wizard/tenths_report_view.xml",
        "wizard/wizard_impuesto_renta.xml",
        "wizard/impuesto_renta_template.xml",
        "wizard/wizard_rdep.xml",
        "views/template_report_payslip.xml",
        "data/comisiones.xml",
        "data/ramas.xml",
        "data/cargos.xml",
        "data/categorias_reglas_salariales_parent.xml",
        "data/categorias_reglas_salariales.xml",
        "data/reglas_salariales.xml",
        "data/imp_renta_pernat.xml",
        "data/payment_method.xml",
        "data/settlement_type.xml",
        "data/account_journal.xml",
        "data/data_template_payslip.xml",
        
    ],
    'qweb': [
        
    ],
    'depends': [
        'hr',
        'hr_payroll',
        'hr_payroll_account',
        'hr_employee_updation',
        'account_batch_payment',
        'l10n_ec_partner',
        'l10n_ec_hr_employee',
        'l10n_ec_withholding',
    ],
    'installable': True,
}
