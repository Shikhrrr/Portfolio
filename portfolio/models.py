"""
Portfolio models — all content for Shikhar Kanaujia's portfolio site.
"""

from django.db import models


class SiteConfig(models.Model):
    """
    Singleton model for global site configuration.
    Only one record should ever exist — enforced via save() override.
    """
    resume_file = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True,
        help_text='Upload the resume PDF here. Will be served as Shikhar_Kanaujia_Resume.pdf',
    )
    about_bio = models.TextField(
        default='',
        help_text='The bio text that appears in the About section.',
    )
    linkedin_url = models.URLField(
        blank=True,
        default='https://linkedin.com/in/shikhar-kanaujia',
        help_text='Full LinkedIn profile URL',
    )
    github_url = models.URLField(
        blank=True,
        default='https://github.com/shikhar-kanaujia',
        help_text='Full GitHub profile URL',
    )
    meta_description = models.CharField(
        max_length=300,
        default='Shikhar Kanaujia — Software Engineer, AI Builder, CS @ IIIT Sonepat.',
        help_text='Meta description for SEO (max 300 chars)',
    )

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return 'Site Configuration'

    def save(self, *args, **kwargs):
        """Enforce singleton — only one SiteConfig record allowed."""
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        """Return the single config instance, creating defaults if needed."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Experience(models.Model):
    """Work experience / internship entries."""
    company = models.CharField(max_length=200)
    company_logo = models.ImageField(
        upload_to='company_logos/',
        blank=True,
        null=True,
        help_text='Company logo image (square aspect ratio recommended)',
    )
    role = models.CharField(max_length=200)
    start_date = models.CharField(
        max_length=50,
        help_text='e.g. "Feb 2026"',
    )
    end_date = models.CharField(
        max_length=50,
        help_text='e.g. "Apr 2026" or "Present"',
    )
    bullets = models.TextField(
        help_text='One bullet point per line. Each line will be displayed as a list item.',
    )
    order = models.IntegerField(
        default=0,
        help_text='Lower numbers appear first (top of timeline).',
    )

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f'{self.role} @ {self.company}'

    def get_bullets_list(self):
        """Return bullets as a Python list, stripping empty lines."""
        return [b.strip() for b in self.bullets.splitlines() if b.strip()]


class Project(models.Model):
    """Portfolio project entries."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=500,
        help_text='Comma-separated technologies, e.g. "Django, REST API, JavaScript"',
    )
    github_url = models.URLField(blank=True, default='#')
    demo_url = models.URLField(blank=True, default='#')
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text='Project screenshot or preview image (800x450px recommended)',
    )
    featured = models.BooleanField(
        default=True,
        help_text='Featured projects appear first in the grid.',
    )
    order = models.IntegerField(
        default=0,
        help_text='Lower numbers appear first.',
    )
    date_label = models.CharField(
        max_length=50,
        blank=True,
        default='',
        help_text='Display date label, e.g. "July 2025"',
    )

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_tech_list(self):
        """Return tech stack as a Python list."""
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Skill(models.Model):
    """Individual skill entries grouped by category."""

    CATEGORY_CHOICES = [
        ('Languages', 'Languages'),
        ('Frameworks & Tools', 'Frameworks & Tools'),
        ('AI/ML', 'AI/ML'),
        ('Databases', 'Databases'),
        ('Concepts', 'Concepts'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Languages',
    )

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.name} ({self.category})'


class Achievement(models.Model):
    """Achievements, awards, and hackathon entries."""
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')
    icon_emoji = models.CharField(
        max_length=10,
        default='🏆',
        help_text='Single emoji character for the achievement icon',
    )
    order = models.IntegerField(
        default=0,
        help_text='Lower numbers appear first.',
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title


class HireRequest(models.Model):
    """
    Contact form submissions — READ-ONLY in admin.
    No editing allowed; only view and mark as read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, default='')
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(
        default=False,
        help_text='Mark as read once reviewed.',
    )

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Hire Request'
        verbose_name_plural = 'Hire Requests'

    def __str__(self):
        return f'{self.name} <{self.email}> — {self.submitted_at.strftime("%d %b %Y")}'
