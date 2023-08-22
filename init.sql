DROP DATABASE IF EXISTS insights;

CREATE DATABASE insights;

USE insights;

-- Users table to store actor information
CREATE TABLE IF NOT EXISTS users (
    actor_id INT PRIMARY KEY, -- GitHub actor ID
    actor_login VARCHAR(255)  -- GitHub actor login
);

-- Repositories table to store repository information
CREATE TABLE IF NOT EXISTS repositories (
    repo_id INT PRIMARY KEY,          -- GitHub repository ID
    repo_name VARCHAR(255),           -- GitHub repository name
    repo_url VARCHAR(255)             -- GitHub repository URL
);

-- GitHub events table with foreign keys to users and repositories tables
CREATE TABLE IF NOT EXISTS github_events (
    id BIGINT PRIMARY KEY,       -- GitHub event ID
    actor_id INT,                -- GitHub actor ID (foreign key)
    repo_id INT,                 -- GitHub repository ID (foreign key)
    event_type VARCHAR(50),      -- Type of the event
    created_at DATETIME,         -- Event creation time
    FOREIGN KEY (actor_id) REFERENCES users(actor_id),
    FOREIGN KEY (repo_id) REFERENCES repositories(repo_id)
);
