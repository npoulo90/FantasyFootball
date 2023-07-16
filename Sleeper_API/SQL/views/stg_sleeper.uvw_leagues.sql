USE [FantasyFootball]
GO

/****** Object:  View [stg_sleeper].[uvw_leagues]    Script Date: 7/9/2023 10:58:55 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE VIEW [stg_sleeper].[uvw_leagues]
AS
SELECT cast(league_id AS BIGINT) AS league_id,
	cast([name] AS VARCHAR(100)) AS league_name,
	cast(total_rosters AS INT) AS total_rosters,
	cast(season_type AS VARCHAR(50)) AS season_type,
	cast(season AS INT) AS season,
	cast(draft_id AS BIGINT) AS draft_id,
	cast(bracket_id AS BIGINT) AS bracket_id
FROM raw_sleeper.leagues
GO


