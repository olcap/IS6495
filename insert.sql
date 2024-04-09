
INSERT INTO Rooms (id, room_description, room_type, room_rate) VALUES (1, 'Penthouse', 'Premium', '229.00');
INSERT INTO Rooms (id, room_description, room_type, room_rate) VALUES (2, 'Business Suite', 'Premium', '259.00');
INSERT INTO Rooms (id, room_description, room_type, room_rate) VALUES (3, 'King Study', 'Standard', '129.00');
INSERT INTO Rooms (id, room_description, room_type, room_rate) VALUES (4, 'King', 'Standard', '119.00');
INSERT INTO Rooms (id, room_description, room_type, room_rate) VALUES (5, 'Queen', 'Standard', '99.00');

INSERT INTO Room_inventory (room_id, floor) VALUES (1, 1);
INSERT INTO Room_inventory (room_id, floor) VALUES (2, 1);
INSERT INTO Room_inventory (room_id, floor) VALUES (3, 1);
INSERT INTO Room_inventory (room_id, floor) VALUES (4, 1);
INSERT INTO Room_inventory (room_id, floor) VALUES (5, 1);
INSERT INTO Room_inventory (room_id, floor) VALUES (1, 2);
INSERT INTO Room_inventory (room_id, floor) VALUES (2, 2);
INSERT INTO Room_inventory (room_id, floor) VALUES (3, 2);
INSERT INTO Room_inventory (room_id, floor) VALUES (4, 2);
INSERT INTO Room_inventory (room_id, floor) VALUES (5, 2);
INSERT INTO Room_inventory (room_id, floor) VALUES (1, 3);
INSERT INTO Room_inventory (room_id, floor) VALUES (2, 3);
INSERT INTO Room_inventory (room_id, floor) VALUES (3, 3);
INSERT INTO Room_inventory (room_id, floor) VALUES (4, 3);
INSERT INTO Room_inventory (room_id, floor) VALUES (5, 3);

INSERT INTO Bookings (inv_id, start_date, end_date, status) VALUES (1, '2024-04-10', '2024-04-12', 'Booked');
INSERT INTO Bookings (inv_id, start_date, end_date, status) VALUES (3, '2024-04-15', '2024-04-20', 'Booked');
INSERT INTO Bookings (inv_id, start_date, end_date, status) VALUES (7, '2024-04-22', '2024-04-25', 'Booked');
INSERT INTO Bookings (inv_id, start_date, end_date, status) VALUES (14, '2024-05-01', '2024-05-05', 'Cancelled');
INSERT INTO Bookings (inv_id, start_date, end_date, status) VALUES (9, '2024-05-10', '2024-05-12', 'Booked');
