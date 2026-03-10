CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(50)
);

CREATE TABLE seats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    showtime_id INT,
    seat_label VARCHAR(5),
    status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    showtime_id INT,
    seat_label VARCHAR(5)
);

-- Test users for login demo
INSERT INTO users (email, password, role)
VALUES
('customer@test.com', 'password123', 'customer'),
('staff@test.com', 'password123', 'staff');

-- Sample seats for showtime 1
INSERT INTO seats (showtime_id, seat_label, status)
VALUES
(1, 'A1', 'available'),
(1, 'A2', 'available'),
(1, 'A3', 'available'),
(1, 'A4', 'available'),
(1, 'A5', 'available')
(1, 'B1', 'available'),
(1, 'B2', 'available'),
(1, 'B3', 'available'),
(1, 'B4', 'available'),
(1, 'B5', 'available');
