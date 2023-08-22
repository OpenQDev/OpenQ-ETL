DROP DATABASE insights;

CREATE DATABASE insights;

USE insights;

CREATE TABLE github_events (
    id BIGINT PRIMARY KEY,  -- GitHub event ID
    actor_id INT,         -- GitHub actor ID
    actor_login VARCHAR(255), -- GitHub actor login
    repo_id INT,          -- GitHub repository ID
    repo_name VARCHAR(255),          -- GitHub repository ID
    repo_url VARCHAR(255),          -- GitHub repository ID
    event_type VARCHAR(50), -- Type of the event
    created_at DATETIME  -- Event creation time
);
