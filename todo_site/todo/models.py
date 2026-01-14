from django.db import models
from django.utils import timezone

# Create your models here.
#定義資料庫的長相
#在全端開發中，我們不會直接去寫複雜的 SQL 指令來蓋表格，
# 而是透過 Python 寫下一個「類別（Class）」，Django 就會自動幫我們在資料庫
# （如 SQLite 或 MySQL）中建立對應的表格
class Todo(models.Model):
    #定義優先順序選項---增訂功能2
    PRIORITY_CHOICES = [
        ('H', '高'),
        ('M', '中'),
        ('L', '低')
    ]

    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    #預設為false(未完成)---增訂功能1
    completed = models.BooleanField(default=False)
    # 新增：截止日期 (可以不填)---增訂功能4
    due_date = models.DateField(null=True, blank=True)

    #預設值為 'M' (中)---增訂功能2
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )

    #這是 Python 的特殊方法。它的作用是：當你在後台管理介面（Admin）查看這些資料時，應該「顯示什麼名字」
    def __str__(self):
        return self.title
    
    # 新增一個小工具：判斷是否過期---增訂功能4
    #@property 是 Python 中一個非常優雅且強大的 「裝飾器 (Decorator)」。
    #簡單來說，它的功能是：把一個「函式 (Method)」偽裝成一個「屬性 (Attribute)」
    #加上了 @property 之後，你可以像讀取變數一樣使用它
    #Django 的 HTML 模板系統（Template）不允許你在 HTML 裡面寫括號 () 來呼叫函式
    @property
    def is_overdue(self):
        if self.due_date and self.due_date < timezone.now().date() and not self.completed:
            return True
        return False