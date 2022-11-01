CREATE TABLE message
(
    message_id SERIAL PRIMARY KEY,
    plugin_id TEXT,
    plugin_key TEXT,
    plugin_secret TEXT,
    message JSONB,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX plugin_info ON message (plugin_id, plugin_key, plugin_secret);