import re
import steamreviews
from time import sleep
from mytypes import columns

request_params = {
    'language': 'russian'
}
# Взял из раздела Новинки (02.08.2023)
# https://store.steampowered.com/app/2239150/Thronefall/
# Можно посмотреть что за игра по id вот так
# https://steamdb.info/app/20/
start_app_id = 1911590
max_app_id = 2239150
columns = columns

for app_id in range(start_app_id, max_app_id+1):
    print('app {} fetching  ...'.format(app_id))
    result, query_count = steamreviews.download_reviews_for_app_id(app_id, chosen_request_params=request_params)
    print('app {} fetched in {} queries'.format(app_id, query_count))
    print('app {} total reviews count is {}'.format(app_id, result['query_summary']['total_reviews']))
    if result['query_summary']['total_reviews'] > -1 and 'reviews' in result:
        filename = '{}.csv'.format(app_id)
        with open(filename, 'w+') as f:
            # можно добавить заголовки в каждый файл, но потом сложней их склеивать будет
            # f.write('{}\n'.format(';'.join(columns)))
            for item in result['reviews'].values():
                data = []
                for column in columns:
                    value = ''
                    if column.find('.') > -1:
                        left, sep, right = column.partition('.')
                        if left in item and right in item[left]:
                            value = str(item[left][right])
                    else:
                        if column in item:
                            value = str(item[column])

                    if not (value.isnumeric() or value.startswith('0.') or (value == 'True' or value == 'False')):
                        parts = re.findall(r'[a-zа-яйёА-ЯЙЁ0-9.,!?:\s]+', value, re.IGNORECASE | re.MULTILINE)
                        value = '"{}"'.format('\n'.join(parts))
                        value = re.sub(r'\s+', ' ', value)

                    data.append(value)

                f.write('{}\n'.format(';'.join(data)))
        print('app {} file {} saved'.format(app_id, filename))

    sleep(2)
