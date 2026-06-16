# utils/allure_helper.py
import allure

def attach_json(name, data):
    allure.attach(
        str(data),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )

def attach_text(name, data):
    allure.attach(
        str(data),
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )