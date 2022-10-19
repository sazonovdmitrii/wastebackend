from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
	return JsonResponse({'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NjYyMDk1NjYsImV4cCI6MTY2NjIxMzE2Niwicm9sZXMiOlsiUk9MRV9BRE1JTiJdLCJ1c2VybmFtZSI6InNhem9uQG54dC5ydSJ9.Jc9jhbt5u7l0PkCcTV-4EGXv1zGCNxbHaxM3Bo1oEkYd3fXGWHR8YEy_bFpJlq0TXXFqFjvSPMJgy2msLphGKf89KXMpv7DDDBsmy2Gn9GaJCmdgdvsvvRsxWdAQGGPFdnWWnW9QYUEzil8LYFQZD6FZAdO3GmzhCrOGJUZ_M80v66RRzhCcyXAsVyqSM3XR88PjWGCC-eo9saxkYPxyKZ2vgmtDIkonVZOqbZpktBVB-qZudQokbqivQ1nc80GJwSLj8Pq9jCA0D_DNNNrge3bWo_bfePDl4KOaHWfT1lIZv3_8LkA6GeviuY1J3tb_cDkhSKYHydFVkWMZ2Fac8A'})

def account(request):
	return JsonResponse(
		{
			'email': 'sazon@nxt.ru',
			'phone': '79889917443',
			'firstname': 'Дмитрий',
			'lastname': 'Сазонов'
		}
	)

def sendsms(request):
	return JsonResponse(
		{"success": 'true'}
	)

def checksms(request):
	return JsonResponse(
		{"success": 'true'}
	)
