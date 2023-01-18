-- 코드를 입력하세요
WITH TEMP AS (
    SELECT CATEGORY,MAX(PRICE) AS PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
)
SELECT FP.CATEGORY, FP.PRICE AS MAX_PRICE, FP.PRODUCT_NAME
FROM FOOD_PRODUCT FP
INNER JOIN TEMP
WHERE FP.CATEGORY = TEMP.CATEGORY AND FP.PRICE = TEMP.PRICE AND FP.CATEGORY IN ("과자","국","김치","식용유")
ORDER BY MAX_PRICE DESC