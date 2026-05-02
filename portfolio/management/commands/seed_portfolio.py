"""
Management command: seed_portfolio
Seeds the database with all initial content for Shikhar Kanaujia's portfolio.
Run with: python manage.py seed_portfolio
"""

from django.core.management.base import BaseCommand
from portfolio.models import (
    SiteConfig, Experience, Project, Skill, Achievement
)


class Command(BaseCommand):
    help = 'Seeds the portfolio database with initial content for Shikhar Kanaujia.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO('🌱 Seeding portfolio database...'))

        # ------------------------------------------------------------------
        # SITE CONFIG (singleton)
        # ------------------------------------------------------------------
        config, _ = SiteConfig.objects.get_or_create(pk=1)
        config.about_bio = (
            "I'm a Computer Science undergrad at IIIT Sonepat (B.Tech, expected 2027) "
            "with a GPA of 8.2/10. I build AI systems, full-stack web apps, and desktop "
            "tools that solve real problems. I've interned at CyberMedia, won national "
            "hackathons, led my student council, and shipped products used by 1,000+ people "
            "— all before my third year."
        )
        config.linkedin_url = 'https://linkedin.com/in/shikhar-kanaujia'
        config.github_url = 'https://github.com/shikhar-kanaujia'
        config.meta_description = (
            'Shikhar Kanaujia — Software Engineer, AI Builder, CS @ IIIT Sonepat. '
            'Building full-stack apps, RAG pipelines, and systems that scale.'
        )
        config.save()
        self.stdout.write(self.style.SUCCESS('  ✓ SiteConfig'))

        # ------------------------------------------------------------------
        # EXPERIENCE
        # ------------------------------------------------------------------
        Experience.objects.all().delete()

        Experience.objects.create(
            company='CyberMedia',
            company_logo='company_logos/cybermedia.png',
            role='Software Engineering Intern',
            start_date='Feb 2026',
            end_date='Apr 2026',
            order=1,
            bullets=(
                'Built a dual-mode AI sales chatbot capable of switching between '
                'structured FAQ responses and open-ended LLM-driven conversations.\n'
                'Engineered a RAG knowledge base indexing 50–100 documents, enabling '
                'context-aware responses with dramatically reduced hallucination rates.\n'
                'Developed a website scanning feature that analyzes page structure and '
                'content to generate targeted ad placement recommendations.'
            ),
        )

        Experience.objects.create(
            company='IIIT Sonepat',
            company_logo='company_logos/iiit.png',
            role='Desktop Application Developer Intern',
            start_date='Feb 2025',
            end_date='May 2025',
            order=2,
            bullets=(
                'Built a Qt C++ attendance management desktop application now adopted '
                'by 1,000+ students across the institute.\n'
                'Eliminated 90% of paper-based processes, reducing administrative '
                'overhead and improving data accuracy.\n'
                'Received a formal Letter of Recommendation for delivery quality.\n'
                'Shipped with zero critical bugs post-deployment — validated across '
                'multiple departments before rollout.'
            ),
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Experience (2 entries)'))

        # ------------------------------------------------------------------
        # PROJECTS
        # ------------------------------------------------------------------
        Project.objects.all().delete()

        Project.objects.create(
            name='Say App',
            description=(
                'Full-stack microblogging platform with posts, photo uploads, user follows, '
                'likes, threaded replies, full-text search, and a voice comment pipeline. '
                'Achieved ~40% response time reduction via strategic query indexing and '
                'optimized database access patterns. Supports thousands of concurrent interactions.'
            ),
            tech_stack='Django, REST API, JavaScript, Bootstrap, SQLite',
            github_url='https://github.com/shikhar-kanaujia/say-app',
            demo_url='#',
            featured=True,
            order=1,
            date_label='July 2025',
        )

        Project.objects.create(
            name='InvoicerAI',
            description=(
                'Receipt and invoice extraction tool powered by a 4-stage LangChain pipeline '
                'running on local Llama 3. Achieves 80%+ faster extraction versus manual entry '
                'with zero API costs. Uses OCR + LLM reasoning to handle messy, real-world '
                'document formats with high accuracy.'
            ),
            tech_stack='Python, LangChain, Llama 3, OCR, Ollama',
            github_url='https://github.com/shikhar-kanaujia/invoicerai',
            demo_url='#',
            featured=True,
            order=2,
            date_label='August 2025',
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Projects (2 entries)'))

        # ------------------------------------------------------------------
        # SKILLS
        # ------------------------------------------------------------------
        Skill.objects.all().delete()

        skills_data = {
            'Languages': [
                'Python', 'C++', 'JavaScript', 'C', 'SQL', 'Bash',
            ],
            'Frameworks & Tools': [
                'Django', 'Qt (C++)', 'REST Framework', 'LangChain',
                'Git', 'Linux', 'VS Code', 'Postman',
            ],
            'AI/ML': [
                'RAG Pipelines', 'LLM Integration', 'Llama 3', 'Ollama',
                'Prompt Engineering', 'OCR', 'NLP Basics',
            ],
            'Databases': [
                'SQLite', 'PostgreSQL', 'MongoDB', 'Redis (basics)',
            ],
            'Concepts': [
                'Data Structures & Algorithms', 'System Design', 'REST APIs',
                'OOP', 'Computer Networks', 'OS Fundamentals', 'DBMS',
            ],
        }

        for category, skill_names in skills_data.items():
            for name in skill_names:
                Skill.objects.create(name=name, category=category)
        self.stdout.write(self.style.SUCCESS('  ✓ Skills'))

        # ------------------------------------------------------------------
        # ACHIEVEMENTS
        # ------------------------------------------------------------------
        Achievement.objects.all().delete()

        achievements_data = [
            {
                'icon_emoji': '🥉',
                'title': "Igniter's Hackathon 2025 — 3rd Place",
                'description': (
                    'IIIT Kancheepuram — Secured 3rd place in both Web Development '
                    'and Competitive Programming tracks.'
                ),
                'order': 1,
            },
            {
                'icon_emoji': '🔥',
                'title': 'HackZilla 2025 — Top 10 Nationally',
                'description': (
                    'IIIT Sonepat — Ranked in the Top 10 nationally across '
                    'all participating teams.'
                ),
                'order': 2,
            },
            {
                'icon_emoji': '💻',
                'title': '650+ DSA Problems Solved',
                'description': (
                    'Active on LeetCode, CodeChef, and Codeforces. Consistent '
                    'problem-solving practice across arrays, graphs, DP, and more.'
                ),
                'order': 3,
            },
            {
                'icon_emoji': '🎓',
                'title': 'Reliance Foundation Scholar 2024',
                'description': (
                    'Selected at the national level for the Reliance Foundation '
                    'Scholarship — merit-based recognition of academic excellence.'
                ),
                'order': 4,
            },
            {
                'icon_emoji': '👑',
                'title': 'President, Student Council 2025',
                'description': (
                    'Led a 23-member team, drove 35%+ year-on-year event participation '
                    'growth, and coordinated 500+ participants across flagship events '
                    'including Agnito and Smart India Hackathon.'
                ),
                'order': 5,
            },
            {
                'icon_emoji': '🎤',
                'title': 'Host, Agnito 2024',
                'description': (
                    "Anchored IIIT Sonepat's annual technical fest with 500+ attendees, "
                    'managing the full event flow from planning to execution.'
                ),
                'order': 6,
            },
        ]

        for data in achievements_data:
            Achievement.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('  ✓ Achievements (6 entries)'))

        # ------------------------------------------------------------------
        # DONE
        # ------------------------------------------------------------------
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ Portfolio seeded successfully!'))
        self.stdout.write(self.style.HTTP_INFO(
            '   Next: python manage.py createsuperuser → runserver → visit /admin/'
        ))
