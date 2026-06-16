import allure
from pytest_bdd import given, when, then, scenario

from config.paths import FEATURES_PATH

from clients.post_client import PostClient
from fixtures.context import valid_post_payload
from utils.allure_helper import attach_json, attach_text

client = PostClient()


@scenario(FEATURES_PATH, "Successfully create a new post")
def test_post_success():
    pass


@given("user has valid post payload")
@allure.step("Given user has valid post payload")
def payload(context):
    context["payload"] = valid_post_payload()
    attach_json("Request Payload", context["payload"])


@when("user sends POST request to create post")
@allure.step("When user sends POST request to create post")
def send_request(context):
    response = client.create_post(context["payload"])
    context["response"] = response

    attach_text("Status Code", response.status_code)
    attach_json("Response Body", response.text)


@then("response status code should be 201")
@allure.step("Then response status code should be 201")
def check_status(context):
    assert context["response"].status_code == 201


@then("response should contain id")
@allure.step("And response should contain id")
def check_body(context):
    response_json = context["response"].json()

    attach_json("Final Response JSON", response_json)

    assert "id" in response_json