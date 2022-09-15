from bitrix24 import Bitrix24, BitrixError


async def create_lid(title, name, last_name, second_name, phone, company_name, product_id: int, price: float):
    bx24 = Bitrix24('https://b24.kalibr.co/rest/484/ajbtz1jwhheaq3fj')
    try:
        result = bx24.callMethod('crm.lead.add',
                                 fields={
                                     'TITLE': title,
                                     'NAME': name,
                                     'SECOND_NAME': second_name,
                                     "LAST_NAME": last_name,
                                     "STATUS_ID": "NEW",
                                     "OPENED": "Y",
                                     "ASSIGNED_BY_ID": 232,
                                     "CURRENCY_ID": "RUB",
                                     "PHONE": [{"VALUE": phone, "VALUE_TYPE": "WORK"}],
                                     "UF_CRM_1550213429": 68,
                                     "SOURCE_ID": 15,
                                     "COMPANY_TITLE": company_name

                                 },
                                 params={
                                     "REGISTER_SONET_EVENT": "Y"
                                 }
                                 )
        rows = {
            'id': result,
            'rows': {'PRODUCT_ID': product_id, 'PRICE': price, 'QUANTITY': 1}
        }
        bx24.callMethod('crm.lead.productrows.set', id=result, rows=rows)
    except BitrixError as message:
        print(message)
