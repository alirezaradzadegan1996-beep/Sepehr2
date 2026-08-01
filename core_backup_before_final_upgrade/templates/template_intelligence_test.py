
from core.templates.request_understanding import request_understanding
from core.templates.adaptive_template_manager import adaptive_template_manager


tests=[
"یک اپ بیمارستان بساز",
"یک اپ ادیت عکس بساز",
"یک فروشگاه اینترنتی بساز"
]


for t in tests:

    intent=request_understanding.analyze(t)

    print(t)
    print(intent)

    print(
    adaptive_template_manager.get_template(
        intent["project_type"],
        intent["features"]
    ))
