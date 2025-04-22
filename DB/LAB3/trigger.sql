CREATE OR REPLACE FUNCTION Birthday()
RETURNS TRIGGER AS $$
DECLARE
    last_sensation RECORD;
    last_sensation_date DATE;
    new_sensation_id INTEGER;
BEGIN
    IF NEW.age <> OLD.age THEN
        -- Получаем последнее Sensation для этого Human.id
        SELECT Sensation.* INTO last_sensation
        FROM Human 
        JOIN Sensation_to_Human ON Human.id = Sensation_to_Human.human_id
        JOIN Sensation ON Sensation_to_Human.sensation_id = Sensation.id
        WHERE Human.id = NEW.id
        ORDER BY Sensation.now_date DESC, Sensation.now_time DESC
        LIMIT 1;
        
        -- Определяем дату(последняя дата + 1) для нового sensation
        IF last_sensation IS NULL THEN
            last_sensation_date := CURRENT_DATE;
        ELSE
            last_sensation_date := last_sensation.now_date;
        END IF;
        
        -- Проверяем возраст и вставляем соответствующее sensation
        IF NEW.age > 18 THEN
            INSERT INTO Sensation (fall_derection, emotion, now_time, now_date, location_id, visible_light_id)
            VALUES (
                'not fall', 
                'unhappy', 
                '00:00:00', 
                last_sensation_date + INTERVAL '1 day', 
                last_sensation.location_id,
                last_sensation.visible_light_id
			)
            RETURNING id INTO new_sensation_id;
        ELSE
            INSERT INTO Sensation (fall_derection, emotion, now_time, now_date, location_id, visible_light_id)
            VALUES (
                'not fall', 
                'happy', 
                '00:00:00', 
                last_sensation_date + INTERVAL '1 day', 
                last_sensation.location_id,
                last_sensation.visible_light_id
            )
            RETURNING id INTO new_sensation_id;
        END IF;
        
        -- Связываем новое sensation с человеком
        INSERT INTO Sensation_to_Human (sensation_id, human_id) 
        VALUES (new_sensation_id, NEW.id);
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER age_mood_trigger
BEFORE UPDATE ON Human
FOR EACH ROW
EXECUTE FUNCTION Birthday();