DELETE FROM incomes;
DELETE FROM expenses;
DELETE FROM vehicles;

INSERT INTO vehicles (name, plate, type, odometer_km) VALUES
    ('اتوبوس ۱', '11A111', 'اتوبوس', 250000),
    ('کامیون ۱', '22B222', 'کامیون', 400000),
    ('کامیون ۲', '33C333', 'کامیون', 150000);

INSERT INTO incomes (vehicle_id, date, amount, note) VALUES
    (1, '2026-10-01', 50000000, 'سفر مشهد'),
    (1, '2026-10-10', 30000000, 'سفر شیراز'),
    (2, '2026-10-05', 40000000, 'بار تهران'),
    (3, '2026-10-07', 25000000, 'بار اصفهان');

INSERT INTO expenses (vehicle_id, date, category, amount, note) VALUES
    (1, '2026-10-02', 'سوخت', 8000000, NULL),
    (1, '2026-10-08', 'تعمیر', 12000000, 'لنت'),
    (2, '2026-10-06', 'سوخت', 10000000, NULL);