DROP DATABASE IF EXISTS insights;

CREATE DATABASE insights;

USE insights;

CREATE TABLE github_events (
    id BIGINT PRIMARY KEY,
    type VARCHAR(50),
    actor_id BIGINT,
    actor_login VARCHAR(50),
    repo_id BIGINT,
    repo_name VARCHAR(255),
    payload_action VARCHAR(50),
    payload_release_id BIGINT,
    payload_release_author_login VARCHAR(50),
    payload_release_author_id BIGINT,
    payload_release_tag_name VARCHAR(50),
    payload_release_name VARCHAR(255),
    created_at TIMESTAMP
);
