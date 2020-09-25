from .models import *

def generate_form(form_slug):
    form = Forms.objects.filter(slug=form_slug).first()
    if form:
        formfileldsstorage = FormFieldsStorage.objects.filter(form=form.id)
        fields = list()
        for form_field in formfileldsstorage:
            field = FormFields.objects.filter(id=form_field.id).first()
            fields.append( field )
        form.fields = fields

    return form

def get_form_fields(formID):
    form = Forms.objects.filter(id=formID).first()
    if form:
        formfileldsstorage = FormFieldsStorage.objects.filter(form=form.id)
        fields = list()
        for form_field in formfileldsstorage:
            field = FormFields.objects.filter(id=form_field.id).first()
            fields.append( field )

    return fields
