# Открытые данные извлеченные из проекта ristat.org (Электронный архив Российской исторической статистики)

## Описание

Данные массивы данных являются копией данных извлеченных из электронного архива Российской исторической статистики (ristat.org) и преобразованные в форматы пригодные для последующего использования.
Целью данной работы было преобразование данных в форматы CSV, JSON, BSON и предоставление их широкому кругу разработчиков.

## Структура
* zip - оригинальные файлы из ristat.org по группам и подгруппам
* data - результаты распаковки zip файлов. Файлы в форматах .xlsx и описание данных в .docx и .pdf
* csv - преобразованные данные из .xlsx файлов
* scripts - программы/скрипты использованные для преобразования данных
* fulldb - сведенные вместе данные в CSV, преобразованные в единый CSV файл (full_db.csv) и JSON файл в виде записей по одной записи на строку (newline JSON) - fulldb_newline.json, а также файл BSON для быстрой загрузки данных в базу MongoDB


## Как использовать данные

Вы можете воспользоваться любым инструментом работы с CSV файлами для любого языка программирования или загрузить данные в MongoDB и делать запросы к базе в MongoDB.
Описание методологии Вы найдете в файлах .docx в папке data.

А также на сайте проекта http://ristat.org

## Источник информации
Кесслер Хайс и Маркевич Андрей (2014), Электронный архив Российской исторической статистики, XVIII – XXI вв., [Электронный ресурс] : [сайт]. — Режим доступа: http://ristat.org/

## Условия использования
Это произведение доступно по лицензии Creative Commons «Attribution-NonCommercial-ShareAlike» («Атрибуция — Некоммерческое использование — На тех же условиях») 4.0 Всемирная.
http://creativecommons.org/licenses/by-nc-sa/4.0/deed.ru