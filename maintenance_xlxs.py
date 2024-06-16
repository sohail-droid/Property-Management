import io
import json
import xlsxwriter
from odoo import models
from odoo.tools import date_utils

class MaintenanceRequestXlsx(models.AbstractModel):
    # _inherit = 'maintenance.request'
    _name = 'report.property_management_newupdates.report_maintenance_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, maintenance):
        format = workbook.add_format({'font_size': 14, 'align': 'center', 'bold': True, 'bg_color': 'yellow'})
        bold = workbook.add_format({'bold': True})
        # bordered = workbook.add_format({'border': 1})  # Add border to cells

        for obj in maintenance:
            sheet = workbook.add_worksheet(obj.name)  # sheet name
            row = 3
            col = 3
            # sheet.set_column('A:A', 15)
            # sheet.set_column('B:B', 15)

            row = row + 1
            sheet.merge_range(row, col, row, col + 3, 'Maintenance Report Details', format)

            # if obj.image:
            #     user_image = io.BytesIO(base64.b64decode(obj.image))
            #     sheet.insert_image(row, col, "image.png", {"image_data": user_image, 'x_scale': 0.5, 'y_scale': 0.5})

            row = row + 6
            sheet.write(row, col, 'Name', bold)
            sheet.write(row, col + 1, obj.name)

            row = row + 1
            sheet.write(row, col, 'Apartment Name', bold)
            sheet.write(row, col + 1, obj.apartment_issue_id)

            sheet.write(row, col, 'Duration', bold)
            sheet.write(row, col + 3, obj.duration)

            row = row + 1
            sheet.write(row, col, 'Created By', bold)
            sheet.write(row, col + 1, obj.employee_id)

            sheet.write(row, col, 'Renters Fault', bold)
            sheet.write(row, col + 3, obj.renters_fault)

            row = row + 1
            sheet.write(row, col, 'Team', bold)
            sheet.write(row, col + 3, str(obj.maintenance_team_id))

            row = row + 1
            sheet.write(row, col, 'Service Handler Name', bold)
            sheet.write(row, col + 1, obj.user_id)

            row = row + 1
            sheet.write(row, col, 'Requested Date', bold)
            sheet.write(row, col + 1, obj.request_date)

            row = row + 1
            sheet.write(row, col, 'Scheduled Date', bold)
            sheet.write(row, col + 1, obj.schedule_date)

            row = row + 1
            sheet.write(row, col, 'Maintenance Type', bold)
            sheet.write(row, col + 1, obj.maintenance_type)

            row = row + 2

            # sheet.write(row, 0, obj.name)
            # sheet.write(row, 1, obj.company_id.name)
            # sheet.write(row, 2, obj.apartment_issue_id.name)
            # sheet.write(row, 3, obj.employee_id.name)
            # sheet.write(row, 4, obj.user_id.name)
            # sheet.write(row, 5, str(obj.request_date))
            # sheet.write(row, 6, str(obj.schedule_date))
            # sheet.write(row, 7, obj.maintenance_type.name)
            # sheet.write(row, 8, obj.maintenance_team_id.name)
            # sheet.write(row, 9, obj.equipment_id.name)
            # sheet.write(row, 10, obj.maintenance_for)
            # sheet.write(row, 11, obj.cost)
            # sheet.write(row, 12, obj.renters_fault)

        # report_name = obj.name
        # One sheet by partner

        # sheet1 = workbook.add_worksheet(report_name[:31])
