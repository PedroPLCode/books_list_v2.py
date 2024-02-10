Lista wydatków

DOSTEP Z PRZEGLADARKI:
/expenses/                          - formularz wyświatlający liste wydatkow
/expenses/<id>                      - formularz pozwalajacy na zmiane wybranego wydatku

REST API:
GET    /api/v1/expenses/            - pobranie listy wszystkich wydatkow
GET    /api/v1/expenses/?paid=true  - pobranie listy wydatkow przefiltrowanych po parametrze paid (true/false)
POST   /api/v1/expenses/            - utworzenie nowego wydatku
GET    /api/v1/expenses/<id>        - pobranie szczegółów wydatku dla podanego id
DELETE /api/v1/expenses/<id>        - usunięcie wydatku o podanym id
PUT    /api/v1/expenses/<id>        - update wybranego wydatku (nadpisanie całego zasobu)