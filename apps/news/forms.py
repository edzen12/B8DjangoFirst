from django import forms 
from apps.news.models import Comment, News


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category','title','description','image']
        