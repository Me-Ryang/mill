-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS I ON (I.ANIMAL_ID = A.ANIMAL_ID)
WHERE I.ANIMAL_ID IS NULL
ORDER BY 1