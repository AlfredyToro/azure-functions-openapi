import json
import azure.functions as func
from azure_functions_openapi.decorator import openapi
from azure_functions_openapi.openapi import get_openapi_json, get_openapi_yaml
from azure_functions_openapi.swagger_ui import render_swagger_ui

app = func.FunctionApp()

@openapi(
    summary="Greet user",
    route="/api/http_trigger",
    request_model={"name": "string"},
    response_model={"message": "string"},
    tags=["Example"]
)
@app.function_name(name="http_trigger")
@app.route(route="/api/http_trigger", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
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

@app.function_name(name="openapi_json")
@app.route(route="/api/openapi.json", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def openapi_json(req: func.HttpRequest) -> func.HttpResponse:
    return get_openapi_json()

@app.function_name(name="openapi_yaml")
@app.route(route="/api/openapi.yaml", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def openapi_yaml(req: func.HttpRequest) -> func.HttpResponse:
    return get_openapi_yaml()

@app.function_name(name="swagger_ui")
@app.route(route="/api/docs", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def swagger_ui(req: func.HttpRequest) -> func.HttpResponse:
    return render_swagger_ui()