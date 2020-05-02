SELECT Distinct Email
	FROM 
	(
		SELECT EMail, COUNT(Email) OVER (PARTITION BY Email ORDER BY Email) AS C
		FROM [Person]
	) T
WHERE T.C > 1