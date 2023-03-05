DROP TABLE IF EXISTS plugin_to_user;
CREATE TABLE plugin_to_user (
    id BIGSERIAL PRIMARY KEY,
    plugin_name TEXT,
    plugin_config TEXT,
    user_type TEXT,
    user_id TEXT
);
SELECT *
FROM plugin_to_user;