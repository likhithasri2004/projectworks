from django.db import connection
from django.http import JsonResponse

def fetch_employees(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM company_db.dbo.Employees")
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
    return JsonResponse(data, safe=False)