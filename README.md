Lista wydatków

z przegladarki:
/expenses/                        - formularz wyświatlający liste wydatkow
/expenses/<id>                    - formularz pozwalajacy na zmiane wybranego wydatku

REST API:
GET    /api/v1/expenses/          - pobranie listy wydatkow
POST   /api/v1/expenses/          - utworzenie nowego wydatku
GET    /api/v1/expenses/<id>      - pobranie szczegółów wydatku dla danego id
DELETE /api/v1/expenses/<id>      - usunięcie wydatku o danym id
PUT    /api/v1/expenses/<id>      - update wybranego wydatku (nadpisanie całego zasobu)