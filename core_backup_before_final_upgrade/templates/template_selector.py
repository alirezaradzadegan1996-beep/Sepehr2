from core.templates.template_engine import template_engine
from core.templates.template_creator import template_creator


class TemplateSelector:


    def select(self,name,features):

        result = template_engine.get_or_create(
            name,
            features
        )

        return result



template_selector=TemplateSelector()
