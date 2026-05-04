DROP DATABASE IF EXISTS reel_deal;
CREATE DATABASE reel_deal;
USE reel_deal;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    poster_path VARCHAR(255)
);

CREATE TABLE showtimes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    show_time VARCHAR(50) NOT NULL,
    auditorium VARCHAR(50) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

CREATE TABLE seats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    showtime_id INT NOT NULL,
    seat_label VARCHAR(5) NOT NULL,
    status VARCHAR(20) DEFAULT 'available',
    FOREIGN KEY (showtime_id) REFERENCES showtimes(id),
    UNIQUE (showtime_id, seat_label)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    showtime_id INT NOT NULL,
    seat_label VARCHAR(5) NOT NULL,
    ticket_code VARCHAR(20) NOT NULL,
    ticket_status VARCHAR(20) DEFAULT 'active',
    booked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (showtime_id) REFERENCES showtimes(id)
);

INSERT INTO users (email, password, role)
VALUES
('customer@test.com', 'password123', 'customer'),
('staff@test.com', 'password123', 'staff');

INSERT INTO movies (title, description, poster_path)
VALUES
('Batman', 'A superhero movie set in Gotham City.', 'images/batman.svg'),
('Toy Story', 'An animated adventure about toys that come to life.', 'images/toy_story.svg'),
('Pulp Fiction', 'A crime drama following interconnected stories in Los Angeles.', 'images/pulp_fiction.svg');

INSERT INTO showtimes (movie_id, show_time, auditorium)
VALUES
(1, '5:30 PM', 'Auditorium 1'),
(1, '7:30 PM', 'Auditorium 1'),
(1, '9:30 PM', 'Auditorium 1'),

(2, '4:00 PM', 'Auditorium 2'),
(2, '6:30 PM', 'Auditorium 2'),
(2, '8:45 PM', 'Auditorium 2'),

(3, '5:00 PM', 'Auditorium 3'),
(3, '7:45 PM', 'Auditorium 3'),
(3, '10:15 PM', 'Auditorium 3');

INSERT INTO seats (showtime_id, seat_label, status)
SELECT
    showtimes.id,
    CONCAT(seat_rows.row_letter, seat_numbers.seat_number),
    'available'
FROM showtimes
CROSS JOIN (
    SELECT 'A' AS row_letter
    UNION ALL SELECT 'B'
    UNION ALL SELECT 'C'
    UNION ALL SELECT 'D'
) AS seat_rows
CROSS JOIN (
    SELECT 1 AS seat_number
    UNION ALL SELECT 2
    UNION ALL SELECT 3
    UNION ALL SELECT 4
    UNION ALL SELECT 5
    UNION ALL SELECT 6
    UNION ALL SELECT 7
    UNION ALL SELECT 8
) AS seat_numbers;