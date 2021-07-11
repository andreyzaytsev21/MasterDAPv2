from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory


class EntityTemplate:

    def __init__(self, entity_template_json, property_template_factory: PropertyTemplateFactory):
        self.key_property = entity_template_json['key_property']
        self.properties_templates = list(map(
            lambda property_template_json:
            property_template_factory.load_property_template(property_template_json),
            entity_template_json['properties']
        ))
