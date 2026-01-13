from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    #這行是去資料庫把所有Todo抓出來。-date的負號代表「倒序」，也就是讓最新的待辦事項排在最上面。
    item_list = Todo.objects.order_by("-date")
    #處理新增請求 (POST)，提交資料 (POST)
    if request.method == "POST":
        #將使用者填寫的內容裝進表單
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            #執行 redirect。這會發送一個指令叫瀏覽器：請改用 GET 方法重新開啟這個網頁
            #瀏覽器重新載入網頁。這時它心裡記得的是：「我剛剛是用 GET 進來的。
            #安全： 這時使用者按 F5（重新整理），瀏覽器只是重複執行 GET（看網頁），不會再存一次資料
            return redirect('todo')
    #單純看網頁 (GET)，跳過整個 if 區塊（因為這不是 POST）
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST" 
    }
    #把空白表單顯示在網頁上
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed")
    return redirect('todo')
