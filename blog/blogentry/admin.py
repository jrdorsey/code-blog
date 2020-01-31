from django.contrib import admin
from blogentry.models import BlogEntry, BlogCategory, BlogImage, BlogCodeSnippet

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogCodeSnippetInline(admin.TabularInline):
    model = BlogCodeSnippet
    extra = 1

class BlogEntryAdmin(admin.ModelAdmin):
    fields = ["title", "body", "category", "user", "posted"]
    ordering = ["posted"]
    inlines = [BlogImageInline, BlogCodeSnippetInline, ]
    
    def __unicode__(self):
       return self.title

admin.site.register(BlogEntry, BlogEntryAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {'slug': ('title',)}
    ordering = ["title"]

    def __unicode__(self):
       return self.title

admin.site.register(BlogCategory, BlogCategoryAdmin)
