USE [FantasyFootball]
GO

/****** Object:  View [stg_sleeper].[uvw_leagues]    Script Date: 7/9/2023 10:58:55 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE view [stg_sleeper].[uvw_leagues] 
as 
select 
 cast(league_id as bigint)				as league_id				
,cast([name] as varchar(100))		as league_name
,cast(total_rosters as int)			as total_rosters
,cast(season_type as varchar(50))	as season_type
,cast(season as int)				as season
,cast(draft_id as bigint)				as draft_id
,cast(bracket_id as bigint)			as bracket_id
from raw_sleeper.leagues
GO


