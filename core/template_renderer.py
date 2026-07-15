class TemplateRenderer:

    def render(self, text, context):

        for key, value in context.items():

            text = text.replace(
                "{{" + key + "}}",
                str(value)
            )

        return text
