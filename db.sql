CREATE DATABASE IF NOT EXISTS quik_note;

-- Create Tables

CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(50) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(250) NOT NULL
);


CREATE TABLE IF NOT EXISTS notes (
    id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    title VARCHAR(250) NOT NULL,
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Insert Statements

INSERT INTO users VALUES (id, username, password);

INSERT INTO notes VALUES (id, user_id, title, content);


-- Read Statements

SELECT * FROM users WHERE username = ??;
SELECT * FROM notes WHERE user_id = ??;


-- Delete Statements

UPDATE notes SET title=?? WHERE id = ??;
UPDATE notes SET content=?? WHERE id = ??;
UPDATE notes SET title = ?? and content = ?? WHERE id = ??;

-- Delete Statements

DELETE FROM notes WHERE id = ??;
