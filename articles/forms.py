from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        print('clean')
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"\"{title}\" is already in use. Please choose other title.")

class ArticleFormOld(forms.Form):
    title=forms.CharField()
    content=forms.CharField()

    
   

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # dictionary
    #     title = cleaned_data.get('title')
    #     print("title",title)
    #     if title.lower().strip()=="the office":
    #             raise forms.ValidationError('this tittle is taken.')
    #     return title

    # asi limpiamos todos los campos del formulario y no solo tittle.
    def clean(self):
        cleaned_data = self.cleaned_data  # dictionary
        print('all data ',cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip()=="the office":
                self.add_error('title','This tittle is take')
                #raise forms.ValidationError('this tittle is taken.')
        if "office" in content.lower() or "office" in title.lower():
            self.add_error('content','Office can not be in content')
            raise forms.ValidationError('Office is not allowed')
        return cleaned_data

        
        