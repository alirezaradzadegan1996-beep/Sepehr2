
from core.templates.template_creator import template_creator


class TemplateBrain:


    def get(self,project_type,features):

        result=template_creator.create(
            project_type,
            features
        )

        return result



template_brain=TemplateBrain()
