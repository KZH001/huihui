#coding=utf-8
from django import forms
from myapp.models import Book
# from myapp.models import Author

TOPIC_CHOICES = (
    ('leve1','好评'),
    ('leve2','中评'),
    ('leve3','差评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(max_length = 100,label = '标题')
    mail = forms.EmailField(label = '邮件')
    topic = forms.ChoiceField(choices = TOPIC_CHOICES,label = '评价')
    message = forms.CharField(label = '内容',widget = forms.Textarea)
    cc_myself = forms.BooleanField(required = False,label = '订阅')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        #
        fields = ('title','publication_date','publisher')
        labels = {
        #命名根据类的名字
            'title':'标题',
            'publication_date':'出版时间',
            'publisher':'出版社号',
        }



# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         # fields = '__all__'
#         fields = ('first_name','last_name','age','email')
#         labels = {
#             'first_name':'名字',
#             'last_name':'姓',
#             'age':'年龄',
#             'email':'邮件',
#         }
