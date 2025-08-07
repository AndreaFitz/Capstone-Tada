# TADA! The Amateur Dramatic Almanack

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2+-green.svg)](https://djangoproject.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)](https://getbootstrap.com)

A comprehensive web platform for amateur theatre societies to connect, share events, ask questions, and build community. TADA! serves as a central hu## 📱 Responsive Design

- **Mobile-first approach** with Bootstrap grid system
- **Responsive navigation** with collapsible menu
- **Optimized images** with lazy loading
- **Touch-friendly interfaces** for mobile devices
- **Cross-browser compatibility** (Chrome, Firefox, Safari, Edge)

## 🏆 Design & Accessibility Standards

TADA! meets and exceeds modern web development standards:

- ✅ **Semantic HTML**: Professional-grade semantic structure
- ✅ **WCAG Compliance**: Comprehensive accessibility features
- ✅ **User-Friendly Design**: Consistent, polished interface
- ✅ **Responsive Design**: Flawless Bootstrap implementation with no functionality loss

### **Accessibility Features**
- **ARIA attributes** for screen reader compatibility
- **Keyboard navigation** support throughout the application
- **High contrast** color schemes for readability
- **Alt text** for all images and meaningful content
- **Form labels** properly associated with input fields
- **Focus indicators** for enhanced navigation

### **Standards Compliance**
- **HTML5 semantic elements** (`<nav>`, `<main>`, `<section>`, `<article>`)
- **WCAG 2.1 guidelines** implemented across all pages
- **Mobile-first responsive design** ensuring accessibility on all devices
- **Cross-browser compatibility** tested and verifiedheatre enthusiasts to discover societies, manage events, and engage in meaningful discussions about amateur dramatic arts.

## 🎭 Features Overview

- **Society Directory**: Searchable directory of amateur theatre societies
- **Event Management**: Full CRUD operations for theatre events with image uploads
- **Community Q&A**: Society-specific question and answer system
- **User Authentication**: Secure registration, login, and session management
- **Contact System**: Direct communication with the TADA! team
- **Responsive Design**: Mobile-first design optimized for all devices
- **Performance Optimized**: Lighthouse-compliant with excellent performance scores

## 🏗️ Wireframes

<img width="894" height="638" alt="laptop wireframe" src="https://github.com/user-attachments/assets/7747451f-52d3-4972-b007-9f2a6a229fa7" />
<img width="216" height="356" alt="tablet-wireframe" src="https://github.com/user-attachments/assets/bb776e41-4de4-42ce-a334-bdc226e2d254" />
<img width="409" height="627" alt="mobile wire frame" src="https://github.com/user-attachments/assets/bfa6a167-6b1a-492b-9ee0-7cfcf529572e" />

## 🎨 UX Design Process

### **Design Philosophy**
TADA! was designed with a **user-centered approach** focusing on the unique needs of amateur theatre communities. The design process emphasized accessibility, ease of use, and community engagement.

### **User Research & Requirements Analysis**
#### **Target Audience Identification**:
- **Primary Users**: Amateur theatre society members and organizers
- **Secondary Users**: Theatre enthusiasts seeking local groups
- **Tertiary Users**: General public interested in community theatre

#### **User Needs Assessment**:
- **Event Management**: Simple CRUD operations for theatre events
- **Community Building**: Q&A systems for knowledge sharing
- **Information Discovery**: Easy-to-navigate society directory
- **Social Interaction**: Comment systems for engagement
- **Administrative Control**: Comprehensive admin interface

#### **User Stories**:

##### **Epic 1: Event Management**
- **As a** society organizer, **I want to** create new events **so that** members and the public can see what's coming up
- **As a** society member, **I want to** view all events for my society **so that** I can stay informed about activities
- **As an** event creator, **I want to** edit my event details **so that** I can update information if plans change
- **As an** event creator, **I want to** delete my events **so that** I can remove cancelled or outdated events
- **As a** user, **I want to** upload photos and posters for events **so that** events are more visually appealing

##### **Epic 2: Community Engagement**
- **As a** user, **I want to** comment on events **so that** I can express interest or ask questions
- **As a** content author, **I want to** edit my comments and answers **so that** I can correct mistakes or add information
- **As a** content author, **I want to** delete my contributions **so that** I can remove content I no longer want public

##### **Epic 3: Society Discovery**
- **As a** potential member, **I want to** submit a new society **so that** my group can be listed in the directory
- **As an** admin, **I want to** approve or reject society submissions **so that** I can maintain quality control

##### **Epic 4: User Management**
- **As a** new user, **I want to** register for an account **so that** I can participate in the community
- **As a** returning user, **I want to** log in to my account **so that** I can access my content and create new posts
- **As a** user, **I want to** see my authentication status **so that** I know what actions I can perform

##### **Epic 5: Content Security**
- **As a** content creator, **I want** only I can edit or delete my content **so that** my contributions are protected
- **As a** user, **I want** to be required to log in for content creation **so that** all content is attributed to real users
- **As an** admin, **I want** comprehensive content management tools **so that** I can moderate the platform effectively

##### **Epic 6: Platform Information**
- **As a** visitor, **I want to** learn about the TADA! platform **so that** I understand its purpose and benefits
- **As a** user, **I want to** contact the TADA! team **so that** I can get support or provide feedback

### **Information Architecture**
#### **Site Structure Planning**:
```
TADA! Site Map
├── Homepage (Welcome & Navigation Hub)
├── About (Platform Information)
├── Directory (Society Listings & Submissions)
├── Contact (User Support)
└── Society Pages (Individual Community Spaces)
    ├── Events (CRUD Operations)
    ├── Comments (User Interaction)
    └── Q&A (Knowledge Sharing)
```

#### **User Flow Design**:
1. **Discovery Flow**: Homepage → Directory → Society Selection
2. **Engagement Flow**: Society Page → Event Interaction → Comment/Question
3. **Content Creation Flow**: Login → Society Page → Add Event/Question
4. **Administrative Flow**: Admin Login → Dashboard → Content Management

### **Wireframe Development Process**
#### **Initial Sketches**:
- **Low-fidelity wireframes** created for core user journeys
- **Mobile-first approach** ensuring responsive design from conception
- **Iterative refinement** based on user story mapping

#### **Wireframe Evolution**:
- **Desktop Layout**: Focus on content hierarchy and navigation clarity
- **Tablet Layout**: Balanced approach between desktop and mobile experiences
- **Mobile Layout**: Streamlined interface prioritizing essential functions

### **Visual Design Rationale**
#### **Color Scheme Selection**:
- **Dark Theme**: Theatrical ambiance reflecting stage lighting
- **Gold Accents (#d4af37)**: Representing prestige and artistic excellence
- **High Contrast**: Ensuring WCAG accessibility compliance

#### **Typography Choices**:
- **Limelight**: Display font evoking classic theatre marquees
- **Oregano**: Body text providing elegant readability
- **Hierarchical Structure**: Clear content organization and scanning

#### **Component Design**:
- **Card-Based Layout**: Modular content organization
- **Consistent Spacing**: Bootstrap grid system for responsive alignment
- **Interactive Elements**: Clear call-to-action buttons and form designs

### **Responsive Design Strategy**
#### **Breakpoint Planning**:
- **Mobile (≤576px)**: Single-column layout, collapsible navigation
- **Tablet (≤768px)**: Two-column layout where appropriate
- **Desktop (≥992px)**: Full multi-column layout with sidebar content
- **Large Desktop (≥1200px)**: Optimized spacing and content width

#### **Touch Interface Considerations**:
- **Button Sizing**: Minimum 44px touch targets
- **Form Design**: Large input fields for mobile interaction
- **Navigation**: Thumb-friendly menu placement

### **Design Iterations & Refinements**
#### **Initial Challenges**:
- **Content Density**: Balancing information display with readability
- **Navigation Complexity**: Simplifying multi-society architecture
- **Form Usability**: Streamlining event creation process

#### **Solutions Implemented**:
- **Society-Specific Pages**: Dedicated spaces reducing cognitive load
- **Progressive Enhancement**: Core functionality accessible without JavaScript
- **Visual Hierarchy**: Clear content prioritization through typography and spacing

#### **User Feedback Integration**:
- **Simplified Navigation**: Reduced menu complexity based on testing
- **Enhanced Forms**: Added visual feedback for form submission states
- **Improved Accessibility**: Enhanced ARIA labels and keyboard navigation

### **Accessibility Design Decisions**
#### **WCAG 2.1 Compliance**:
- **Color Contrast**: All text meets AA contrast ratios
- **Keyboard Navigation**: Full site accessibility without mouse
- **Screen Reader Support**: Semantic HTML and ARIA attributes
- **Focus Management**: Clear visual focus indicators

#### **Inclusive Design Features**:
- **Alt Text**: Descriptive alternative text for all images
- **Form Labels**: Proper association between labels and inputs
- **Error Handling**: Clear, actionable error messages
- **Loading States**: Visual feedback for all user actions

### **Performance Considerations**
#### **Optimization Strategy**:
- **Lazy Loading**: Images load as needed to improve initial page speed
- **CDN Usage**: External resources served from optimized networks
- **Minimal CSS**: Custom styles complement rather than override Bootstrap
- **Font Optimization**: Google Fonts with display=swap for performance

## 📱Responsive Design

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

## �️ Database Management

TADA! includes a comprehensive Django admin interface for managing all application data. The admin panel provides enhanced functionality for administrators and content managers.

### **Accessing Django Admin**
1. Create a superuser account:
```bash
python manage.py createsuperuser
```
2. Access admin panel: `http://127.0.0.1:8000/admin/`
3. Login with superuser credentials
4. user name: user
5. pasword: theatreblog

### **Admin Interface Features**

#### **Event Management**
- **List View**: Title, society, date, location, creator, creation time
- **Filtering**: Filter by society, event date, creation date
- **Search**: Search by title, description, location
- **Ordering**: Chronological by creation date (newest first)
- **Read-only Fields**: Created at, updated at timestamps

#### **Comment Administration**
- **List View**: Associated event, author, content preview (first 50 characters), creation time
- **Filtering**: Filter by creation date
- **Search**: Search by content, author username, event title
- **Custom Preview**: Content preview method for quick review
- **Ordering**: Chronological by creation date (newest first)

#### **Question Management**
- **List View**: Title, society, author, creation time
- **Filtering**: Filter by society, creation date
- **Search**: Search by title, content, author username
- **Ordering**: Chronological by creation date (newest first)

#### **Answer Administration**
- **List View**: Associated question, author, content preview, creation time
- **Filtering**: Filter by creation date
- **Search**: Search by content, author username, question title
- **Custom Preview**: Content preview for efficient moderation
- **Ordering**: Chronological by creation date (newest first)

#### **Society Submission Management**
- **List View**: Name, location, email, submitted by, approval status, submission time
- **Filtering**: Filter by approval status, submission date
- **Search**: Search by society name, location, email, submitter username
- **Bulk Actions**: 
  - Approve multiple submissions simultaneously
  - Reject multiple submissions simultaneously
- **Custom Actions**: Enhanced messaging for bulk operations
- **Read-only Fields**: Submission timestamp

### **Database Models Structure**

#### **Event Model Fields**
```python
title           # CharField: Event name (max 200 characters)
description     # TextField: Detailed event information
date            # DateTimeField: Event date and time
location        # CharField: Event venue (max 200 characters)
society         # CharField: Associated theatre society
created_by      # ForeignKey: User who created the event
photo           # ImageField: Event poster/image upload
poster          # ImageField: Additional event poster
created_at      # DateTimeField: Auto timestamp on creation
updated_at      # DateTimeField: Auto timestamp on update
```

#### **Comment Model Fields**
```python
event           # ForeignKey: Associated event (CASCADE delete)
author          # ForeignKey: Comment author user
content         # TextField: Comment text content
created_at      # DateTimeField: Auto timestamp on creation
```

#### **Question Model Fields**
```python
title           # CharField: Question title (max 200 characters)
content         # TextField: Question details
society         # CharField: Associated theatre society
author          # ForeignKey: User who posted question
created_at      # DateTimeField: Auto timestamp on creation
```

#### **Answer Model Fields**
```python
question        # ForeignKey: Associated question (CASCADE delete)
author          # ForeignKey: User who provided answer
content         # TextField: Answer content
created_at      # DateTimeField: Auto timestamp on creation
```

#### **Society Submission Model Fields**
```python
name            # CharField: Society name (max 200 characters)
location        # CharField: Society location (max 200 characters)
email           # EmailField: Contact email
description     # TextField: Society description
submitted_by    # ForeignKey: User who submitted society
is_approved     # BooleanField: Admin approval status
submitted_at    # DateTimeField: Auto timestamp on submission
```

### **Database Maintenance**

#### **Migrations**
```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# View migration status
python manage.py showmigrations
```

#### **Data Management**
```bash
# Create database backup
python manage.py dumpdata > backup.json

# Load data from backup
python manage.py loaddata backup.json

# Clear specific app data
python manage.py flush
```

#### **Database Shell Access**
```bash
# Access Django shell for direct database queries
python manage.py shell

# Example: Query all events
>>> from blog.models import Event
>>> Event.objects.all()
```

### **Admin Security Features**
- **Authentication Required**: Admin access restricted to superusers
- **Permission System**: Django's built-in permission framework
- **Audit Trail**: Creation and modification timestamps on all records
- **Content Preview**: Safe content preview without exposing full data
- **Bulk Operations**: Secure bulk approval/rejection with confirmation messages

## �📱 Responsive Design

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
