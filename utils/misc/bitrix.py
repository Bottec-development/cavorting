from bitrix24 import Bitrix24, BitrixError


async def create_lid():
    bx24 = Bitrix24('https://b24.kalibr.co/rest/484/ajbtz1jwhheaq3fj')
    try:
        result = bx24.callMethod('crm.lead.add',
                                 fields={
                                     'TITLE': "Тестовый лид",
                                     'NAME': "Имя",
                                     'SECOND_NAME': "Отчество",
                                     "LAST_NAME": "Фамилия",
                                     "STATUS_ID": "NEW",
                                     "OPENED": "Y",
                                     "ASSIGNED_BY_ID": 232,
                                     "CURRENCY_ID": "RUB",
                                     "OPPORTUNITY": 12500,
                                     "PHONE": [{"VALUE": "79779678576", "VALUE_TYPE": "WORK"}],
                                     "UF_CRM_1550213429": 68,
                                     "SOURCE_ID": 15,
                                     "COMPANY_TITLE": "Тестовое название компании"

                                 },
                                 params={
                                     "REGISTER_SONET_EVENT": "Y"
                                 }
                                 )
        rows = [
            {"PRODUCT_ID": 689, "PRICE": 100.00, "QUANTITY": 2},
            {"PRODUCT_ID": 690, "PRICE": 200.00, "QUANTITY": 1}
        ]

        bx24.callMethod('crm.lead.productrows.set', id=result, rows=rows)
    except BitrixError as message:
        print(message)
