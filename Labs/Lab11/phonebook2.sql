-- phonebook2.sql

-- 1. Function: Search by pattern (name or phone)
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook2
    WHERE username ILIKE '%' || pattern || '%' OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- 2. Procedure: Insert or update one user
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook2 WHERE username = p_username) THEN
        UPDATE phonebook2 SET phone = p_phone WHERE username = p_username;
    ELSE
        INSERT INTO phonebook2 (username, phone) VALUES (p_username, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


-- 3. Procedure: Insert many users (loop and validation)
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_usernames TEXT[],
    p_phones TEXT[]
)
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_usernames, 1) LOOP
        IF p_phones[i] ~ '^[78][0-9]{10}$' THEN
            PERFORM insert_or_update_user(p_usernames[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone for %: %', p_usernames[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


-- 4. Function: Pagination (LIMIT/OFFSET)
CREATE OR REPLACE FUNCTION get_users_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook2
    ORDER BY id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;


-- 5. Procedure: Delete by username or phone
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook2
    WHERE username = p_value OR phone = p_value;
END;
$$ LANGUAGE plpgsql;
