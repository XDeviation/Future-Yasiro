DROP TABLE IF EXISTS send_message;
CREATE TABLE send_message
(
    message_id BIGSERIAL PRIMARY KEY,
    plugin_name TEXT,
    message TEXT,
    message_type TEXT,
    message_second_type TEXT,
    user_id TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM send_message;
