from rest_framework.serializers import ValidationError

def special_character(value):
    special_characters = "!#$%^&*()_~`<>/:|;][}{,.=+-"
    if any(c in value for c in special_characters):
        raise ValidationError("fields should not contain special characters")
