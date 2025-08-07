from django.contrib import admin
from .models import Event, Comment, Question, Answer, SocietySubmission

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'society', 'date', 'location', 'created_by', 'created_at')
    list_filter = ('society', 'date', 'created_at')
    search_fields = ('title', 'description', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'author', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username', 'event__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = "Content Preview"

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'society', 'author', 'created_at')
    list_filter = ('society', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username', 'question__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = "Content Preview"

@admin.register(SocietySubmission)
class SocietySubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'submitted_by', 'is_approved', 'submitted_at')
    list_filter = ('is_approved', 'submitted_at')
    search_fields = ('name', 'location', 'email', 'submitted_by__username')
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at',)
    actions = ['approve_submissions', 'reject_submissions']
    
    def approve_submissions(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"Approved {queryset.count()} society submissions.")
    approve_submissions.short_description = "Approve selected submissions"
    
    def reject_submissions(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"Rejected {queryset.count()} society submissions.")
    reject_submissions.short_description = "Reject selected submissions"
