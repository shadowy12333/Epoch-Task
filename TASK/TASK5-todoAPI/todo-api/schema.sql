CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed TNTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

#not null 是非空约束
     primary key 为主键
     autoincrement是自己补id