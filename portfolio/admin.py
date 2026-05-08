"""
Django admin registration for portfolio models.
All models are registered with sensible list_display and search fields.
HireRequest is read-only (no editing contact form submissions).
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteConfig, Experience, Project, Skill, Achievement, HireRequest, SocialLink
)


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1
    fields = ('title', 'url', 'icon_image', 'order')

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    """Singleton site configuration — always edit record #1."""
    fieldsets = (
        ('Resume', {
            'fields': ('resume_file',),
            'description': 'Upload the PDF to enable the Download Resume button.',
        }),
        ('About Section', {
            'fields': ('about_bio',),
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url'),
        }),
        ('SEO', {
            'fields': ('meta_description',),
        }),
    )

    def has_add_permission(self, request):
        """Prevent creating a second config record."""
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deleting the config record."""
        return False


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    search_fields = ('company', 'role', 'bullets')
    ordering = ('order',)
    fieldsets = (
        (None, {
            'fields': ('company', 'company_logo', 'role', 'start_date', 'end_date', 'order'),
        }),
        ('Impact Bullets', {
            'fields': ('bullets',),
            'description': 'Enter one bullet point per line.',
        }),
        ('Certificate', {
            'fields': ('certificate_link', 'certificate_file'),
            'description': 'Provide a link or upload a file for the experience certificate.',
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'tech_stack', 'date_label', 'featured', 'order', 'project_image_preview')
    list_editable = ('featured', 'order')
    search_fields = ('name', 'description', 'tech_stack')
    list_filter = ('featured',)
    ordering = ('order',)

    def project_image_preview(self, obj):
        """Show a thumbnail in the admin list."""
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px; border:2px solid #FF2200;" />',
                obj.image.url
            )
        return '—'
    project_image_preview.short_description = 'Preview'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'name')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('icon_emoji', 'title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(HireRequest)
class HireRequestAdmin(admin.ModelAdmin):
    """
    HireRequest is READ-ONLY — no editing contact form submissions.
    Admin can only view and mark as read.
    """
    list_display = ('name', 'email', 'company', 'submitted_at', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'company', 'message')
    ordering = ('-submitted_at',)
    readonly_fields = ('name', 'email', 'company', 'message', 'submitted_at')

    def has_add_permission(self, request):
        """Disallow manual creation — only form submissions."""
        return False

    def has_change_permission(self, request, obj=None):
        """
        Allow marking as read but no field editing.
        The 'read' field is the only editable thing via list view.
        """
        return True

    def get_fields(self, request, obj=None):
        """Show all fields in detail view (all readonly)."""
        return ('name', 'email', 'company', 'message', 'submitted_at', 'read')
