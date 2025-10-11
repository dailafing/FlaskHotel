# Criteria Matching - Flask Hotel

[← Back to Readme](../../Readme.md)

This document maps each Level 5 Diploma Project 3 criterion to the implementation in the Flask Hotel application. Criteria are sourced from both the iungo Solutions Project Criteria and Gateway Qualifications Unit Learning Outcomes.

## Unit Learning Outcome 1: Design, develop and implement a Back end for a web application using Python and a framework

| Criterion | Requirement | Implementation Evidence | Status |
|-----------|-------------|------------------------|--------|
| **1.1** | Design a Front end for a data-driven web application that meets accessibility guidelines, follows UX principles, has structured layout, navigation model, and clearly meets its intended purpose | • **Accessibility**: Semantic HTML (`<nav>`, `<main>`, `<section>`) in `app/templates/base.html`<br>• **Aria-labels**: Form labels with `for` attributes in `app/templates/book.html`<br>• **Screen readers**: `aria-live="polite"` for flash messages in `app/templates/base.html`<br>• **UX**: Bootstrap 5 responsive design, clear navigation in `app/templates/base.html`<br>• **Structured Layout**: Consistent sections, proper headers, Bootstrap grid system<br>• **Navigation**: Navbar with login/logout, my bookings, contact links in `app/templates/base.html`<br>• **Purpose**: Clear hotel booking system - users can browse rooms in `app/templates/index.html` and make bookings | Done |
| **1.2** | Implement custom HTML and CSS code for responsive full-stack application with data manipulation functions and dynamic user interaction | • **Full-Stack**: Flask backend + HTML/CSS frontend working together<br>• **Data Manipulation**: CRUD operations for users, rooms, bookings in `app/routes.py`<br>• **Dynamic Interaction**: Form submissions, flash messages, real-time validation<br>• **Responsive**: Bootstrap 5 responsive grid, mobile-friendly design<br>• **Custom CSS**: `app/static/css/style.css` with custom styling and variables | Done |
| **1.3** | Build database-backed web application allowing users to store and manipulate data records | • **CRUD Operations**: Create (register, book), Read (view rooms/bookings), Update (edit booking), Delete (cancel booking) in `app/routes.py`<br>• **Database Schema**: Well-designed with User, Room, Booking entities in `app/models.py`<br>• **Form Handling**: WTForms with validation in `app/forms.py`, proper database operations | Done |
| **1.4** | Design database structure relevant to domain with relationships between entities | • **Entities**: User (customers), Room (accommodation), Booking (reservations) in `app/models.py`<br>• **Relationships**: User → Booking (one-to-many), Room → Booking (one-to-many)<br>• **Normalization**: Proper foreign keys, no redundancy<br>• **Data Types**: Appropriate types (Date, String, Integer, Float)<br>• **Constraints**: NOT NULL, UNIQUE email, primary keys<br>• **Schema Diagram**: Available at `docs/img/SchemaDiagram.png` | Done |
| **1.5** | Design and implement test procedures (automated or manual) to assess functionality, usability, responsiveness and data management | • **Manual Testing**: Comprehensive test plan in `docs/TestPlan.md` with 11 test cases and screenshots<br>• **Test Coverage**: Functionality, usability, responsiveness and data management all tested<br>• **Documentation**: All test cases and results clearly documented<br>• **Debugging**: Issues identified and resolved (see TestPlan.md) | Done |
| **1.6** | Write Python code consistent with PEP8 style guide and validated HTML and CSS code | • **PEP8 Compliance**: Consistent naming, indentation, line length<br>• **HTML Validation**: ✅ **COMPLETED** - All templates validated using W3C Markup Validator (see [HTML/CSS Validation Report](../htmlCssValidation.md))<br>• **CSS Validation**: ✅ **COMPLETED** - Custom CSS validated using W3C CSS Validator (see [HTML/CSS Validation Report](../htmlCssValidation.md))<br>• **Code Quality**: Clean, readable code throughout | Done |
| **1.7** | Write Python logic demonstrating proficiency in the language | • **Data Types**: Strings, integers, floats, booleans, dates in `app/models.py` and `app/routes.py`<br>• **Collections**: Lists (room queries), dictionaries (form data), tuples<br>• **Operators**: Comparison, logical, arithmetic operators<br>• **Real Problems**: Booking overlap detection in `app/routes.py`, password hashing in `app/models.py`, form validation | Done |
| **1.8** | Include functions with compound statements (if conditions and/or loops) | • **Control Structures**: `if/elif/else` in booking validation, authentication in `app/routes.py`<br>• **Loops**: `for` loops in templates, query filtering<br>• **Compound Logic**: Overlap detection algorithm in `app/routes.py`, form validation chains<br>• **Modular Functions**: Reusable functions with meaningful parameters | Done |
| **1.9** | Write code meeting minimum standards for readability (comments, indentation, naming conventions) | • **Naming**: Clear, descriptive variable and function names throughout codebase<br>• **Indentation**: Consistent 4-space indentation in all Python files<br>• **Comments**: Comprehensive explanatory comments for complex logic (overlap detection, password hashing, webhook validation)<br>• **Structure**: Well-organized code with clear separation of concerns and docstrings for all functions | Done |
| **1.10** | Name files consistently and descriptively without spaces or capitalisation | • **Naming Convention**: All files use lowercase with underscores<br>• **Descriptive**: `booking_form.py`, `user_models.py`, `deploy_hook.py`<br>• **Cross-platform**: No spaces, no capital letters<br>• **Extensions**: Appropriate file extensions (.py, .html, .css) | Done |

## Unit Learning Outcome 2: Model and manage data

| Criterion | Requirement | Implementation Evidence | Status |
|-----------|-------------|------------------------|--------|
| **2.1** | Design a data model that fits the purpose of the project | • **Key Entities**: User (customers), Room (accommodation), Booking (reservations) in `app/models.py`<br>• **Attributes**: User (name, email, password), Room (name, description, price), Booking (dates, status)<br>• **Relationships**: One-to-many relationships between User/Booking and Room/Booking<br>• **Use Cases**: Supports registration, room browsing, booking creation/editing/deletion<br>• **ER Diagram**: Visual representation in `docs/img/SchemaDiagram.png` | Done |
| **2.2** | Develop the model into a usable relational database with consistent and well-organised data storage | • **Tables**: User, Room, Booking tables with appropriate field names and data types in `app/models.py`<br>• **Primary Keys**: Unique identification for all records<br>• **Foreign Keys**: Referential integrity between User/Booking and Room/Booking<br>• **Sample Data**: Database populated with rooms and test data<br>• **Organization**: Logically organized, easy to query and maintain | Done |

## Unit Learning Outcome 3: Query and manipulate data

| Criterion | Requirement | Implementation Evidence | Status |
|-----------|-------------|------------------------|--------|
| **3.1** | Create functionality for users to create, locate, display, edit and delete records | • **Create**: User registration in `app/routes.py` register(), room booking creation in book_room()<br>• **Read**: View rooms in `app/templates/index.html`, view user bookings in my_bookings()<br>• **Update**: Edit existing bookings in edit_booking()<br>• **Delete**: Cancel/delete bookings in delete_booking()<br>• **CRUD Operations**: All operations implemented with proper form handling and database operations | Done |

## Unit Learning Outcome 4: Deploy a Full Stack web application to a Cloud platform

| Criterion | Requirement | Implementation Evidence | Status |
|-----------|-------------|------------------------|--------|
| **4.1** | Deploy final version to cloud-based hosting platform and test to ensure it matches development version | • **Cloud Platform**: Deployed on PythonAnywhere<br>• **Live URL**: https://dailafing.pythonanywhere.com/<br>• **Functionality**: All features working on live deployment<br>• **Testing**: Manual testing performed on live site (see TestPlan.md) | Done |
| **4.2** | Ensure deployed application is free of commented out code and has no broken internal links | • **Clean Code**: Verified - no commented-out code found in codebase<br>• **Link Testing**: All internal links tested and working<br>• **Navigation**: All menu items and buttons function correctly<br>• **No 404s**: All routes properly configured and accessible | Done |
| **4.3** | Document deployment process in README file explaining application purpose and value | • **Purpose**: Clearly described in `Readme.md` - paperless hotel booking system<br>• **Value**: Solves paper-based booking management for small accommodation providers<br>• **Deployment Instructions**: Detailed setup steps, prerequisites, local and production setup<br>• **Platform Info**: PythonAnywhere configuration, environment variables, webhook deployment | Done |

## Unit Learning Outcome 5: Identify and apply security features

| Criterion | Requirement | Implementation Evidence | Status |
|-----------|-------------|------------------------|--------|
| **5.1** | Use Git & GitHub for version control up to deployment with commit messages documenting development process | • **Git Usage**: Regular commits with clear messages<br>• **GitHub Repository**: Complete project stored on GitHub<br>• **Version History**: Evidence of development process through commit history<br>• **Deployment Integration**: GitHub webhook for automatic deployment in `app/deployhook.py` | Done |
| **5.2** | Commit final code free of passwords or secret keys to repository and hosting platform | • **No Hardcoded Secrets**: All sensitive data in environment variables<br>• **Clean Repository**: No passwords, API keys, or credentials in code<br>• **Secure Storage**: Secrets stored in environment files on server | Done |
| **5.3** | Use environment variables or gitignore files to hide all secret keys | • **Environment Variables**: SECRET_KEY, database credentials in .env files<br>• **Gitignore**: Sensitive files excluded from repository in `.gitignore`<br>• **Server Configuration**: Production secrets in server environment | Done |
| **5.4** | Ensure DEBUG mode is turned off in production versions | • **Production Config**: DEBUG = False in production environment<br>• **Security**: No debug information exposed in live application<br>• **Environment Separation**: Different configs for development and production | Done |

## Additional Security Features Implemented

- **Password Hashing**: bcrypt for secure password storage in `app/models.py`
- **CSRF Protection**: Enabled on all forms via Flask-WTF in `app/forms.py`
- **Session Security**: Secure and HttpOnly cookie flags
- **Input Validation**: WTForms validation on all user inputs
- **SQL Injection Prevention**: SQLAlchemy ORM prevents SQL injection
- **Authentication**: Flask-Login for secure user sessions

## Outstanding Requirements

All criteria have been successfully implemented and documented. No outstanding requirements remain.

## File References

- **Models**: `app/models.py` - Database schema and relationships
- **Routes**: `app/routes.py` - CRUD operations and business logic
- **Forms**: `app/forms.py` - Form validation and user input handling
- **Templates**: `app/templates/` - Frontend HTML with accessibility features
- **Styling**: `app/static/css/style.css` - Custom CSS with responsive design
- **Configuration**: `instance/config.py` - Environment-based configuration
- **Testing**: `docs/TestPlan.md` - Manual tests with screenshots
- **Deployment**: `app/deployhook.py` - GitHub webhook for automatic deployment
- **Documentation**: `Readme.md` - Complete setup and deployment instructions