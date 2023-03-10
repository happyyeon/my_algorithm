-- 코드를 입력하세요
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE*S.SALES) AS TOTAL_SALES
FROM BOOK B, AUTHOR A, BOOK_SALES S
WHERE YEAR(S.SALES_DATE) = 2022 AND MONTH(S.SALES_DATE) = 1 AND B.BOOK_ID = S.BOOK_ID AND B.AUTHOR_ID = A.AUTHOR_ID
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY B.AUTHOR_ID, B.CATEGORY DESC