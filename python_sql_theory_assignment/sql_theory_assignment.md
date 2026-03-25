Q1. Why are Databases Important in Real-World AI Systems?
When I think about AI systems like recommendation engines, chatbots, or fraud detection models — all of them need data to function. And that data has to be stored somewhere in an organized way. That's where databases come in.
Without a proper database, an AI system would have no reliable source of information to learn from or make decisions with.
Types of data typically stored in databases:
User data — names, emails, preferences, login history
Transaction data — purchases, payment records, order history
Model metadata — which AI model version was used, accuracy scores, timestamps

Why structured storage is necessary:
If data is just dumped as raw files or text, it becomes very hard to search, filter, or update. Structured storage (like a relational database) lets us:
Query specific records quickly (e.g., "find all users who bought product X")
Avoid duplicate or missing data
Feed clean, organized data into AI models for training or inference
Example: Netflix's recommendation AI needs structured data like user_id, movie_id, watch_time, and rating stored in tables — not scattered text files.

Q2. The Relational Database Mental Model
The best way I understood relational databases is by thinking of them like Excel sheets — but smarter and more structured.
A relational database organizes data into tables, and each table represents one specific thing (entity) in the real world.
Why should each table represent only one entity?
If we mix multiple entities in one table (like storing both user info and order info together), it leads to:
Repeated data (same user name written 10 times for 10 orders)
Harder updates (if a user changes their email, we'd have to update 10 rows)
Confusion and errors
So we keep users in one table and orders in another — and then connect them using keys.
Example:
users table         orders table
--------            --------
user_id | name      order_id | user_id | item
   1    | Arjun        101   |    1    | Laptop
   2    | Priya        102   |    2    | Phone

Q3. What is a Primary Key?
A primary key is a special column in a table that uniquely identifies each row. No two rows can have the same primary key value, and it can never be empty (NULL).
Why must it be unique?
Because if two rows had the same primary key, we wouldn't be able to tell them apart. Imagine two students with the same roll number — it would cause complete confusion.
Why must it be non-null?
If a row has no primary key, it's essentially "unidentifiable." We can't reference it, update it, or delete it reliably.
Example:
In a students table, student_id is the primary key:
student_id | name   | age
    1      | Arjun  | 20      valid
    2      | Priya  | 22      valid
    2      | Rahul  | 21      duplicate — not allowed
   NULL    | Sneha  | 19      null — not allowed

How do primary keys help?
They act like a unique "ID card" for every record. When other tables want to refer to a specific user or product, they use this primary key to point to the exact row.

Q4. What is a Database Schema?
A schema is like a blueprint or plan of the entire database. It defines the structure before any actual data is inserted.
What does a schema define?
What tables exist in the database
What columns each table has
What data type each column stores (text, number, date, etc.)
Which column is the primary key
What rules/constraints apply (e.g., a column cannot be empty)

Why are schemas important?
Without a schema, anyone could store anything in any format — which would make the data messy and unreliable. A schema enforces consistency.

Q5. How Do Relationships Between Tables Work?
In real-world systems, data is spread across multiple tables, and these tables need to be connected to each other. This is done using foreign keys.
What is a Foreign Key?
A foreign key is a column in one table that refers to the primary key of another table. It creates a link between the two tables.
Example — connecting users and orders:
users table
-----------
user_id (PK) | name   | email
     1       | Arjun  | arjun@email.com
     2       | Priya  | priya@email.com

orders table
------------
order_id (PK) | user_id (FK) | item    | amount
    101       |      1       | Laptop  | 55000
    102       |      2       | Phone   | 20000
    103       |      1       | Mouse   | 1500

Here, user_id in the orders table is a foreign key pointing to user_id in the users table. This tells us:
Order 101 and 103 belong to Arjun
Order 102 belongs to Priya
Why is this useful?
Instead of repeating Arjun's full name and email in every order row, we just store his user_id. This avoids duplication and keeps data clean. When we need full details, we join the two tables.