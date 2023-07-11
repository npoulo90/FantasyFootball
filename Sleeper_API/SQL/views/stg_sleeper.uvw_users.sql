create view stg_sleeper.uvw_users
AS
SELECT [username]
      ,[user_id]
      ,[display_name]
FROM [FantasyFootball].[raw_sleeper].[users]