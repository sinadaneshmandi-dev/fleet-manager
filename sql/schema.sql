CREATE TABLE IF NOT EXISTS vehicles (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    plate TEXT,
    type TEXT,
    odometer_km INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount INTEGER NOT NULL,
    note TEXT
);

CREATE TABLE IF NOT EXISTS incomes (
    id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
    date TEXT NOT NULL,
    amount INTEGER NOT NULL,
    note TEXT
);