# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Invoice in cash statement lines',
    'summary': 'Add seleccion of invoice in cash statement lines',
    'version': '11.0.1.0.0',
    'category': 'Account',
    'website': 'comunitea.com, Aresoltec Canarias',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'account'
    ],
    'data': [
        'views/account_bank_statement_line_view.xml',
    ],
}
