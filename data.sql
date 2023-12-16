/*students*/
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

INSERT INTO students (name, group_id) VALUES
('James Krasicki', 1),
('Emily Nowak', 2),
('Michael Wojcik', 1),
('Olivia Dabrowski', 3),
('Liam Kowalczyk', 2),
('Sophia Kaminski', 1),
('Jacob Lewandowski', 3),
('Emma Lukasiewicz', 2),
('Mia Wojciechowski', 1),
('Noah Kaminski', 3),
('Ava Kowal', 2),
('Isabella Zajac', 1),
('William Szymanski', 3),
('Amelia Wozniak', 2),
('Alexander Duda', 1),
('Daniel Mazur', 3),
('Grace Pawlowski', 2),
('Henry Zalewski', 1),
('Avery Krol', 3),
('Oliver Majewski', 2),
('Scarlett Nowicki', 1),
('Sebastian Kaczmarek', 3),
('Lily Piotrowski', 2),
('Zachary Jasinski', 1),
('Abigail Grabowski', 3),
('Christopher Nowacki', 2),
('Hannah Sikora', 1);
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