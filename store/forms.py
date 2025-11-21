from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Store,Product

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields=['name','description']
        labels={
            'name':'اسم فروشگاه',
            'description':'توضیحات فروشگاه'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class':'form-control',
             'placeholder':'نام فروشگاه'
            }
        )
        self.fields['description'].widget.attrs.update(
            {'class':'form-control',
             'placeholder':'توضیحات فروشگاه'
            }
        )

        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','description','image']
        labels={
            'name':'اسم محصول',
            'price':'قیمت محصول',
            'description':'توضیحات محصول',
            'image':'عکس محصول',
        }  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class':'form-control',
             'placeholder':'نام محصول'
            }
        )
        self.fields['price'].widget.attrs.update(
            {'class':'form-control',
              'placeholder':'قیمت محصول'
            }
        )
        self.fields['description'].widget.attrs.update(
            {'class':'form-control',
             'placeholder':'توضیحات محصول'
            }
        )
        self.fields['image'].widget.attrs.update(
            {'class':'form-control',
             'placeholder':'عکس محصول'
            }
        )
          

 
 
