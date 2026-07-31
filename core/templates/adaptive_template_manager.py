from core.templates.template_engine import template_engine


class AdaptiveTemplateManager:


    name = "adaptive_template_manager"


    def get_template(self, project_type, features):

        return template_engine.get_or_create(
            project_type,
            features
        )


adaptive_template_manager = AdaptiveTemplateManager()
