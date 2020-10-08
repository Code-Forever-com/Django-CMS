class UI():
    def __init__(self,model,m_object):
        self.model = model
        self.object = m_object

    def get_fields(self):
        self.fields = self.model._meta.get_fields()

    def header