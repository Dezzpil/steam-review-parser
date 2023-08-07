# steam-review-parser

Перед началом сбора отзывов, необходимо указать start_app_id и max_app_id, в `parser.py`.
```shell
python parser.py
```

Парсер создает отдельный *.csv файл для отзывов каждой игры формата `app_id.csv` в корне.

Степлер сшивает все *.csv в корне в один файл - stapled.csv
```shell
python stapler.py
```

Структуру данных описана в `mytypes.py` - поля как есть берутся из Steam API