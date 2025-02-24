-- Articoli
INSERT INTO articoli (nome, descrizione, prezzo) VALUES
('Smartphone', 'Samsung smartphone', 599.99),
('T-shirt', 'Tshirt di moda', 19.99),
('Monopoly (Edizione Star Wars)', 'Il classico gioco da tavolo con tema star wars', 129.99),
('Python Crash Course', 'Un libro completo per imparare a programmare in Python', 29.99),
('Laptop', 'Laptop Asus', 899.99),
('Jeans', 'Jeans standard', 49.99),
('Accessori Gatti', 'Set dei tiragraffi e giocatoli', 39.99),
('Film DVD', 'Film a caso', 14.99);

-- Clienti
INSERT INTO customer (nome, cognome) VALUES
('Mario', 'Rossi'),
('Laura', 'Bianchi'),
('Giovanni', 'Verdi');

-- Ordini
INSERT INTO ordini (id_customer, data_ordine, totale) VALUES
(1, '2023-10-26', 619.98), -- Smartphone + T-shirt
(2, '2023-10-27', 179.98), -- Monopoly + Python
(3, '2023-10-28', 949.98); -- Laptop + Jeans

-- Articoli_ordine
INSERT INTO Articoli_Ordine (id_ordine, id_articolo) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6);