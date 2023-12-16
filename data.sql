/*students*/
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

INSERT INTO students (name, group_id) VALUES
('John Doe', 1),
('Jane Smith', 2),
('Bob Johnson', 1),
('Camilleus Rex', 3),
('Octavian August', 3),
('Matthias El Guerriero', 3),
;


/*subjects*/
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    professor_id INTEGER
);

INSERT INTO subjects (name, professor_id) VALUES
('Mathematics', 1),
('History', 2),
('Computer Science', 3),
('Worldwide Literature', 4),
('Polish Literature', 5),
('Physics', 6),
('Biology', 7),
('Geography', 8),
('Chemistry', 9),
('Grammary', 10),
;