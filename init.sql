DROP DATABASE IF EXISTS insights;

CREATE DATABASE insights;

USE insights;

CREATE TABLE github_events (
    id BIGINT PRIMARY KEY,
    actor_id BIGINT,
    actor_login VARCHAR(100),
    actor_avatar_url VARCHAR(255),
    repo_id BIGINT,
    repo_name VARCHAR(255),
    author_email VARCHAR(100),
    author_name VARCHAR(100),
    created_at TIMESTAMP
);