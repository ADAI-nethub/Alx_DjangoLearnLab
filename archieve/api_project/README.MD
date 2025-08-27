# 🌍 A.D.Ai API — adai_api

A Django REST Framework backend for **Atomos Dubaako (A.D.Ai)** — a gamified, AI-assisted cultural tourism platform aligned with the **Great Green Wall Initiative**.

This API enables users to discover, book, and contribute to **location-based workshops** focused on art, sustainability, and African cultural heritage. It also allows role-based interactions, storytelling, and gamified engagement through points.

---

## 🚀 Features

- 🌐 **Role-based user system**: Tourists, Artists, Local Guides, and Administrators
- 📍 **Workshops**: Location-aware, date-specific art/cultural events
- ✍️ **Stories**: User-submitted reflections/media tied to workshops
- 🪙 **Gamification**: Point system to encourage participation and contribution
- ⚙️ RESTful API powered by Django REST Framework

---

## 🏗️ Project Structure
adai_api/
│
├── api/ # Core application
│ ├── models.py # Data models: UserProfile, Workshop, Story
│ ├── views.py # API logic using DRF ViewSets
│ ├── serializers.py # ModelSerializers for API output/input
│ ├── urls.py # API endpoint routing
│ └── ...
│
├── api_project/ # Django project config
│ ├── settings.py # Project settings
│ ├── urls.py # Includes api.urls
│ └── ...
│
├── db.sqlite3 # Development database
├── manage.py
└── README.md



Poku Cheremeh
WhatsApp: +233 504083325
ALX Backend Developer | Data Science Learner
Email: cnanapoku@hotmail.com
LinkedIn: LinkedIn URL
GitHub/Portfolio: https://github.com/ADAI-nethub