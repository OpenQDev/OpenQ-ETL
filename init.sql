DROP DATABASE IF EXISTS insights;

CREATE DATABASE insights;

USE insights;

CREATE TABLE github_events (
    id BIGINT PRIMARY KEY,
    event_type VARCHAR(50),
    actor_id BIGINT,
    actor_login VARCHAR(100),
    actor_display_login VARCHAR(100),
    actor_url VARCHAR(255),
    actor_avatar_url VARCHAR(255),
    repo_id BIGINT,
    repo_name VARCHAR(255),
    repo_url VARCHAR(255),
    payload_commit_author_email VARCHAR(100),
    payload_commit_author_name VARCHAR(100),
    is_public BOOLEAN,
    created_at TIMESTAMP
);