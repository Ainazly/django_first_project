from django import forms


class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dict{}
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     print(title)
    #     if title.lower().strip() == "tree":
    #         raise forms.ValidationError('This title already exists !')
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if title and description:
            if title.lower().strip() == "tree":
                self.add_error('title', 'This title already exists ! ')
            if 'hey' in description or 'hey' in title:
                self.add_error('description', "This description not a correct !")
            if 'python is not the best language'.lower().strip() in description:
                self.add_error('description', "Correct")
        return cleaned_data

