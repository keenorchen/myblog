from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 显示在admin控制台中的列名
    list_display = ('title', 'content', 'pub_time')
    # 时间过滤器
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)

