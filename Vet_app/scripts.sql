CREATE DATABASE IF NOT EXISTS veterinaria_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE veterinaria_db;




CREATE USER IF NOT EXISTS 'vet_user'@'localhost' IDENTIFIED BY 'VetPassword123!';

GRANT ALL PRIVILEGES ON veterinaria_db.* TO 'vet_user'@'localhost';

FLUSH PRIVILEGES;