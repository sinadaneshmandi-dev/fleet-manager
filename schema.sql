CREATE TABLE Vehicles
(
	ID INT PRIMARY KEY,
	Name TEXT NOT NULL,
	Plate TEXT,
	Type TEXT,
	odometer_km INTEGER DEFAULT 0
	);
	
CREATE TABLE Expenses
(
		ID INT PRIMARY KEY,
		Vehicle_ID INT REFERENCES Vehicles(ID),
		Date TEXT NOT NULL,           
		Category TEXT NOT NULL,       
		Amount INT NOT NULL,
		Note TEXT
		);
	
CREATE TABLE Incomes 
(
    ID INTEGER PRIMARY KEY,
    Vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    Date TEXT NOT NULL,
    Amount INT NOT NULL,
    Note TEXT
);