select b.Id from Weather a, Weather b
where b.Recorddate = dateadd(day,1,a.recorddate)
and a.temperature < b.temperature