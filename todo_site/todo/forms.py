#從 Django 倉庫裡拿出「表單工具箱」
from django import forms
#告訴 Django：「我要根據我們之前在同一個資料夾下定義好的 Todo 模型來製作表單」
from .models import Todo
#在 Django 中，TodoForm 繼承自 ModelForm，它的任務是幫你把資料庫的模型（Model）轉化成網頁表單
#TodoForm（本體）：代表這個表單**「是什麼」以及它具備什麼「功能」**
class TodoForm(forms.ModelForm):
    #class Meta（設定）：代表這個表單**「如何與外界連結」。
    # 它像是一個「參數面板」**，用來告訴 Django 引擎如何去讀取你的設計圖
    class Meta:
        model = Todo
        #「把 Todo 模型裡的所有欄位（title、details、date）通通都放到表單上，讓使用者可以填寫」
        fields = "__all__"
        # 新增這段：把日期欄位變成 HTML5 的日期選擇器
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        