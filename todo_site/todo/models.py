from django.db import models
from django.utils import timezone

# Create your models here.
#定義資料庫的長相
#在全端開發中，我們不會直接去寫複雜的 SQL 指令來蓋表格，
# 而是透過 Python 寫下一個「類別（Class）」，Django 就會自動幫我們在資料庫
# （如 SQLite 或 MySQL）中建立對應的表格
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    #預設為false(未完成)---增訂功能1
    completed = models.BooleanField(default=False)

    #這是 Python 的特殊方法。它的作用是：當你在後台管理介面（Admin）查看這些資料時，應該「顯示什麼名字」
    def __str__(self):
        return self.title