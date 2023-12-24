/*students*/
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

INSERT INTO students (student_id, name, group_id) VALUES
(1, 'James Krasicki', 1),
(2, 'Emily Nowak', 2),
(3, 'Michael Wojcik', 1),
(4, 'Olivia Dabrowski', 3),
(5, 'Liam Kowalczyk', 2),
(6, 'Sophia Kaminski', 1),
(7, 'Jacob Lewandowski', 3),
(8, 'Emma Lukasiewicz', 2),
(9, 'Mia Wojciechowski', 1),
(10, 'Noah Kaminski', 3),
(11, 'Ava Kowal', 2),
(12, 'Isabella Zajac', 1),
(13, 'William Szymanski', 3),
(14, 'Amelia Wozniak', 2),
(15, 'Alexander Duda', 1),
(16, 'Daniel Mazur', 3),
(17, 'Grace Pawlowski', 2),
(18, 'Henry Zalewski', 1),
(19, 'Avery Krol', 3),
(20, 'Oliver Majewski', 2),
(21, 'Scarlett Nowicki', 1),
(22, 'Sebastian Kaczmarek', 3),
(23, 'Lily Piotrowski', 2),
(24, 'Zachary Jasinski', 1),
(25, 'Abigail Grabowski', 3),
(26, 'Christopher Nowacki', 2),
(27, 'Hannah Sikora', 1),
(28, 'Camilleus Rex', 3),
(29, 'Octavian August', 3),
(30, 'Matthias El Guerriero', 3);


/*subjects*/
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    professor_id INTEGER
);

INSERT INTO groups (name) VALUES
(1, 'Grupa 1'),
(2, 'Grupa 2'),
(3, 'Grupa 3');

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