

declare @json varchar(max)
set @json = (select settings from raw_sleeper.leagues where league_id = '858366433351020544')

select * from openJSON(@json)

--print(@json)