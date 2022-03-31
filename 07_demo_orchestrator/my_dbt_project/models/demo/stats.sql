--This is for src sql files
{{
  config(materialized='table')
}}

WITH src AS (

	SELECT
		_AIRBYTE_AB_ID,
		_AIRBYTE_EMITTED_AT,
		CURRENT_TIMESTAMP AS ELT_UPDATED_AT,
		{{airbyte_json_column_grab(source('epidemic', '_airbyte_raw_epidemic_stats'),'_AIRBYTE_DATA')}}

	FROM {{ source('epidemic', '_airbyte_raw_epidemic_stats') }}

)


SELECT * FROM src
