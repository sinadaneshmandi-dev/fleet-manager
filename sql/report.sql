SELECT
    v.name,
    COALESCE(i.total_income, 0) AS total_income,
    COALESCE(e.total_expense, 0) AS total_expense,
    COALESCE(i.total_income, 0) - COALESCE(e.total_expense, 0) AS profit
FROM vehicles v
LEFT JOIN (
    SELECT vehicle_id, SUM(amount) AS total_income
    FROM incomes
    GROUP BY vehicle_id
) i ON i.vehicle_id = v.id
LEFT JOIN (
    SELECT vehicle_id, SUM(amount) AS total_expense
    FROM expenses
    GROUP BY vehicle_id
) e ON e.vehicle_id = v.id
ORDER BY profit DESC;