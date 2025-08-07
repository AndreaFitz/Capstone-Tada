# TADA! The Amateur Dramatic Almanack

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)](https://getbootstrap.com)

A comprehensive web platform for amateur theatre societies to connect, share events, ask questions, and build community. TADA! serves as a central hub for theatre enthusiasts to discover societies, manage events, and engage in meaningful discussions about amateur dramatic arts.

## 🎭 Features Overview

- **Society Directory**: Searchable directory of amateur theatre societies
- **Event Management**: Full CRUD operations for theatre events with image uploads
- **Community Q&A**: Society-specific question and answer system
- **User Authentication**: Secure registration, login, and session management
- **Contact System**: Direct communication with the TADA! team
- **Responsive Design**: Mobile-first design optimized for all devices
- **Performance Optimized**: Lighthouse-compliant with excellent performance scores

## Wireframes

<img width="894" height="638" alt="laptop wireframe" src="https://github.com/user-attachments/assets/7747451f-52d3-4972-b007-9f2a6a229fa7" />
<img width="216" height="356" alt="tablet-wireframe" src="https://github.com/user-attachments/assets/bb776e41-4de4-42ce-a334-bdc226e2d254" />
<img width="409" height="627" alt="mobile wire frame" src="https://github.com/user-attachments/assets/bfa6a167-6b1a-492b-9ee0-7cfcf529572e" />

##  Responsive Design

<img width="1108" height="884" alt="laptop" src="https://github.com/user-attachments/assets/691163d8-e729-411e-b436-e6935336f394" />
<img width="860" height="915" alt="tablet" src="https://github.com/user-attachments/assets/2bae0178-66f6-44fa-be05-278d1b61e451" />
<img width="507" height="886" alt="larger mobile" src="https://github.com/user-attachments/assets/47361eee-020a-47ea-ae5c-6fd93b10d07f" />
<img width="607" height="907" alt="small mobile" src="https://github.com/user-attachments/assets/8a33bde5-772c-4867-a1b0-9cf65a32a970" />


## 🏗️ Project Structure

```
Capstone-Tada/
├── blog/                       # Main Django application
│   ├── models.py              # Database models (Event, Comment, Question, Answer, SocietySubmission)
│   ├── views.py               # View functions handling all CRUD operations
│   ├── forms.py               # Django forms for user input validation
│   ├── admin.py               # Django admin configuration
│   └── templates/blog/        # HTML templates
│       ├── index.html         # Homepage
│       ├── about.html         # About page
│       ├── directory.html     # Society directory with search
│       ├── contact.html       # Contact form
│       ├── login.html         # User login
│       ├── register.html      # User registration
│       ├── edit_event.html    # Event editing interface
│       ├── delete_event.html  # Event deletion confirmation
│       └── society pages/     # Individual society pages
├── theatre_blog/              # Django project configuration
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing configuration
│   └── wsgi.py               # WSGI configuration
├── static/                    # Static files (CSS, images, JavaScript)
├── media/                     # User-uploaded media files
├── requirements.txt           # Python dependencies
└── manage.py                 # Django management script
```

## 🔧 CRUD Functionality

### **Events Management**
Complete Create, Read, Update, Delete operations for theatre events:

#### **Create (C)**
- **Function**: `riverside_players()`, `metropolitan_drama()`, `experimental_theatre_lab()`, `cats_theatre()`
- **Purpose**: Users can create new events for their respective societies
- **Features**: 
  - Event title, description, date/time, location
  - Photo and poster image uploads
  - Society-specific event categorization
  - User authentication required

#### **Read (R)**
- **Function**: Society view functions (e.g., `riverside_players()`)
- **Purpose**: Display all events for each society
- **Features**:
  - Chronological event listing
  - Society-filtered event display
  - Event details with images
  - Public access (no authentication required)

#### **Update (U)**
- **Function**: `edit_event(request, event_id)`
- **Purpose**: Allow event creators to modify their events
- **Features**:
  - Pre-populated form with existing event data
  - Image replacement capability
  - User authorization (only event creator can edit)
  - Success/error messaging

#### **Delete (D)**
- **Function**: `delete_event(request, event_id)`
- **Purpose**: Remove events from the system
- **Features**:
  - Confirmation page before deletion
  - User authorization (only event creator can delete)
  - Automatic redirect to society page
  - Success messaging

### **Comments System**
Full CRUD for event comments:

#### **Create**: `add_comment(request, event_id)`
- Add comments to specific events
- User authentication required
- Automatic timestamp and author assignment

#### **Read**: Embedded in society pages
- Display all comments for each event
- Chronological ordering
- Author attribution

#### **Update**: `edit_comment(request, comment_id)`
- Edit existing comments
- User authorization (only comment author)
- Pre-populated edit form

#### **Delete**: `delete_comment(request, comment_id)`
- Remove comments with confirmation
- User authorization required
- Soft delete with messaging

### **Questions & Answers System**
Complete Q&A CRUD operations:

#### **Questions CRUD**:
- **Create**: Society-specific question posting
- **Read**: Display questions on society pages
- **Update**: `edit_question(request, question_id)`
- **Delete**: `delete_question(request, question_id)`

#### **Answers CRUD**:
- **Create**: `add_answer(request, question_id)`
- **Read**: Display answers under questions
- **Update**: `edit_answer(request, answer_id)`
- **Delete**: `delete_answer(request, answer_id)`

### **Society Submissions**
- **Create**: `directory()` view handles new society submissions
- **Read**: Admin interface for reviewing submissions
- **Update**: Admin approval system
- **Delete**: Admin removal capabilities

## 🎯 Core Functions Description

### **Main Application Views**

#### **`index(request)`**
- **Purpose**: Homepage displaying welcome content and navigation
- **Features**: Hero section, navigation to all societies, user authentication status
- **Template**: `index.html`

#### **`about(request)`**
- **Purpose**: Information about TADA! platform and its mission
- **Features**: Platform description, team information, contact details
- **Template**: `about.html`

#### **`directory(request)`**
- **Purpose**: Central directory of all amateur theatre societies
- **Features**: 
  - Searchable society listings
  - Society submission form for authenticated users
  - Society approval workflow
- **Template**: `directory.html`

#### **`contact(request)`**
- **Purpose**: Direct communication with TADA! administrators
- **Features**: Contact form validation, message handling, success feedback
- **Template**: `contact.html`

### **Society-Specific Views**

#### **`riverside_players(request)`, `metropolitan_drama(request)`, `experimental_theatre_lab(request)`, `cats_theatre(request)`**
- **Purpose**: Individual society pages with full event and Q&A management
- **Features**:
  - Society-filtered events and questions display
  - Event creation forms (authenticated users)
  - Question posting (authenticated users)
  - Comment addition on events
  - Society-specific styling and branding

### **Authentication System**

#### **`login_view(request)`**
- **Purpose**: User authentication and session management
- **Features**: Username/password validation, session creation, redirect handling
- **Template**: `login.html`

#### **`register_view(request)`**
- **Purpose**: New user account creation
- **Features**: User registration form, password validation, automatic login
- **Template**: `register.html`

#### **`logout_view(request)`**
- **Purpose**: Session termination and user logout
- **Features**: Session cleanup, success messaging, homepage redirect

### **Event Management Functions**

#### **`edit_event(request, event_id)`**
- **Purpose**: Event modification interface
- **Security**: User must be event creator
- **Features**: Form pre-population, image handling, validation

#### **`delete_event(request, event_id)`**
- **Purpose**: Event removal with confirmation
- **Security**: User authorization required
- **Features**: Confirmation page, cascade deletion handling

### **Interactive Features**

#### **`add_comment(request, event_id)`**
- **Purpose**: Add user comments to events
- **Security**: Authentication required
- **Features**: Comment validation, author assignment, timestamp

#### **`add_answer(request, question_id)`**
- **Purpose**: Answer community questions
- **Security**: Authentication required
- **Features**: Answer threading, author tracking, society context

## 🗄️ Database Models

### **Event Model**
```python
- title (CharField): Event name
- description (TextField): Detailed event information
- date (DateTimeField): Event date and time
- location (CharField): Event venue
- society (CharField): Associated theatre society
- created_by (ForeignKey): Event creator
- photo/poster (ImageField): Event images
- created_at/updated_at: Timestamps
```

### **Comment Model**
```python
- event (ForeignKey): Associated event
- author (ForeignKey): Comment author
- content (TextField): Comment text
- created_at (DateTimeField): Creation timestamp
```

### **Question Model**
```python
- title (CharField): Question title
- content (TextField): Question details
- author (ForeignKey): Question author
- society (CharField): Target society
- created_at (DateTimeField): Creation timestamp
```

### **Answer Model**
```python
- question (ForeignKey): Associated question
- content (TextField): Answer content
- author (ForeignKey): Answer author
- created_at (DateTimeField): Creation timestamp
```

### **SocietySubmission Model**
```python
- name (CharField): Society name
- location (CharField): Society location
- email (EmailField): Contact email
- submitted_by (ForeignKey): Submitting user
- is_approved (BooleanField): Approval status
```

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/AndreaFitz/Capstone-Tada.git
cd Capstone-Tada
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Database setup**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. **Run development server**
```bash
python manage.py runserver
```

6. **Access the application**
- Homepage: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## 🎨 Technology Stack

- **Backend**: Django 5.2+ (Python web framework)
- **Frontend**: Bootstrap 5.3.0 (Responsive CSS framework)
- **Database**: SQLite (Development), PostgreSQL (Production ready)
- **Authentication**: Django's built-in authentication system
- **Media Handling**: Django file upload system
- **Icons**: Font Awesome 6.5.1
- **Fonts**: Google Fonts (Limelight, Oregano)
- **Performance**: Lighthouse optimized (90+ scores)

## 📱 Responsive Design

- **Mobile-first approach** with Bootstrap grid system
- **Responsive navigation** with collapsible menu
- **Optimized images** with lazy loading
- **Touch-friendly interfaces** for mobile devices
- **Cross-browser compatibility** (Chrome, Firefox, Safari, Edge)

## 🔒 Security Features

- **User authentication** required for all CRUD operations
- **Authorization checks** ensuring users can only edit their own content
- **CSRF protection** on all forms
- **Input validation** and sanitization
- **Secure file upload** handling
- **Session management** with automatic logout

## 🎭 Future Features

- **Newsletter** sign up for monthly newsletter
- **Gallery** for each society to upload photos of productions and rehearsals to increase engagement
- **Community Corner** partnerships with local schools, venues or charities
- **Countdown timer** for each society - countdown to opening night
- **Ticket links** for each society


## 🎭 Contributing

TADA! welcomes contributions from the amateur theatre community. Whether you're a developer, theatre enthusiast, or have ideas for improvement, we'd love to hear from you!

## 📞 Contact

For questions, suggestions, or support, please use the contact form within the application or reach out to the development team.

---

**TADA! - Connecting Amateur Theatre Communities** 🎭
