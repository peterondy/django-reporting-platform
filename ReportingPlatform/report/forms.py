from dataclasses import fields
from pyexpat import model
from unicodedata import category
from django import forms
from .models import subCategory

class subCategoryCreationForm(forms.ModelForm):
    class Meta:
        model = subCategory
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subName'].queryset = subCategory.objects.all()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subCategory'].queryset = subCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass # invalid form
        elif self.instance.pk:
            self.fields['subCategory'].queryset = self.instance.category.subCategory_set.order_by('name')