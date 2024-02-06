from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]
        print(f"Estou criando  o produto {product_code}")
        print("Estou na minha view")       
        return HttpResponse(status_code=200, body={"tag": "ok"})
