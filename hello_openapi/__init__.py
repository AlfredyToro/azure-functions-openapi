import json
import azure.functions as func
from azure_functions_openapi.decorator import openapi

@openapi(
    summary="Greet user",
    route="/api/http_trigger",
    request_model={"name": "string"},
    response_model={"message": "string"},
    tags=["Example"]
)
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        name = data.get("name", "world")
        return func.HttpResponse(
            json.dumps({"message": f"Hello, {name}!"}),
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)
