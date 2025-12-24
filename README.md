Overview of Student Management System (SMS):

      A Student Management System (SMS) in Python Django is a web application designed 
      to streamline and automate administrative tasks in educational institutions. 
      It typically employs the Django Model-View-Template (MVT) design pattern, 
      using Python for backend logic and HTML/CSS for the frontend user interface. 

Key Features:

      Beyond basic CRUD, a well-structured Django SMS often includes
      
    -Authentication and Authorization: 
    
      Secure login for administrators and potentially students, with permissions defining who can 
      perform which operations.
      
    -Database Management: 
    
      Django's built-in Object-Relational Mapper (ORM) simplifies database interactions, 
      supporting various backends like SQLite (default), PostgreSQL, and MySQL.
      
    -User Interface: 
    
      Utilizing HTML, CSS, and JavaScript within Django templates to provide an intuitive and responsive 
      design for managing records.
      
    -Search and Filtering:
    
      Allowing users to quickly find specific student records based on criteria like name, ID. 

Typical Implementation Flow:

    -Define Models: 
    
      Create a Student model in models.py to define the database schema (e.g., name, ID, email, date of birth).
    
    -Set up URLs:
    
      Map specific URLs to corresponding views in urls.py.
      
    -Create Views: 
    
      Write logic in views.py (either class-based or function-based views) to handle requests and 
      interact with the model and templates.
      
    -Design Templates:
    
      Use Django's template engine to create HTML pages for listing, viewing, adding, updating, 
      and deleting students.
      
    -Configure Forms: 
    
      Use Django forms to handle data input and validation efficiently. 
