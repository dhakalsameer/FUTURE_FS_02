from django.contrib import admin
from .models import Lead, LeadNote


class LeadNoteInline(admin.TabularInline):
    model = LeadNote
    extra = 1


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source', 'status', 'created_at')
    list_filter = ('status', 'source', 'created_at')
    search_fields = ('name', 'email', 'source')
    ordering = ('-created_at',)
    inlines = [LeadNoteInline]


@admin.register(LeadNote)
class LeadNoteAdmin(admin.ModelAdmin):
    list_display = ('lead', 'created_by', 'created_at')
    search_fields = ('lead__name', 'note')
