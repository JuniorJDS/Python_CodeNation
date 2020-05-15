from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]


def calc_tarifa(start, end):
    hora_6 = datetime(start.year, start.month, start.day, 6)
    hora_22 = datetime(start.year, start.month, start.day, 22)

    if (start >= hora_22) or (end < hora_6):
        return 0.36

    if end >= hora_22:
        end = hora_22

    if start < hora_6:
        start = hora_6

    minuto = int((end - start).seconds / 60)
    tarifa = minuto * 0.09 + 0.36

    return tarifa


def classify_by_phone_number(records):
    resultado = []
    for record in records:

        start = datetime.fromtimestamp(record['start'])
        end = datetime.fromtimestamp(record['end'])

        tarifa = calc_tarifa(start, end)

        count = 0
        for i in range(len(resultado)):
            if record['source'] == resultado[i]['source']:
                count = 1
                resultado[i]['total'] += tarifa

        if count == 0:
            resultado.append(
                {'source': record['source'], 'total': round(tarifa, 2)})
    resultado = sorted(resultado, key=lambda k: k['total'], reverse=True)

    return resultado
